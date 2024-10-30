from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView
from .models import RestaurantInfo, DishCategory, DishItem, Currency, BarCategory, BarItem, User
from .forms import DishCategoryForm


class AdminMainPageView(ListView):
    template_name = 'restaurant_admin/admin-main.html'
    context_object_name = 'dish_categories'

    def get_queryset(self):
        user = self.request.user
        try:
            restaurant = RestaurantInfo.objects.get(restaurant_owner=user)
            queryset = DishCategory.objects.filter(restaurant=restaurant)
            return queryset
        except RestaurantInfo.DoesNotExist:
            return DishCategory.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DishCategoryForm()  # Добавляем форму в контекст
        return context

    def post(self, request, *args, **kwargs):
        form = DishCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.restaurant = RestaurantInfo.objects.get(restaurant_owner=request.user)
            new_category.save()
            return redirect('admin-main')  # Замените на вашу нужную страницу после добавления
        else:
            return self.get(request, *args, form=form)  # При ошибке форма останется на странице