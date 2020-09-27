from django.views import View
from django.shortcuts import render
from store.models.product import Product

class Cart(View):
    def get(self,request):
        ids_list=request.session.get('cart').keys()
        if not ids_list:
            return render(request, 'cart.html')
        products = Product.get_productbyid(ids_list)
        return render(request,'cart.html',{'products':products})