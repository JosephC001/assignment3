from django import forms
from .models import Contact  # Make sure to import your Contact model

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class UpdateContactForm(forms.ModelForm):
    contact_id = forms.CharField(max_length=20) #new
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession', 'telephone', 'email']

class DeleteContactForm(forms.Form):
    contact_id = forms.CharField(max_length=20)

class ReadContactForm(forms.Form):
    contact_id = forms.CharField(max_length=20)
    
    
#class RequestIdForm(forms.Form):
 #   contact_id = forms.CharField(max_length=20)

