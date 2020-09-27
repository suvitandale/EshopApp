from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer
from django.utils.decorators import method_decorator


class OrderView(View):

    def get(self,request):
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        print(order)
        return render(request,'orders.html',{'orders':order})


