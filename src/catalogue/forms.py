from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError

from . import models


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
