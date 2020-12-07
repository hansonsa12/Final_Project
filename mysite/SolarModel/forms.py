from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields =['item_name', 'item_size', 'item_mass', 'item_age', 'item_characteristics', 'item_distance']