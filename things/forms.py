from django import forms
from django.core.validators import RegexValidator

class ThingForm(forms.Form):
    name = forms.CharField(label = "Name",max_length=120, blank=False )
    description = forms.Textarea(label = "Description",max_length=120, blank=False )
    quantity = forms.NumberInput(label = "Quantity", max_length=120, blank=False )

