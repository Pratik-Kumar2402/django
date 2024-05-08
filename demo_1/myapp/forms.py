from django import forms

class InputForm1(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
from .models import Customers
class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
