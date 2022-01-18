from django.shortcuts import render
from basicinventory.models.warehouse import Warehouse
from basicinventory.forms.warehouse import WarehouseForm


def warehouse_list(request):
    warehouses = Warehouse.objects.all()

    context = {
        'warehouses': warehouses,
        'url_name': 'warehouse_list'
    }
    return render(request, 'dashboard/warehouses/list.html', context)


def warehouse_add(request):
    form = WarehouseForm()

    context = {
        'form': form,
        'url_name': 'warehouse_add'
    }
    return render(request, 'dashboard/warehouses/add.html', context)
