from django.shortcuts import render , redirect
from django.contrib import messages
import zipfile
import folium
from folium import plugins
import matplotlib.pyplot as plt
from .fonctions_backend import *
import shap
import pandas as pd
import numpy as np
import os
import tensorflow as tf
from keras.utils import img_to_array, load_img, save_img
from .forms import UserRegisterForm
import ast
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def client_home(request):
    return render(request, 'HomePages/Client Home Page/client_home.html')

def client_contact(request):
    return render(request, 'HomePages/Client Contact/client_contact.html')

def client_guid(request):
    return render(request, 'HomePages/Client Guid/client_guid.html')

def client_signup(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Compte a etait cree avec success"))
            return redirect('client-login')
        messages.error(request, ("Veuillez vérifier les informations saisies"))
        return redirect('client_signup')
    return render(request, 
            'HomePages/Client Login/client_signup.html',
            {'form': form})

@login_required
def client_map(request):
    return render(request, 'AppPages/Client Dashboard/client_map.html')

@login_required
def client_graph(request): 
    try:
        df2 = pd.read_csv('AI_MAP/static/data/IAV_INSTALLATION_PV.csv' , sep = ';', encoding = 'utf-8', header = 0)
        df2.columns = pd.MultiIndex.from_arrays([df2.columns, df2.iloc[0].values])
        df2 = df2.iloc[1:]
        df2.index = pd.to_datetime(df2.iloc[:,0],dayfirst=True,infer_datetime_format=True,format='mixed')
        df2.drop(columns = df2.columns[0], axis = 1, inplace= True)
        df2 = df2.sort_index(axis=1)
        df2.index.name = None
        df2 = df2.astype(float)
        min_date = df2.index[0].strftime('%Y-%m-%d')
        max_date = df2.index[-1].strftime('%Y-%m-%d')
        vari = df2.columns.values.tolist()
        liste= [a for a in vari]
    except Exception as ex:
        print("Error while connecting to PostgreSQL: \n", ex)

    if request.method == 'POST':
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        grandeur = request.POST.getlist('c[]')

        if grandeur == [] :
            grandeur = "All"
        if 'All' in grandeur :
            grandeur = "All"
        else :
            for a,i in zip(grandeur,range(0,len(grandeur))) :
                grandeur[i] = ast.literal_eval(grandeur[i])

        aggregate = request.POST['d']
        if aggregate == "L'agrégat :" :
            aggregate = 'Moyenne'
        dictionnary = {"fa-regular fa-chart-bar":'bar',"fa-solid fa-chart-line":'line',"fa-regular fa-signal":'stem',"fa-solid fa-chart-pie":'pie'}
        mapper = lambda x :  dictionnary[x]
        choix_graphe = request.POST['e']
        if choix_graphe == 'Le graphe :':
            choix_graphe = 'bar'
        else :
            choix_graphe = mapper(choix_graphe)
        start_day = request.POST['start']
        end_date = request.POST['end']
        if request.POST['fname'] == '' :
            frequency_number = 1
        else :
            frequency_number = int(request.POST['fname'])
        frequency_str = request.POST['frequence']
        dictionnary2 = {"Jours":'D',"Mois":'M',"Semaines":'W',"Années":'Y'}
        mapper2 = lambda x,y :  str(x)+dictionnary2[y] if x not in [0,1] else (dictionnary2[y])
        frequency = mapper2(frequency_number,frequency_str)



        if 'a' in request.POST:
            timeframe = request.POST['a']
        else :
            timeframe = None
        df3 = choix_user_periodrange(df2,start_day,end_date, frequency,timeframe, aggregate, grandeur)
        draw_adaptative_graphs_period(df3,start_day,end_date, frequency,timeframe, aggregate, grandeur,choix_graphe)
        return redirect('client-graph')
    return render(request , 
                  'AppPages/Client Dashboard/client_graph.html',
                  {'min_date':min_date,'max_date':max_date,'liste':liste}
                )

@login_required
def client_geo(request):
    if request.method == 'POST':

        fichier_zip = request.FILES["dossier"]
        with open(fichier_zip.name, 'wb+') as destination:
            destination.write(fichier_zip.read())
        with zipfile.ZipFile(fichier_zip.name, mode="r") as dossier :
            dossier.extractall()
        np.set_printoptions(formatter={'float_kind':'{:f}'.format})
        table1 = pd.DataFrame({'moduleID': pd.Series(dtype='int32'),
                    'Defect_Class': pd.Series(dtype='int'),
                    'Probability': pd.Series(dtype='float')})

        directory = fichier_zip.name[:-4] + '/Modules_ClippedRasters'
        for image_name in os.listdir(directory):
            image = load_img(directory +'/' + image_name,color_mode = "grayscale")
            image = img_to_array(image)
            untouched_image = np.copy(image)
            image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
            image = tf.image.resize_with_pad( image, 100, 100, method=tf.image.ResizeMethod.BILINEAR, antialias=False)

            id = image_name[0:-4]
            model = tf.keras.models.load_model("CLIENT/model/model_6c_11aug_5r_100p_Smote.h5")
            defect_class = np.argmax(model(image))
            probability = np.max(model(image))*100

            if defect_class!=0 :
                #table filling
                table1.loc[len(table1.index)] = [id, defect_class, probability]
                path = "AI_MAP/static/appfunction/ImagesWithDefect/Class" + str(defect_class) +'/' +  image_name
                save_img(path,untouched_image,scale=False)
                image2 = load_img(directory +'/' + image_name,color_mode = "grayscale", target_size=(100,100))
                image2 = img_to_array(image2)
                image2 = image2.reshape((1,image2.shape[0],image2.shape[1],image2.shape[2]))
                masker = shap.maskers.Image("blur(100,100)", image2[0].shape)
                explainer = shap.Explainer(model, masker)
                shap_values = explainer(image2[:1], max_evals=500, batch_size=50, outputs=shap.Explanation.argsort.flip[:1])
                shap.image_plot(shap_values, show=False)
                plt.savefig('AI_MAP/static/appfunction/Interpretation/' + id + '.png')


        table1 = table1.astype({'moduleID':'int32'})
        table2 = pd.read_csv(fichier_zip.name[:-4] + '/centroides.csv',header=0,dtype={'moduleID':'int','X':'str','Y':'str'})
        table_folium = table1.merge(table2, on='moduleID',sort=True)
        coordonnees = pd.read_csv(fichier_zip.name[:-4] + '/CoordonneesProjet.csv',header=0,dtype={'Point':'str','X':'float','Y':'float'})


        # returning a folium map with defects highlighting
        carte = folium.Map(location=[float(coordonnees[coordonnees.Point=='Centre'].Y),float(coordonnees[coordonnees.Point=='Centre'].X )], zoom_start=2, tiles=None, crs='EPSG4326',width='100%',height='80%')
        directory2 = fichier_zip.name[:-4]+ '/Orthos'
        if len(os.listdir(directory2+'/Ortho_RGB')) == 0:
            folium.raster_layers.ImageOverlay(directory2+'/Ortho_Thermique/solarfarm_ortho.png',[[float(coordonnees[coordonnees.Point=='Inferieur_Gauche'].Y),float(coordonnees[coordonnees.Point=='Inferieur_Gauche'].X )],
            [float(coordonnees[coordonnees.Point=='Superieur_Droit'].Y),float(coordonnees[coordonnees.Point=='Superieur_Droit'].X )]],name='Orthomosaique Thermique').add_to(carte)
        else :
            folium.raster_layers.ImageOverlay(directory2+'/Ortho_Ortho_RGB/solarfarm_ortho.png',[[float(coordonnees[coordonnees.Point=='Inferieur_Gauche'].Y),float(coordonnees[coordonnees.Point=='Inferieur_Gauche'].X)],
            [float(coordonnees[coordonnees.Point=='Superieur_Droit'].Y),float(coordonnees[coordonnees.Point=='Superieur_Droit'].X) ]],name='Orthomosaique RGB').add_to(carte)
        plugins.MousePosition(position='bottomright', separator=' / ',num_digits=6).add_to(carte)
        plugins.Fullscreen(position='topleft').add_to(carte)
        plugins.Draw(True, position='bottomleft').add_to(carte)
        plugins.MeasureControl(position='bottomleft').add_to(carte)
        folium.GeoJson(fichier_zip.name[:-4] + '/Installation_GEOJSON/panneaux_centralesolaire.geojson',lambda x:{"color":'#41B3A3',"opacity":0.8},
                zoom_on_click=True,show=False,name='Modules de l\'installation photovoltaique').add_to(carte)

        # Class 1
        subset1 = table_folium.loc[table_folium.Defect_Class==1]
        classe1 = folium.FeatureGroup(name="<span style='color: black'>Type 1 du défaut : Un seul point-chaud</span>")
        carte.add_child(classe1)
        for i in range(0,len(subset1)):
            html_string = '''<b><u>Identifiant du module :</u></b> '''+str(int(subset1.iloc[i].moduleID))+'''<br>
            <b><u>Nature du défaut :</u></b> Un seul point-chaud <br>
            <b><u>Description du défaut :</u></b> Une cellule est considérablement chauffée par rapport au reste des cellules du module <br>
            <b><u>Causes potentielles de défaillance :</u></b> La cellule est défectueuse, délaminée ou ombrée <br>
            <b><u>Probabilité de l'existence du défaut :</u></b> '''+str(round(subset1.iloc[i].Probability,2))+'''%<br>
            <b><u>Centroide du module défectueux :</u></b> X = '''+subset1.iloc[i].X+''' / Y = '''+subset1.iloc[i].Y + ' (m)'
            folium.Marker(
                location=[float(subset1.iloc[i].Y), float(subset1.iloc[i].X)],
                icon=folium.Icon(color='black'),
                tooltip=html_string,
                popup= folium.Popup(html=str('<h5>Les régions du module PV qui ont poussé le modèle deep learning à classifier le défaut thermique comme tel sont coloriées en rose dans la figure ci-dessous : </h5> <img style="width: 400px; height: 320px;" src="static/Interpretation/')+str(subset1.iloc[i].moduleID)+ str('.png" Alt="does not seem to upload the image">'))
            ).add_to(classe1)

        # Class 2
        subset2 = table_folium.loc[table_folium.Defect_Class==2]
        classe2 = folium.FeatureGroup(name="<span style='color: red'>Type 2 du défaut : Une mosaïque de points chauds</span>")
        carte.add_child(classe2)
        for i in range(0,len(subset2)):
            html_string2 = '''<b><u>Identifiant du module :</u></b> '''+str(int(subset2.iloc[i].moduleID))+'''<br>
            <b><u>Nature du défaut :</u></b> Une mosaïque de points chauds <br>
            <b><u>Description du défaut :</u></b> Plusieurs cellules sont chauffées de manière substantielle à l'intérieur d'un module selon un modèle en mosaïque <br>
            <b><u>Causes potentielles de défaillance :</u></b> Le module est court-circuité <br>
            <b><u>Probabilité de l'existence du défaut :</u></b> '''+str(round(subset2.iloc[i].Probability,2))+'''%<br>
            <b><u>Centroide du module défectueux :</u></b> X = '''+str(subset2.iloc[i].X)+''' / Y = '''+str(subset2.iloc[i].Y) + ' (m)'
            folium.Marker(
                location=[float(subset2.iloc[i].Y), float(subset2.iloc[i].X)],
                icon=folium.Icon(color='red'),
                tooltip=html_string2,
                popup= folium.Popup(html=str('<h5>Les régions du module PV qui ont poussé le modèle deep learning à classifier le défaut thermique comme tel sont coloriées en rose dans la figure ci-dessous : </h5> <img style="width: 400px; height: 320px;" src="static/Interpretation/')+str(subset2.iloc[i].moduleID)+ str('.png" Alt="does not seem to upload the image">'))
            ).add_to(classe2)

        # Class 3
        subset3 = table_folium.loc[table_folium.Defect_Class==3]
        classe3 = folium.FeatureGroup(name="<span style='color: blue'>Type 3 du défaut : Module dont une rangée de cellule est surchauffée</span>")
        carte.add_child(classe3)
        for i in range(0,len(subset3)):
            html_string3 = '''<b><u>Identifiant du module :</u></b> '''+str(int(subset3.iloc[i].moduleID))+'''<br>
            <b><u>Nature du défaut :</u></b> Module dont une rangée de cellule est surchauffée <br>
            <b><u>Description du défaut :</u></b> Une rangée de cellules est plus chaude que les autres régions du module <br>
            <b><u>Causes potentielles de défaillance :</u></b> La rangée de cellules est ouverte ou court-circuitée <br>
            <b><u>Probabilité de l'existence du défaut :</u></b> '''+str(round(subset3.iloc[i].Probability,2))+'''%<br>
            <b><u>Centroide du module défectueux :</u></b> X = '''+str(subset3.iloc[i].X)+''' / Y = '''+str(subset3.iloc[i].Y) + ' (m)'
            folium.Marker(
                location=[float(subset3.iloc[i].Y), float(subset3.iloc[i].X)],
                icon=folium.Icon(color='darkblue'),
                tooltip=html_string3,
                popup= folium.Popup(html=str('<h5>Les régions du module PV qui ont poussé le modèle deep learning à classifier le défaut thermique comme tel sont coloriées en rose dans la figure ci-dessous : </h5> <img style="width: 400px; height: 320px;" src="static/Interpretation/')+str(subset3.iloc[i].moduleID)+ str('.png" Alt="does not seem to upload the image">'))
            ).add_to(classe3)

        # Class 4
        subset4 = table_folium.loc[table_folium.Defect_Class==4]
        classe4 = folium.FeatureGroup(name="<span style='color: green'>Type 4 du défaut : Module surchauffé</span>")
        carte.add_child(classe4)
        for i in range(0,len(subset4)):
            html_string4 = '''<b><u>Identifiant du module :</u></b> '''+str(int(subset4.iloc[i].moduleID))+'''<br>
            <b><u>Nature du défaut :</u></b> Module surchauffé <br>
            <b><u>Description du défaut :</u></b> Le module est plus chaud que les autres modules de l'installation <br>
            <b><u>Causes potentielles de défaillance :</u></b> Le module est en circuit ouvert ou n'est pas connecté au système <br>
            <b><u>Probabilité de l'existence du défaut :</u></b> '''+str(round(subset4.iloc[i].Probability,2))+'''%<br>
            <b><u>Centroide du module défectueux :</u></b> X = '''+str(subset4.iloc[i].X)+''' / Y = '''+str(subset4.iloc[i].Y) + ' (m)'
            folium.Marker(
                location=[float(subset4.iloc[i].Y), float(subset4.iloc[i].X)],
                icon=folium.Icon(color='darkgreen'),
                tooltip=html_string4,
                popup= folium.Popup(html=str('<h5>Les régions du module PV qui ont poussé le modèle deep learning à classifier le défaut thermique comme tel sont coloriées en rose dans la figure ci-dessous : </h5> <img style="width: 400px; height: 320px;" src="static/Interpretation/')+str(subset4.iloc[i].moduleID)+ str('.png" Alt="does not seem to upload the image">'))
            ).add_to(classe4)

        # Class 5
        subset5 = table_folium.loc[table_folium.Defect_Class==5]
        classe5 = folium.FeatureGroup(name="<span style='color: orange'>Type 5 du défaut : Un réchauffement ponctuel</span>")
        carte.add_child(classe5)
        for i in range(0,len(subset5)):
            html_string5 = '''<b><u>Identifiant du module :</u></b> '''+str(int(subset5.iloc[i].moduleID))+'''<br>
            <b><u>Nature du défaut :</u></b> Un réchauffement ponctuel <br>
            <b><u>Description du défaut :</u></b> Une tache ponctuelle présentant un contraste de température légèrement plus élevé <br>
            <b><u>Causes potentielles de défaillance :</u></b> La présence d'un dépôt de poussière local ou d'un déchet d'oiseaux <br>
            <b><u>Probabilité de l'existence du défaut :</u></b> '''+str(round(subset5.iloc[i].Probability,2))+'''%<br>
            <b><u>Centroide du module défectueux :</u></b> X = '''+str(subset5.iloc[i].X)+''' / Y = '''+str(subset5.iloc[i].Y)  + ' (m)'
            folium.Marker(
                location=[float(subset5.iloc[i].Y), float(subset5.iloc[i].X)],
                icon=folium.Icon(color='orange'),
                tooltip=html_string5,
                popup= folium.Popup(html=str('<h5>Les régions du module PV qui ont poussé le modèle deep learning à classifier le défaut thermique comme tel sont coloriées en rose dans la figure ci-dessous : </h5> <img style="width: 400px; height: 320px;" src="static/Interpretation/')+str(subset5.iloc[i].moduleID)+ str('.png" Alt="does not seem to upload the image">'))
            ).add_to(classe5)

        folium.LayerControl().add_to(carte)
        return HttpResponse(carte._repr_html_())
    return render(request , 'AppPages/Client Dashboard/client_geo.html')