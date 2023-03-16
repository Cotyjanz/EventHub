from django import forms
from django.contrib.auth.forms import UserCreationForm
from hub.models import EventDetails


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ('title', 'description', 'Location', 'date', 'time', 'Is_public','poster_layout')
        widgets={
'description': forms.TextInput(attrs={'style': 'width: 100%;', }),
'date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'style': 'width: 40%;', }),
'time': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'style': 'width: 40%;', }),
        }

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name",)


class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
