from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Resume

def homePage(Request):
    data = Resume.objects.all()
    return render(Request,'index.html',{"data":data})


def dataPage(Request, id):
    try:
        data = Resume.objects.get(id = id)
        return render(Request, 'resumehere.html', {'data': data})
    except Resume.DoesNotExist:
        return HttpResponseRedirect('/')

def addDetailsPage(Request):
    if(Request.method=="POST"):
        u = Resume()
        u.name = Request.POST.get('name')
        u.dob = Request.POST.get('dob')
        u.gender = Request.POST.get('gender')
        u.locality = Request.POST.get('locality')
        u.city = Request.POST.get('city')
        u.state = Request.POST.get('state')
        u.pin = Request.POST.get('pin')
        u.mobile = Request.POST.get('mobile')
        u.email = Request.POST.get('email')
        u.img = Request.POST.get('img')
        u.save()
        return HttpResponseRedirect('/')
    return render(Request,'adddetails.html')