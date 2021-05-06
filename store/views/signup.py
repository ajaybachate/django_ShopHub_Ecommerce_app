from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password=make_password(customer.password)
            customer.save()
            return redirect('index')
        else:
            return render(request, 'signup.html', {'error': error_message})

    def validateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "first name required"
        elif len(customer.first_name) < 4:
            error_message = "first name too small"

        elif not customer.last_name:
            error_message = "last name required"
        elif len(customer.last_name) < 4:
            error_message = "last name too small"

        elif not customer.email:
            error_message = "email required"
        elif not ("@gmail.com" in customer.email):
            error_message = "email should contain @gmail.com"

        elif not customer.phone:
            error_message = "phone number required"
        elif len(customer.phone) < 10:
            error_message = " invalid phone number"

        elif not customer.password:
            error_message = "password required"
        elif len(customer.password) < 4:
            error_message = "password too small"
        elif customer.isExists():
            error_message = "email already taken"
        return error_message













