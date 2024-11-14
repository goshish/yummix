from django import forms
from .models import RestaurantInfo, DishCategory, DishItem, BarCategory, BarItem


class DishCategoriesForm(forms.ModelForm):
    class Meta:
        model = DishCategory
        fields = ['dish_category_name', 'dish_category_description', 'is_active_dish_category', 'dish_category_photo']



class BarCategoriesForm(forms.ModelForm):
    class Meta:
        model = BarCategory
        fields = ['bar_category_name', 'bar_category_description', 'is_bar_category_active', 'bar_category_photo']