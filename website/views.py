from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        send_mail(
            subject=f"New Contact: {form.cleaned_data['name']}",
            message=form.cleaned_data["message"],
            from_email=form.cleaned_data["email"],
            recipient_list=["contact@novaintel.ai"],
        )
        success = True
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "success": success})
