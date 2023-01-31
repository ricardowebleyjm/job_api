from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationForm(UserCreationForm):
    """ User creation form to be used in the Admin for creating users"""

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):
    """ User change form to be used in the Admin for changing users passwords"""
    class Meta:
        model = User
        fields = ('email',)