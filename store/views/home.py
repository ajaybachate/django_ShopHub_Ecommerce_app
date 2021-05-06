from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1

        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('index')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_product_by_categoryid(categoryID)
        else:
            products = Product.get_all_product()

        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)
