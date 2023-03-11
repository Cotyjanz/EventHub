from django.contrib.auth.forms import UserCreationForm


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = EventDetail
        fields = ('title', 'description', 'Location', 'date', 'time', 'Is_public',)
        exclude = ('u_id',)


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name",)


class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
