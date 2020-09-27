from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer

class SignupView(View):
    def get(self,request):
        if request.method == 'GET':
            return render(request, 'signup.html')

    def post(self,request):
        postdata = request.POST
        customer = Customer(first_name=postdata.get('firstname'), last_name=postdata.get('lastname'),
                            phone=postdata.get('phone'), email=postdata.get('email'), password=postdata.get('password'))
        value = {
            'firstname': customer.first_name,
            'lastname': customer.last_name,
            'phone': customer.phone,
            'email': customer.email}
        error_msg = self.validatefield(customer)
        if not error_msg:
            if postdata.get('password') == postdata.get('cpassword'):
                customer.password = make_password(customer.password)
                customer.register()
                return redirect('homepage')
            error_msg = 'Make sure password and confirm password are same...!!'
        data = {'value': value, 'msg': error_msg}
        return render(request, 'signup.html', data)

    def validatefield(self,customer):
        error_msg = None
        if not len(customer.first_name) > 4:
            error_msg = 'please enter valid firstname'
        elif not len(customer.last_name) > 4:
            error_msg = 'please enter valid lastname'
        elif len(customer.phone) != 10 and customer.phone in range(7700000000, 9999999999):
            error_msg = 'Please enter 10 digit valid mobile number'
        elif not len(customer.password) > 6:
            error_msg = 'Password length should be greater than 6..!!'
        elif customer.isExist():
            error_msg = 'Email ID is Already Registered..!!'
        return error_msg

