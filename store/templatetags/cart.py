from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    # print(cart)
    for id in cart:
        if int(id)==product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in cart:
        if int(id)==product.id:
            return cart.get(id)
    return False


@register.filter(name='product_price')
def product_price(product,cart):
    return product.price* cart_quantity(product,cart)

@register.filter(name='total_prod_price')
def total_prod_price(product,cart):
    sum=0
    for p in product:
        sum+=product_price(p,cart)
    return sum