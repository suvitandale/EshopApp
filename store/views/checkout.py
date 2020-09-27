from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class Checkout(View):
    def post(self,request):
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        print(cart)
        products = Product.get_productbyid(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id = customer),product = product,price = product.price,
                          address=address,phone=phone, quantity = cart.get(str(product.id)))
            order.placeorder()
        request.session['cart']={}

        # print(address,phone,customer,products)
        return redirect('cart')