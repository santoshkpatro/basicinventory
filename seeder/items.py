import shortuuid
import random
from basicinventory.models.item import Item
from basicinventory.models.warehouse import Warehouse
import json

f = open('items.json')

data = json.load(f)

for i in data:
    code = shortuuid.ShortUUID().random(length=5).upper()
    quantity = random.randint(10, 200)

    try:
        warehouse = Warehouse.objects.order_by('?')[0]
        item = Item(**i, code=code, quantity=quantity, warehouse=warehouse)
        item.save()
        print('Item saved', item.name)
    except:
        print('Unable to create')
