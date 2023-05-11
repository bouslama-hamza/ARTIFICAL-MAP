import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)
from datetime import datetime


## Attention match version recente , utiliser if if older version
def choix_user_instanttime(df,timeframe, aggregate, grandeur) :

    match timeframe:
        case 'Années':
            match aggregate:
                case 'Moyenne' :
                    if grandeur =='All':
                        return df.groupby(df.index.year).mean()
                    else :
                        return df.groupby(df.index.year).mean()[grandeur]
                case 'Minimum':
                    if grandeur =='All':
                        return df.groupby(df.index.year).min()
                    else :
                        return df.groupby(df.index.year).min()[grandeur]
                case 'Maximum':
                    if grandeur =='All':
                        return df.groupby(df.index.year).max()
                    else :
                        return df.groupby(df.index.year).max()[grandeur]
                case 'Total':
                    if grandeur =='All':
                        return df.groupby(df.index.year).sum()
                    else :
                        return df.groupby(df.index.year).sum()[grandeur]
        case 'Mois':
            match aggregate:
                case 'Moyenne' :
                    if grandeur =='All':

                        temp = df.groupby(df.index.month).mean()
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                    else :
                        temp = df.groupby(df.index.month).mean()[grandeur]
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                case 'Minimum':
                    if grandeur =='All':

                        temp = df.groupby(df.index.month).min()
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                    else :
                        temp = df.groupby(df.index.month).min()[grandeur]
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp
                case 'Maximum':
                    if grandeur =='All':
                        temp = df.groupby(df.index.month).max()
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                    else :
                        temp = df.groupby(df.index.month).max()[grandeur]
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                case 'Total':
                    if grandeur =='All':
                        temp = df.groupby(df.index.month).sum()
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

                    else :
                        temp = df.groupby(df.index.month).sum()[grandeur]
                        temp['Mois'] = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
                        temp.set_index('Mois',inplace=True)
                        return temp

        case 'Semaines':
            match aggregate:
                case 'Moyenne' :
                    if grandeur =='All':
                        return df.groupby(df.index.isocalendar().week).mean()
                    else :
                        return df.groupby(df.index.isocalendar().week).mean()[grandeur]
                case 'Minimum':
                    if grandeur =='All':
                        return df.groupby(df.index.isocalendar().week).min()
                    else :
                        return df.groupby(df.index.isocalendar().week).min()[grandeur]
                case 'Maximum':
                    if grandeur =='All':
                        return df.groupby(df.index.isocalendar().week).max()
                    else :
                        return df.groupby(df.index.isocalendar().week).max()[grandeur]
                case 'Total':
                    if grandeur =='All':
                        return df.groupby(df.index.isocalendar().week).sum()
                    else :
                        return df.groupby(df.index.isocalendar().week).sum()[grandeur]
        case 'Jours':
            match aggregate:
                case 'Moyenne' :
                    if grandeur =='All':
                        return df.groupby(df.index.day).mean()
                    else :
                        return df.groupby(df.index.day).mean()[grandeur]
                case 'Minimum':
                    if grandeur =='All':
                        return df.groupby(df.index.day).min()
                    else :
                        return df.groupby(df.index.day).min()[grandeur]
                case 'Maximum':
                    if grandeur =='All':
                        return df.groupby(df.index.day).max()
                    else :
                        return df.groupby(df.index.day).max()[grandeur]
                case 'Total':
                    if grandeur =='All':
                        return df.groupby(df.index.day).sum()
                    else :
                        return df.groupby(df.index.day).sum()[grandeur]

        case 'JoursDeLaSemaine':
            match aggregate:
                case 'Moyenne' :
                    if grandeur =='All':
                        temp = df.groupby(df.index.dayofweek).mean()
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                    else :
                        temp = df.groupby(df.index.dayofweek).mean()[grandeur]
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                case 'Minimum':
                    if grandeur =='All':
                        temp = df.groupby(df.index.dayofweek).min()
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                    else :
                        temp = df.groupby(df.index.dayofweek).min()[grandeur]
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                case 'Maximum':
                    if grandeur =='All':
                        temp = df.groupby(df.index.dayofweek).max()
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                    else :
                        temp = df.groupby(df.index.dayofweek).max()[grandeur]
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp
                case 'Total':
                    if grandeur =='All':
                        temp = df.groupby(df.index.dayofweek).sum()
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp

                    else :
                        temp = df.groupby(df.index.dayofweek).sum()[grandeur]
                        temp['Jour'] = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
                        temp.set_index('Jour',inplace=True)
                        return temp

