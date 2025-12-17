from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']



class CheckoutForm(forms.Form):
    street_address=forms.CharField(widget=forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'1234 Main St'
        }))
    

    apartment_address=forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apartment or suite'
    }))


    country=CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))

    zip=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
