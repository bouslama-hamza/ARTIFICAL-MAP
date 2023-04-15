from django.shortcuts import render

# Create your views here.
def client_home(request):
    return render(request, 'Client Home Page/client_home.html')

def client_contact(request):
    return render(request, 'Client Contact/client_contact.html')

def client_guid(request):
    return render(request, 'Client Guid/client_guid.html')

def client_map(request):
    return render(request, 'Client Map/client_map.html')