from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
	return 	render(request, 'generator/home.html')


def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

	if request.GET.get('specialchar'):
		characters.extend(list('£$%^&*_+=-@'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	length = int(request.GET.get('length'))

	thepassword = ""
	
	for x in range(length):
		thepassword += random.choice(characters)

	return 	render(request, 'generator/password.html',{'password' : thepassword})


def about(request):
	return render(request, 'generator/about.html')