from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError

from . import models


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'

class AddSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = '__all__'

class AddTheAuthorsForm(forms.ModelForm):
    class Meta:
        model = models.TheAuthors
        fields = '__all__'

class AddPublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = '__all__'
