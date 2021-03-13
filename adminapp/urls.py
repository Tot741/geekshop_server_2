from django.urls import path

# from adminapp.views import index, admin_users_read, admin_users_create, admin_users_update, admin_users_delete, \
#     admin_products_read, admin_products_create, admin_products_delete, admin_products_update
from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, ProductListView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin-products-read/', ProductListView.as_view(), name='admin_products_read'),
    path('admin-products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('admin-products-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('admin-products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
]
