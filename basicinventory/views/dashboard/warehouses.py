from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        addForm = WarehouseForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect('warehouse_list')
        else:
            return redirect('warehouse_list')

    form = WarehouseForm()
    context = {
        'form': form,
        'url_name': 'warehouse_add'
    }
    return render(request, 'dashboard/warehouses/add.html', context)


def warehouse_detail(request, warehouse_id):
    try:
        warehouse = Warehouse.objects.get(pk=warehouse_id)
        context = {
            'warehouse': warehouse
        }
        return render(request, 'dashboard/warehouses/detail.html', context)
    except Warehouse.DoesNotExist:
        return redirect('warehouse_list')


def warehouse_edit(request, warehouse_id):
    try:
        warehouse = Warehouse.objects.get(pk=warehouse_id)

        if request.method == 'POST':
            form = WarehouseForm(request.POST, instance=warehouse)
            if form.is_valid():
                form.save()
                return redirect('warehouse_list')
            else:
                print('Invalid form')
                return redirect('warehouse_edit', warehouse_id=warehouse_id)

        context = {
            'warehouse': warehouse,
        }
        return render(request, 'dashboard/warehouses/edit.html', context)
    except Warehouse.DoesNotExist:
        return redirect('warehouse_list')


def warehouse_delete(request, warehouse_id):
    try:
        warehouse = Warehouse.objects.get(pk=warehouse_id)
        warehouse.delete()
        return redirect('warehouse_list')
    except Warehouse.DoesNotExist:
        return redirect('warehouse_list')
