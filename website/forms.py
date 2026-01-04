from django import forms


from django.forms import ModelForm
from .models import ContactMessage

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "email", "subject", "message"]
