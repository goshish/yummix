from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    currency_name = models.CharField(max_length=50, verbose_name="Currency Name")
    currency_code = models.CharField(max_length=3, verbose_name="Currency Code")
    currency_symbol = models.CharField(max_length=5, verbose_name="Currency Symbol")

    def __str__(self):
        return f"{self.currency_name} ({self.currency_code})"


class RestaurantInfo(models.Model):
    restaurant_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurants")
    restaurant_name = models.CharField(blank=False, verbose_name="Restaurant name", unique=True, max_length=255)
    restaurant_address = models.TextField(blank=False, verbose_name="Restaurant address")
    restaurant_wifi = models.TextField(blank=True, verbose_name="Restaurant wi-fi password")
    restaurant_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=False,
                                            verbose_name="Restaurant Currency")

    def __str__(self):
        return self.restaurant_name


class DishCategory(models.Model):
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE, related_name="dish_categories")
    dish_category_name = models.CharField(blank=False, verbose_name="Dish category name", max_length=20)
    dish_category_description = models.TextField(blank=True, verbose_name="Dish category description", max_length=100)
    is_active_dish_category = models.BooleanField(default=True, verbose_name="Is dish category active")
    dish_category_photo = models.ImageField(blank=True, verbose_name="Dish category photo")

    def __str__(self):
        return self.dish_category_name


class DishItem(models.Model):
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name="dish_items")
    dish_item_name = models.CharField(blank=False, verbose_name="Dish item name", max_length=20)
    dish_item_description = models.TextField(blank=True, verbose_name="Dish item description", max_length=100)
    dish_item_weight = models.IntegerField(blank=True, null=True, verbose_name="Dish item weight")
    is_allergenic_dish_item = models.BooleanField(default=False, verbose_name="Is allergenic dish item")
    dish_item_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10,
                                          verbose_name="Dish item price")
    dish_item_cooking_time = models.IntegerField(blank=True, null=True, verbose_name="Dish item cooking time")
    is_active_dish_item = models.BooleanField(default=True, verbose_name="Is dish item active")
    dish_item_photo = models.ImageField(blank=True, verbose_name="Dish item photo")

    def __str__(self):
        return self.dish_item_name


class BarCategory(models.Model):
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE, related_name="bar_categories")
    bar_category_name = models.CharField(blank=False, verbose_name="Bar category name", max_length=20)
    bar_category_description = models.TextField(blank=True, verbose_name="Bar category description", max_length=100)
    is_bar_category_active = models.BooleanField(default=True, verbose_name="Is bar category active")
    bar_category_photo = models.ImageField(blank=True, verbose_name="Bar category photo")

    def __str__(self):
        return self.bar_category_name


class BarItem(models.Model):
    category = models.ForeignKey(BarCategory, on_delete=models.CASCADE, related_name="bar_items")
    bar_item_name = models.CharField(blank=False, verbose_name="Bar item name", max_length=20)
    bar_item_description = models.TextField(blank=True, verbose_name="Bar item description", max_length=100)
    bar_item_weight = models.IntegerField(blank=True, null=True, verbose_name="Bar item weight")
    is_allergenic_bar_item = models.BooleanField(default=False, verbose_name="Is bar item allergenic")
    bar_item_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10,
                                         verbose_name="Bar item price")
    bar_item_cooking_time = models.IntegerField(blank=True, null=True, verbose_name="Bar item cooking time")
    is_active_bar_item = models.BooleanField(default=True, verbose_name="Is bar item active")
    bar_item_photo = models.ImageField(blank=True, verbose_name="Bar item photo")

    def __str__(self):
        return self.bar_item_name
