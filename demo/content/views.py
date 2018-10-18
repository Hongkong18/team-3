#from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import User
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt 
def loginPageView(request):
    try:
        if request.session['loginAs'] == 'Admin':
            return JsonResponse({'err': 'AlreadyLoginAsAdmin', 'msg': '' })        
        
        if request.session['loginAs'] == 'Donor' or request.session['loginAs'] == 'Volunteer':
            return JsonResponse({'err': 'AlreadyLoginAs' + request.session['loginAs'], 'msg': '' })    
    except KeyError:
        pass    
    return render(request, 'login.html')
    
@csrf_exempt 
def signupPageView(request):   
    return render(request, 'signup.html')
    
    
@csrf_exempt 
def loginSubmitPageView(request):
#    u = request.POST['username']
#    p = request.POST['password']
    #jdata = json.loads(request.body)
    #try:
    #    u = jdata['username']
    #    p = jdata['password']
    #except KeyError:
    #    return JsonResponse({'err': 'malformedJsonData!', 'msg': ''})
    
    u = request.POST.get('username', '')
    p = request.POST.get('password', '')
    
    try:
        user = User.objects.get(username=u)
    except User.MultipleObjectsReturned:
        return JsonResponse({'err': 'duplicateUser', 'msg': ''})
    except User.DoesNotExist:
        return JsonResponse({'err': 'userNotFound', 'msg': ''})
        
        
    if p != user.password:
        return JsonResponse({'err': 'wrongPassword', 'msg': ''})
        
    request.session['username'] = user.username
    
    if user.isAdmin == True:
        request.session['loginAs'] = 'Admin'
        return JsonResponse({'err': '', 'msg': 'loginAsAdmin'})

    request.session['loginAs'] = user.__class__.__name__    
    return JsonResponse({'err': '', 'msg': 'loginAs' + user.__class__.__name__ })    

@csrf_exempt 
def signupSubmitPageView(request):
    #jdata = json.loads(request.body)
    #try:
    #    u = jdata['username']
    #    p = jdata['password']
    #    e = jdata['email']
    #    c = jdata['contact']
    #except KeyError:
    #    return JsonResponse({'err': 'malformedJsonData!', 'msg': ''})
    
    uname = request.POST.get('f1', '')
    pword = request.POST.get('f4', '')
    em = request.POST.get('f2', '')
    cont = request.POST.get('f4', '')
    hourofwork = request.POST.get('f5', '')
    birthdate = request.POST.get('f6', '')
    skills = request.POST.get('f8[]', '')
    comments =  request.POST.get('f3', '')
    
        
    try:
        user = User.objects.get(username=u)
    except User.MultipleObjectsReturned:
        return JsonResponse({'err': 'userAlreadyExist', 'msg': ''})
    except User.DoesNotExist:
        User.objects.create(username=u, password=p, email=e, contact=c)
        return JsonResponse({'err': '', 'msg': 'userAdded'})
    
    return JsonResponse({'err': 'userAlreadyExist', 'msg': ''})

def homePageView(request):
    return render(request, 'home.html')

def adminLandingPageView(request):
	return HttpResponse('adminLandingPageView')
	

def nonadminLandingPageView(request):
	return HttpResponse('nonadminLandingPageView')
