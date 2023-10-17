from django.shortcuts import render
import requests

def obtener_productos():
    fetch = requests.get("https://fakestoreapi.com/products")
    products = fetch.json()
    return products


def viewProducts(request):
    products = obtener_productos()
    return render(request, 'products/viewProducts.html',{'products':products})

def agregar_producto(request, id):
    products = obtener_productos()
    car = request.session.get('car', [])
    for i in car:
        if i['id'] == id:
            i['cant'] += 1
            break
    else:
        car.append({'id': id, 'cant': 1})
    request.session['car'] = car
    return render(request, 'products/viewProducts.html',{'products':products})

def viewCar(request):
        car = request.session['car']
        carForView = []
        if car == "":
            car = []
        else:
            products = obtener_productos()
            for e in car: 
                print(e)
                for i in products:
                    print(i)
                    if e["id"] == i["id"]:
                        i["cant"] = e["cant"]
                        carForView.append(i)
             
        return render(request, 'products/cart.html',{'carForView':carForView})

def deleteCart(request):
    request.session['car'] = []
    carForView = []
    return render(request, 'products/cart.html',{'carForView':carForView})

