from django.contrib import admin
from django.urls import path
from basicinventory.views.home import index
from basicinventory.views.dashboard.index import overview
from basicinventory.views.dashboard.items import item_delete, item_list, item_detail, item_edit, item_add
from basicinventory.views.dashboard.warehouses import warehouse_list, warehouse_add, warehouse_delete, warehouse_edit, warehouse_detail
from basicinventory.views.auth import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('dashboard/', overview, name='overview'),
    path('dashboard/items/', item_list, name='item_list'),
    path('dashboard/items/add/', item_add, name='item_add'),
    path('dashboard/items/<uuid:item_id>/', item_detail, name='item_detail'),
    path('dashboard/items/<uuid:item_id>/edit/', item_edit, name='item_edit'),
    path(
        'dashboard/items/<uuid:item_id>/delete/',
        item_delete,
        name='item_delete'
    ),
    path('dashboard/warehouses/', warehouse_list, name='warehouse_list'),
    path('dashboard/warehouses/add/', warehouse_add, name='warehouse_add'),
    path(
        'dashboard/warehouses/<uuid:warehouse_id>/',
        warehouse_detail,
        name='warehouse_detail'
    ),
    path(
        'dashboard/warehouses/<uuid:warehouse_id>/edit/',
        warehouse_edit,
        name='warehouse_edit'
    ),
    path(
        'dashboard/warehouses/<uuid:warehouse_id>/delete/',
        warehouse_delete,
        name='warehouse_delete'
    ),
]
