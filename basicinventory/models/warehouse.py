from django.db import models
from basicinventory.models.base import BaseModel


class OperationalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_operational=True)


class Warehouse(BaseModel):
    name = models.CharField(max_length=100)
    location = models.TextField()
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    is_operational = models.BooleanField(default=True)

    objects = models.Manager()
    operational_objects = OperationalManager()

    class Meta:
        db_table = 'warehouses'

    def __str__(self) -> str:
        return self.name
