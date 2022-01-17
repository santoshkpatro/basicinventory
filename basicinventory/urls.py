from django.contrib import admin
from django.urls import path
from basicinventory.views.home import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
