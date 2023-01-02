from logging import PlaceHolder
from django import forms
# authentication/forms.py


class login(forms.Form):
    email = forms.CharField(label='Email :', widget=forms.TextInput(attrs={'placeholder': 'Enter your registered email'}), max_length=100)
    password = forms.CharField(label='Password :', max_length=20,widget=forms.PasswordInput)
    


class signup(forms.Form):
    first_name = forms.CharField(max_length=50) 
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}), max_length=100)
    password = forms.CharField(label='Password',  max_length=20, widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(signup, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password1")

        if password != confirm_password:
            raise forms.ValidationError(
                "passwords do not match"
            )

class payment(forms.Form):
    name_on_card = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}), max_length=100)
    card_number = forms.IntegerField(label='Credit Card Number', widget=forms.TextInput(attrs={'placeholder': 'xxxx-xxxx-xxxx'}), max_length=100)
    cvv = forms.IntegerField()

class moviepage(forms.Form):
    quantity= forms.IntegerField()
    



