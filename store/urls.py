from django.urls import path
from store.views.home import Index
from store.views.login import Login, logout
from store.views.signup import Signup
from store.views.cart import Cart
from store.views.checkout import CheckOut
from store.views.orders import OrdersView
from store.middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrdersView.as_view()), name='checkout'),

]
