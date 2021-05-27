from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import Question


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label = 'Имя пользователя', help_text='максимум 150 символов')
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label = 'пароль')

class AddTovar(ModelForm):
    class Meta:
        model = Question
        fields = ['id_tovara','id_postav','name','kol_vo','cena', 'image']

        widgets = {
            "id_tovara": forms.TextInput(attrs={
                'class':'form-control ms-5 mt-2',
                'placeholder': 'Id товара'
            }),
            "id_postav": forms.TextInput(attrs={
                'class': 'form-control ms-5 mt-2',
                'placeholder': 'Id поставщика'
            }),
            "name": forms.TextInput(attrs={
                'class': 'form-control ms-5 mt-2',
                'placeholder': 'имя'
            }),
            "kol_vo": forms.TextInput(attrs={
                'class': 'form-control ms-5 mt-2',
                'placeholder': 'количество'
            }),
            "cena": forms.TextInput(attrs={
                'class': 'form-control ms-5 mt-2',
                'placeholder': 'цена'
            }),
            "image": forms.FileInput,

        }





