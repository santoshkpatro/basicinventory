from django.shortcuts import render
from basicinventory.models.item import Item


def overview(request):
    return render(request, 'dashboard/overview.html')


def item_list(request):
    items = Item.objects.all()

    context = {
        'items': items
    }
    return render(request, 'dashboard/items/list.html', context)
