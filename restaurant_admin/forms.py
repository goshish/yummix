from django import forms
from .models import RestaurantInfo, DishCategory, DishItem, BarCategory, BarItem


class DishCategoryForm(forms.ModelForm):
    class Meta:
        model = DishCategory
        fields = ['dish_category_name', 'dish_category_description', 'is_active_dish_category', 'dish_category_photo']