## Dates, il va afficher le cumul jusqu'a cette valeur ( la valeur ecrite est la derniere instant de la periode )
def choix_user_periodrange(df,start_day,end_date, frequency,timeframe, aggregate, grandeur) :

    df['Dates'] = df.index
    match aggregate:
        case 'Moyenne' :
            if grandeur =='All':
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).mean().loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


            else :
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).mean()[grandeur].loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    grandeur = [x[0] for x in grandeur ]
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


        case 'Minimum':
            if grandeur =='All':
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).min().loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


            else :
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).min()[grandeur].loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    grandeur = [x[0] for x in grandeur ]
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


        case 'Maximum':
            if grandeur =='All':
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).max().loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


            else :
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).max()[grandeur].loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    grandeur = [x[0] for x in grandeur ]
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


        case 'Total':
            if grandeur =='All':
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).sum().loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


            else :
                temp = df.groupby(pd.Grouper(key=('Dates'),freq=frequency)).sum()[grandeur].loc[start_day:end_date]
                temp2 = temp.copy()
                temp2.index = temp2.index.date
                if timeframe == None :
                    return temp2
                else :
                    grandeur = [x[0] for x in grandeur ]
                    return choix_user_instanttime(temp,timeframe, aggregate, grandeur)


def frequency_mapper(frequence):
    if 'D' in frequence :
        return frequence[:-1] + ' jour(s)'
    if 'M' in frequence :
        return  frequence[:-1] + ' mois'
    if 'W' in frequence :
        return frequence[:-1] + ' semaine(s)'
    if 'Y' in frequence :
        return frequence[:-1] + ' année(s)'


