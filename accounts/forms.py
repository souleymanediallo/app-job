from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile, Invite


# https://docs.djangoproject.com/en/3.2/ref/forms/widgets/


class CustomUserForm(UserCreationForm):
    CHOICES = (('is_employer', 'employer'), ('is_employee', 'employee'))
    user_type = forms.CharField(label="Type de compte", widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['user_type'].widget.attrs.update({'class': 'form-check-input'})


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ["created", "description"]

        widgets = {
            "created": forms.DateInput(attrs={'type': 'created'}),
        }


