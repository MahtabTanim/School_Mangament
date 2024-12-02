from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = generateContext(request)
    if request.method =='POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        context.update(
            {
                'user_name': f"{first_name} {last_name}",
                'email': email
            }
        )
    return render(request, 'homepage.html', context)

def about_page(request):
    context = generateContext(request)
    return render(request, 'about.html',context)
def contact_page(request):
    context = generateContext(request)
    return render(request, 'contact.html',context)
def generateContext(request):
    return {
        "school_name": "DevSkill",
        "user_name": "Alice",
        "subjects": ['Bengali', 'Science', 'English'],
        "registration_open": True
    }