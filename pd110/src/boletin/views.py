from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado


# Create your views here.
def inicio(request):
    titulo = "Bienvenido"
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
    titulo = "Contacto"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.iteritems():
            #print(key, value)
        #for key in form.cleaned_data:
         #   print(key)
         #  print(form.cleaned_data.get(key))
        from_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "Form de Contacto"
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, from_email)
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]

        send_mail(asunto, email_mensaje, email_from, email_to, fail_silently=False)
        print(form_nombre, form_mensaje, from_email)
    context = {
        "form": form,
        "titulo": titulo,
    }
    return render(request, "forms.html", context)




