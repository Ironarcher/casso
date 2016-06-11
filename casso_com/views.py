from django.shortcuts import HttpResponse, render
from django.http import *
import time

# Create your views here.

def index(request):
	result = False
	if request.is_ajax():
		if request.POST:
			request_type = request.POST['type']
			username = request.POST['username']
			if request_type == "verify_username":
				result = check_username(username)
				return HttpResponse(result)
			elif request_type == "verify_phone":
				authenticate(username)
				#Use HttpRedirect to success page
	else:
		context = {}
		return render(request, 'casso_com/example.html', context)

#Placeholder function (will be actual authentication by the web server)
def check_username(username):
	if(username == "big_arp"):
		return True
	else:
		return False

#To forward to casso api (to verify with phone)
def authenticate(username):
	pass