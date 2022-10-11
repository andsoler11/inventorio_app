from django.urls import path
from apps.inventario import views


urlpatterns = [
    path('', views.renderProduct, name="product"),
    # edit inventario
    path('edit/<str:pk>', views.editProduct, name="edit_product"),
    # delete inventario
    path('delete/<str:pk>', views.deleteProduct, name="delete_product"),
]