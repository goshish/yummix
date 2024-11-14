from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, DetailView
from unicodedata import category
from .models import RestaurantInfo, DishCategory, DishItem, Currency, BarCategory, BarItem, User
from .forms import DishCategoriesForm, BarCategoriesForm


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
        context['form'] = DishCategoriesForm()
        return context

    def post(self, request, *args):
        form = DishCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.restaurant = RestaurantInfo.objects.get(restaurant_owner=request.user)
            new_category.save()
            return redirect('admin-main')
        else:
            return self.get(request, *args, form=form)


class DishCategoryDetailView(DetailView):
    model = DishCategory
    template_name = 'restaurant_admin/dish-category-detail.html'
    context_object_name = 'dish_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_items'] = DishItem.objects.filter(category=self.object)
        return context


class BarCategoryView(ListView):
    model = BarCategory
    template_name = 'restaurant_admin/bar-category-list.html'
    context_object_name = 'bar_categories'

    def get_queryset(self):
        user = self.request.user
        try:
            restaurant = RestaurantInfo.objects.get(restaurant_owner=user)
            queryset = BarCategory.objects.filter(restaurant=restaurant)
            return queryset
        except RestaurantInfo.DoesNotExist:
            return BarCategory.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BarCategoriesForm
        return context

    def post(self, request, *args):
        form = BarCategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.restaurant = RestaurantInfo.objects.get(restaurant_owner=request.user)
            new_category.save()
            return redirect('bar-categories')
        else:
            return self.get(request, *args, form=form)


class BarCategoryDetailView(DetailView):
    model = BarCategory
    template_name = 'restaurant_admin/bar-category-detail.html'
    context_object_name = 'bar_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bar_items'] = BarItem.objects.filter(category=self.object)
        return context

