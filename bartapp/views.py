from django.shortcuts import render
from django.views import generic
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Offer, OfferImage

def index(request):
    return render(request, "bartapp/index.html", {})
    

def offer_detail(request, pk, category, offer):
    offer = get_object_or_404(Offer, pk=pk, category=category, slug=offer)
    # offer_images = offer.images.all()
    return render(request, "bartapp/offer_detail.html", {"offer": offer})

# 
# Creating a new user and adding him/her to a database
def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, "bartapp/register_done.html", {'new_user': new_user})

    else:
        user_form = RegisterForm()
    return render (request, "bartapp/register.html", {'user_form': user_form})

