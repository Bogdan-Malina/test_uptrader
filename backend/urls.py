from django.contrib import admin
from django.urls import path

from tree_menu.models import Menu
from tree_menu.views import IndexPageView


app_name = 'menu'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(extra_context=dict(menu=Menu.objects.all())), name='index')
]