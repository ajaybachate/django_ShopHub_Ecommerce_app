from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order


class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products =Product.get_products_by_id(list(cart.keys()))
        #print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id = customer),
                          product=product,
                          address=address,
                          phone=phone,
                          price=product.price,
                          quantity=cart.get(str(product.id)))
            order.save()
            print(order.placeOrder())
            request.session['cart']={}


        return redirect('cart')




