from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    request.session['name'] = request.POST['full_name']
    request.session['location'] = request.POST['Dojo_location']
    request.session['languages'] = request.POST['Dojo_language']
    request.session['comments'] = request.POST['optionalComment']
    request.session['engineer'] = request.POST['SoftwareEngineer']
    return redirect('/dojo_dash')

def dashboard(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'languages': request.session['languages'],
        'comments': request.session['comments'],
        'engineer': request.session['engineer']
    }
    return render(request, 'dojo.html', context)

