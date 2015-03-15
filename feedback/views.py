from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from gifts.models import *
from gifts.forms import RecipientForm, AddGiftFormset, SignupForm
from django.contrib.auth import authenticate, login

def feedback(request):
	return render(request, 'feedback.html')