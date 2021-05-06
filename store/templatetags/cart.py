from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_item_count')
def item_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * item_quantity(product, cart)

@register.filter(name='total')
def total(products, cart):
    sum=0
    for p in products:
        sum+= price_total(p, cart)
    return sum

@register.filter(name='multiply')
def multiply(num1, num2):
    return num1*num2
