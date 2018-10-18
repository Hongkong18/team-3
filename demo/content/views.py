#from django.http import HttpResponse
from django.http import JsonResponse
from .models import User
import json

# Create your views here.

def loginPageView(request):
    try:
        if request.session['loginAs'] == 'Admin':
            return JsonResponse({'err': 'AlreadyLoginAsAdmin', 'msg': '' })        
        
        if request.session['loginAs'] == 'Donor' or request.session['loginAs'] == 'Volunteer':
            return JsonResponse({'err': 'AlreadyLoginAs' + request.session['loginAs'], 'msg': '' })    
    except KeyError:
        pass    
    return JsonResponse({'err': '', 'msg': 'ableToLogin' })
    
    
    
def loginSubmitPageView(request):
#    u = request.POST['username']
#    p = request.POST['password']
    jdata = json.loads(request.body)
    try:
        u = jdata['username']
        p = jdata['password']
    except KeyError:
        return JsonResponse({'err': 'malformedJsonData!', 'msg': ''})

    try:
        user = Users.objects.get(username=u)
    except MultipleObjectsReturned:
        return JsonResponse({'err': 'duplicateUser', 'msg': ''})
    except DoesNotExist:
        return JsonResponse({'err': 'userNotFound', 'msg': ''})
        
        
    if p != user.password:
        return JsonResponse({'err': 'wrongPassword', 'msg': ''})
        
    request.session['username'] = user.username
    
    if user.isAdmin == True:
        request.session['loginAs'] = 'Admin'
        return JsonResponse({'err': '', 'msg': 'loginAsAdmin'})

    request.session['loginAs'] = user.__class__.__name__    
    return JsonResponse({'err': '', 'msg': 'loginAs' + user.__class__.__name__ })    

def signupSubmitPageView(request):
    jdata = json.loads(request.body)
    try:
        u = jdata['username']
        p = jdata['password']
        e = jdata['email']
        c = jdata['contact']
    except KeyError:
        return JsonResponse({'err': 'malformedJsonData!', 'msg': ''})
        
    try:
        user = Users.objects.get(username=u)
    except MultipleObjectsReturned:
        return JsonResponse({'err': 'userAlreadyExist', 'msg': ''})
    except DoesNotExist:
        Users.objects.create(username=u, password=p, email=e, contact=c)
        return JsonResponse({'err': '', 'msg': 'userAdded'})
    
    return JsonResponse({'err': 'userAlreadyExist', 'msg': ''})

def adminLandingPageView(request):
	return HttpResponse('adminLandingPageView')
	

def nonadminLandingPageView(request):
	return HttpResponse('nonadminLandingPageView')
