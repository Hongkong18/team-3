from django.http import HttpResponse

# Create your views here.

def monkeyPageView(request):
	return HttpResponse('Yes, I am a code monkey!')