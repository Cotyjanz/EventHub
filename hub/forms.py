from django import forms
from django.contrib.auth.forms import UserCreationForm
from hub.models import EventDetails


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ('title', 'description', 'Location', 'date', 'time', 'Is_public', 'poster_layout','Is_rsvp',)
        widgets={
'description': forms.TextInput(attrs={'style': 'width: 100%;', }),
'date': forms.SelectDateWidget(attrs={'placeholder': 'YYYY-MM-DD', 'style': 'width: 10%; text-align: center;', }),
'time': forms.TimeInput(attrs={'placeholder': 'HH:MM:SS', 'style': 'width: 30%; text-align: center;', }),
'Is_public': forms.CheckboxInput(attrs={'style':'width:20px;height:20px; margin-left: 5%; margin-top: 2%;'}),
}

class EventRSVPForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ('Is_rsvp',)
        widgets={
'Is_rsvp': forms.NumberInput(attrs={'placeholder': 'No. of Guests','style':'border-radius: 10px;font-size: 11px ;width: 80px;height:35px; '}),
}
        


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name",)


class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
