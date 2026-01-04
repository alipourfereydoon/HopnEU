from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    return render(request, "home.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")




# def contact(request):
#     success = False
#     form = ContactForm(request.POST or None)

#     if request.method == "POST" and form.is_valid():
#         # Save message to database ONLY
#         ContactMessage.objects.create(
#             first_name=form.cleaned_data["first_name"],
#             last_name=form.cleaned_data["last_name"],
#             email=form.cleaned_data["email"],
#             subject=form.cleaned_data["subject"],
#             message=form.cleaned_data["message"],
#         )

#         success = True
#         form = ContactForm()  # Reset form after save

#     return render(request, "contact.html", {
#         "form": form,
#         "success": success
#     })


def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        success = True
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success
    })
