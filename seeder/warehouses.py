import random
from basicinventory.models.warehouse import Warehouse
import json

f = open('warehouses.json')

data = json.load(f)

for i in data:
    try:
        capacity = random.randint(200, 2000)
        warehouse = Warehouse(**i, capacity=capacity)
        warehouse.save()

        print('Warehouse created', warehouse.name)
    except:
        print('Unable to create warehouse')
