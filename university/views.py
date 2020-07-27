from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView,DetailView,View



from django.views.generic.list import ListView

class HomeView(ListView):
	template_name = 'university/homepage.html'
	queryset = Profile.objects.all()
	context_object_name = 'profiles'

def index(request):
    profile = Profile.objects.all()
    return redirect (request, 'university/homepage.html', {'profile':profile})

















