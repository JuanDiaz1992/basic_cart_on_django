from django.shortcuts import render
from .models import Users

# Create your views here.
def viewsUsers(request):
    users = Users.objects.all()
    print(users)
    if users:
        return render(request, "users/users.html", {'users':users})
    else:
        return render(request, "users/users.html")

from django.shortcuts import render
from .models import Users

def createNewUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = request.POST.get('user')
        password = request.POST.get('password')
        print(name, email, user, password)

        # Verificar si el usuario ya existe
        if Users.objects.filter(user=user).exists():
            result = "No se pudo realizar el registro. El usuario ya existe."
            return render(request, "users/resultCreate.html", {'result': result})

        try:
            # Crear un nuevo usuario
            new_user = Users(name=name, email=email, user=user, password=password)
            new_user.save()
            result = f"Usuario {user} registrado correctamente."
            return render(request, "users/resultCreate.html", {'result': result})

        except:
            result = f"No se pudo realizar el registro"
            return render(request, "users/resultCreate.html", {'result': result})

    else:
        return render(request, 'users/createNewUser.html')
 