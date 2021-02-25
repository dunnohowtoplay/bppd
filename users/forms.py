from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Enter Your Password',
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Confirm Your Password',
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets =  {
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Enter Your Username',
                }   
            ),

            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'youremail@gmail.com',
                }
            ),
        }