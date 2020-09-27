from django.contrib import admin
from django.urls import path
from .views import login,signup,home,cart,checkout,orders
from store.middlewares.auth import auth_middleware



urlpatterns = [
    path('',home.Index.as_view(),name='homepage'),
    path('signup',signup.SignupView.as_view(),name='signup'),
    path('login',login.LoginView.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('check-out', checkout.Checkout.as_view(), name='checkout'),
    path('orders',auth_middleware(orders.OrderView.as_view()), name='order'),

]
