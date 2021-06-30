from django.urls import path
from api import views

urlpatterns = [
    path('', views.product_get),
    path('vendas/list', views.list_all, name='list_all_vendas'),
    path('vendas/create', views.create, name='create_vendas'),

]
