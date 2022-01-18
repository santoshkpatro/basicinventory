from django import forms
from basicinventory.models.warehouse import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = [
            'name',
            'location',
            'capacity',
            'description',
            'is_operational'
        ]
