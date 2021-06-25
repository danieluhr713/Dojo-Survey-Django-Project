from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    context = {
        'name': request.POST['full_name'],
        'location': request.POST['Dojo_location'],
        'languages': request.POST['Dojo_language'],
        'comments': request.POST['optionalComment'],
        'engineer': request.POST['SoftwareEngineer']
    }
    return render(request, 'dojo.html', context)

