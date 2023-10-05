import random
import stripe
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from products.models import Product
from .models import Purchase

from cfehome.env import config

STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default=None)
stripe.api_key = STRIPE_SECRET_KEY

BASE_ENDPOINT= config("BASE_ENDPOINT", default="http://127.0.0.1:8000") #this is for development

def purchase_start_view(request):
    if not request.method == "POST":
        return HttpResponseBadRequest()
    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    handle = request.POST.get("handle")
    obj = Product.objects.get(handle=handle)
    stripe_price_id = obj.stripe_price_id # stripe price id
    if stripe_price_id is None: # if there is no stripe price id, then we can't create a checkout session; something wrong
        return HttpResponseBadRequest()
    purchase = Purchase.objects.create(user=request.user, product=obj)
    request.session['purchase_id'] = purchase.id # store purchase id in session
    success_path = reverse("purchases:success") # reverse is a django function that will return the url
    if not success_path.startswith("/"): # if success path doesn't start with a slash, then add it
        success_path = f"/{success_path}"
    cancel_path = reverse("purchases:stopped")
    success_url = f"{BASE_ENDPOINT}{success_path}"
    cancel_url = f"{BASE_ENDPOINT}{cancel_path}"
    print(success_url, cancel_url)
    checkout_session = stripe.checkout.Session.create(
        line_items = [
            {
                "price": stripe_price_id,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url
    )
    purchase.stripe_checkout_session_id = checkout_session.id
    purchase.save() #save purchase to have reference to checkout session
    return HttpResponseRedirect(checkout_session.url)

def purchase_success_view(request):
    purchase_id = request.session.get("purchase_id") #once purchase id is stored in session, we can get it
    if purchase_id:
        purchase = Purchase.objects.get(id=purchase_id) #grabs id and update purchase as completed
        purchase.completed = True
        purchase.save()
        del request.session['purchase_id']
        return HttpResponseRedirect(purchase.product.get_absolute_url())
    return HttpResponse(f"Finished {purchase_id}")


def purchase_stopped_view(request):
    purchase_id = request.session.get("purchase_id")
    if purchase_id:
        purchase = Purchase.objects.get(id=purchase_id)
        product = purchase.product
        del request.session['purchase_id']
        return HttpResponseRedirect(product.get_absolute_url())
    return HttpResponse("Stopped")
