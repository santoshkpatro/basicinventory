from enum import unique
from django.db import models
from basicinventory.models.base import BaseModel
from basicinventory.models.warehouse import Warehouse


class Item(BaseModel):
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items'
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=2
    )
    supplier_details = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'items'
        unique_together = ['warehouse', 'code']

    def __str__(self) -> str:
        return self.name
