from unicodedata import name
from django.contrib import admin
from django.urls import path
from basicinventory.views.home import index
from basicinventory.views.dashboard import overview, item_list, item_detail, item_edit, item_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', overview, name='overview'),
    path('dashboard/items/', item_list, name='item_list'),
    path('dashboard/items/add/', item_add, name='item_add'),
    path('dashboard/items/<uuid:item_id>/', item_detail, name='item_detail'),
    path('dashboard/items/<uuid:item_id>/edit/', item_edit, name='item_edit')
]
