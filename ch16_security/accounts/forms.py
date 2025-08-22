# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")


class CustomSignupForm(SignupForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")

    def save(self, request):
        user = super().save(request)
        return user
