def custom_context(request):
    cart = request.session.get('car', [])
    cant = 0
    for i in cart:
        cant += i["cant"]
    return {'cart_quantity': cant}