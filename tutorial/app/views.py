from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext
import urllib2
from models import Pokemon, Purchase
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request, "index.html", {"pokemons": [pokemon for pokemon in Pokemon.objects.all()]})

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/')
        else:
            print user_form.errors
    else:
        user_form = UserCreationForm()
    return render_to_response('register.html', {'user_form': user_form, 'registered': registered}, context)


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect('/') 


@login_required
def purchase(request):
	if "pokemon" in request.GET:
		pokemon = Pokemon.objects.get(pk=float(request.GET["pokemon"]))
		if "currently_purchasing" in request.session:
			purchase = Purchase.objects.get(pk=request.session["currently_purchasing"])
			purchase.pokemons.add(pokemon)
			return HttpResponseRedirect('/')
		else:
			purchase = Purchase(user=request.user)
			purchase.save()
			request.session["currently_purchasing"] = purchase.id
			purchase.pokemons.add(pokemon)
			return HttpResponseRedirect('/')
	else:
		if "currently_purchasing" in request.session:
			purchase = Purchase.objects.get(pk=request.session["currently_purchasing"])
			return render(request, "purchase.html", { "purchase_pokemons": purchase.pokemons.all() })
		else:
			return render(request, "purchase.html")

def checkout(request):
	pass