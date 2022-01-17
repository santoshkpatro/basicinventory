from django.db import models
from basicinventory.models.base import BaseModel


class Warehouse(BaseModel):
    name = models.CharField(max_length=100)
    location = models.TextField()
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_operational = models.BooleanField(default=True)

    class Meta:
        db_table = 'warehouses'

    def __str__(self) -> str:
        return self.name
