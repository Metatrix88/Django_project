from django import forms

from . import models


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'
