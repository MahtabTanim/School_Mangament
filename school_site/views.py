from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = generateContext(request)
    return render(request, 'homepage.html', context)

def about_page(request):
    context = generateContext(request)
    return render(request, 'about.html',context)
def contact_page(request):
    context = generateContext(request)
    return render(request, 'contact.html',context)

def generateContext(request) -> dict:
    context =  {
        "school_name": "DevSkill",
        "user_name": "Alice",
        "subjects": ['Bengali', 'Science', 'English'],
        "registration_open": True
    }
    if request.method =='POST' and request.POST.get('form_type') == 'form1': 
        print('form1 is selected')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email =  request.POST.get('email')
        context.update(
            {
                'fname': fname,
                'lname': lname,
                'user_name': f"{fname} {lname}",
                'email': email
            }
        )
    
    return context
