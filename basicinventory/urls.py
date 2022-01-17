from unicodedata import name
from django.contrib import admin
from django.urls import path
from basicinventory.views.home import index
from basicinventory.views.dashboard import overview, item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', overview, name='overview'),
    path('dashboard/items/', item_list, name='item_list'),
]
