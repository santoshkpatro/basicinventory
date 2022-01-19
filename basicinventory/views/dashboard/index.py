from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from basicinventory.models.item import Item
from basicinventory.models.warehouse import Warehouse


def overview(request):
    warehouse_count = Warehouse.objects.count()
    item_count = Item.objects.count()

    context = {
        'warehouse_count': warehouse_count,
        'item_count': item_count,
        'url_name': 'overview'
    }
    return render(request, 'dashboard/overview.html', context)


def analytics(request):
    warehouses = Warehouse.objects.annotate(item_count=Count('items'))
    context = {
        'labels': [],
        'data': [],
    }
    for warehouse in warehouses:
        context['labels'].append(warehouse.name)
        context['data'].append(warehouse.item_count)

    return JsonResponse(data=context)
