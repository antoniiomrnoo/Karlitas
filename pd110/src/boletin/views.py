from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado


# Create your views here.
def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "temp_titulo": titulo,
        "el_form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nombre:
            instance.nombre = "PERSONA"
            instance.save()

        context = {
            "titulo": "Gracias %s!" %instance.nombre
        }

        if not instance.nombre:
            context = {
                "titulo": "Gracias %s!" %instance.email
            }


        print(instance)
        print(instance.timestamp)
        #form_data = form.cleaned_data
        #abc = form_data.get("email")
        #abc2 = form_data.get("nombre")
        #obj = Registrado.objects.create(email=abc, nombre=abc2)


    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)