def draw_adaptative_graphs_period(df,start_day,end_date, frequency,timeframe, aggregate, grandeur,choix_graphe) :
    if timeframe == None :
        if aggregate=="Moyenne" :

            if choix_graphe == "bar" :
                df.plot.bar(subplots=False, figsize=(13,8))


            if choix_graphe == "line" :
                df.plot.line(subplots=False, figsize=(8,6))


            plt.legend()
            plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
            if len(grandeur) ==1 :
                plt.ylabel( f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}' )
                plt.title(f'La moyenne de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} en {grandeur[0][1]}')
            else :
                plt.ylabel("Les grandeurs enregistrées")
                plt.title(f'Les moyennes des grandeurs enregistrées du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)}')
            plt.show()


        elif aggregate in ["Maximum","Minimum"] :
            df[("Dates","Dates")] = df.index
            if len(grandeur) ==1 :

                plt.stem(df[("Dates","Dates")], df[grandeur[0]], label=f'{grandeur[0][0]} en {grandeur[0][1]}')
                plt.legend()
                plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
                plt.ylabel( f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}' )
                plt.title(f'Le {aggregate.lower()} de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} en {grandeur[0][1]}')
                plt.show()

            else :
                if grandeur != "All" :
                    pass
                else :
                    varia = df.columns.values.tolist()[:-1]
                    grandeur= [a for a in varia]
                for i in range(0,len(grandeur)) :
                    plt.stem(df[("Dates","Dates")], df[grandeur[i]], label=f'{grandeur[i][0]} en {grandeur[i][1]}')
                    plt.legend()
                    plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} (en Wh)")
                    plt.ylabel(f'{grandeur[i][0]} '+'en '+ f'{grandeur[i][1]}' )
                    plt.title(f'Le {aggregate.lower()} de "{grandeur[i][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} en {grandeur[i][1]}')
                    plt.show()


        else :
            if choix_graphe == "pie" :
                if len(grandeur) ==1 :
                    df.plot.pie(y=f'{grandeur[0][0]}', figsize=(8,6), title=f'Le total de "{grandeur[0][0]}" en {grandeur[0][1]} du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} ', autopct='%1.1f%%')

                    plt.legend()
                    plt.show()


                else :
                    if grandeur != "All" :
                        pass
                    else :
                        grandeur = [x for x in df.columns.values.tolist()]
                    for i in range(0,len(grandeur)) :
                        df.plot.pie(y=f'{grandeur[i][0]}', figsize=(8,6), title=f'Le total de "{grandeur[i][0]}" en {grandeur[i][1]} du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)}', autopct='%1.1f%%')

                        plt.legend()
                    plt.show()


            if choix_graphe == "bar" :
                df.plot.bar(subplots=False, figsize=(8,6))


            if choix_graphe == "line" :
                df.plot.line(subplots=False, figsize=(8,6))


            if choix_graphe in ['bar','line'] :

                plt.legend()
                plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
                if len(grandeur) ==1 :
                    f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}'
                    plt.ylabel(f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}')
                    plt.title(f'Le total de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} en {grandeur[0][1]}')
                else :
                    plt.ylabel("Les grandeurs enregistrées (en Wh)")
                    plt.title(f'Les totaux des grandeurs enregistrées du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} ')
                plt.show()
    else :
        if aggregate=="Moyenne" :

            if choix_graphe == "bar" :
                df.plot.bar(subplots=False, figsize=(13,8))


            if choix_graphe == "line" :
                df.plot.line(subplots=False, figsize=(8,6))


            plt.legend()
            plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
            if len(grandeur) ==1 :
                plt.ylabel( f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}' )
                plt.title(f'La moyenne de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} et groupée par {timeframe} en {grandeur[0][1]}')
            else :
                plt.ylabel("Les grandeurs enregistrées")
                plt.title(f'Les moyennes des grandeurs enregistrées du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupées par {timeframe}')
            plt.show()


        elif aggregate in ["Maximum","Minimum"] :
            df[("Dates","Dates")] = df.index
            if len(grandeur) ==1 :

                plt.stem(df[("Dates","Dates")], df[grandeur[0]], label=f'{grandeur[0][0]} en {grandeur[0][1]}')
                plt.legend()
                plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
                plt.ylabel( f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}' )
                plt.title(f'Le {aggregate.lower()} de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupé par {timeframe} en {grandeur[0][1]}')
                plt.show()

            else :
                if grandeur != "All" :
                    pass
                else :
                    varia = df.columns.values.tolist()[:-1]
                    grandeur= [a for a in varia]
                for i in range(0,len(grandeur)) :
                    plt.stem(df[("Dates","Dates")], df[grandeur[i]], label=f'{grandeur[i][0]} en {grandeur[i][1]}')
                    plt.legend()
                    plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} (en Wh)")
                    plt.ylabel(f'{grandeur[i][0]} '+'en '+ f'{grandeur[i][1]}' )
                    plt.title(f'Le {aggregate.lower()} de "{grandeur[i][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupé par {timeframe} en {grandeur[i][1]}')
                    plt.show()


        else :
            if choix_graphe == "pie" :
                if len(grandeur) ==1 :
                    df.plot.pie(y=f'{grandeur[0][0]}', figsize=(8,6), title=f'Le total de "{grandeur[0][0]}" en {grandeur[0][1]} du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupé par {timeframe}', autopct='%1.1f%%')

                    plt.legend()
                    plt.show()


                else :
                    if grandeur != "All" :
                        pass
                    else :
                        grandeur = [x for x in df.columns.values.tolist()]
                    for i in range(0,len(grandeur)) :
                        df.plot.pie(y=f'{grandeur[i][0]}', figsize=(8,6), title=f'Le total de "{grandeur[i][0]}" en {grandeur[i][1]} du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupé par {timeframe}', autopct='%1.1f%%')

                        plt.legend()
                    plt.show()


            if choix_graphe == "bar" :
                df.plot.bar(subplots=False, figsize=(8,6))


            if choix_graphe == "line" :
                df.plot.line(subplots=False, figsize=(8,6))


            if choix_graphe in ['bar','line'] :

                plt.legend()
                plt.xlabel(f"du {datetime.strptime(start_day,'%Y-%m-%d').strftime('%d-%m-%Y')} à {datetime.strptime(end_date,'%Y-%m-%d').strftime('%d-%m-%Y')} chaque {frequency_mapper(frequency)} ")
                if len(grandeur) ==1 :
                    f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}'
                    plt.ylabel(f'{grandeur[0][0]} '+'en '+ f'{grandeur[0][1]}')
                    plt.title(f'Le total de "{grandeur[0][0]}" du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupé par {timeframe} en {grandeur[0][1]}')
                else :
                    plt.ylabel("Les grandeurs enregistrées (en Wh)")
                    plt.title(f'Les totaux des grandeurs enregistrées du {datetime.strptime(start_day,"%Y-%m-%d").strftime("%d-%m-%Y")} à {datetime.strptime(end_date,"%Y-%m-%d").strftime("%d-%m-%Y")} chaque {frequency_mapper(frequency)} groupés par {timeframe} ')
                plt.show()
























