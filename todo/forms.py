from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Todo, Priority, Status



#create a view
# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', "username", 'email', 'password']
#         # fields = "__all__"


#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#         }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    priority = forms.ModelChoiceField(label='Priority', queryset=Priority.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ModelChoiceField(label='Status', queryset=Status.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    short_description = forms.CharField(label='Short Description', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    class Meta:
        model = Todo
        fields = ['title', 'priority', 'status', 'short_description']
