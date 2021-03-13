from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from mainapp.models import Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreateForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_read(request):
#     context = {
#         'users': User.objects.all(),
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Список пользователей'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users_read')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#     context = {
#         'form': form,
#         'current_user': user,
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users_read'))

class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_read(request):
#     context = {
#         'products': Product.objects.all(),
#     }
#     return render(request, 'adminapp/admin_products_read.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/admin_products_read.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Список продуктов'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products_read'))
#     else:
#         form = ProductAdminCreateForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'adminapp/admin-poducts-create.html', context)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/admin-poducts-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products_read')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Создание продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products_read'))
#     else:
#         form = ProductAdminCreateForm(instance=product)
#     context = {
#         'form': form,
#         'current_product': product,
#     }
#     return render(request, 'adminapp/admin-products-update-delete.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products_read')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return HttpResponseRedirect(reverse('admins:admin_products_read'))

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
