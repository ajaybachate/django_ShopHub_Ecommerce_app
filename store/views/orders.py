from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order


class OrdersView(View):

    def get(self, request):
        customer = request.session.get('customer')
        #print(customer)
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html',{'orders':orders})





