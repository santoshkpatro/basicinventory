from django import forms
from basicinventory.models.item import Item


class ItemForm(forms.ModelForm):
    warehouse_id = forms.UUIDField(required=False)

    class Meta:
        model = Item
        fields = [
            'code',
            'name',
            'description',
            'quantity',
            'price',
            'supplier_details',
            'is_available',
            'warehouse_id'
        ]
