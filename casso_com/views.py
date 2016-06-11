from django.shortcuts import HttpResponse, render
from django.http import *
import time

# Create your views here.

def index(request):
	if request.POST:
		username = request.POST['username']
		time.sleep(2)
		result = authenticate(username)
	context = {
		
	}
	return render(request, 'casso_com/example.html', context)

def authenticate(username):
	pass