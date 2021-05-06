from django.shortcuts import render,redirect,HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


class Cart(View):

    def get(self, request):
        if request.session.get('cart'):
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            return render(request, 'cart.html', {'products' : products})
        else:
            return HttpResponse('<h1>Your cart is empty...</h1>')


