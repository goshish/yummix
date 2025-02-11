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


class DishItemsForm(forms.ModelForm):
    class Meta:
        model = DishItem
        fields = ['dish_item_name', 'dish_item_description', 'dish_item_weight', 'is_allergenic_dish_item',
                  'dish_item_price', 'dish_item_cooking_time', 'is_active_dish_item', 'dish_item_photo']


class BarItemsForm(forms.ModelForm):
    class Meta:
        model = BarItem
        fields = ['bar_item_name', 'bar_item_description', 'bar_item_weight', 'is_allergenic_bar_item',
                  'bar_item_price', 'bar_item_cooking_time', 'is_active_bar_item', 'bar_item_photo']


class RestaurantInfoForm(forms.ModelForm):
    class Meta:
        model = RestaurantInfo
        fields = ['restaurant_name', 'restaurant_address', 'restaurant_wifi', 'restaurant_logo', 'restaurant_background_image', 'restaurant_phone_number']
