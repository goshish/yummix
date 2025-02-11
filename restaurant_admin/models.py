from Tools.scripts.cleanfuture import verbose
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
from django.core.validators import RegexValidator



from django.db import models
from django.contrib.auth.models import User

class RestaurantInfo(models.Model):
    restaurant_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurants", verbose_name="Restaurant Owner"
    )
    restaurant_name = models.CharField(
        max_length=255, blank=False, verbose_name="Restaurant Name", unique=True
    )
    restaurant_address = models.TextField(
        blank=False, verbose_name="Restaurant Address"
    )
    restaurant_wifi = models.TextField(
        blank=True, verbose_name="Restaurant Wi-Fi Password"
    )
    restaurant_phone_number = models.CharField(
        max_length=13,
        blank=False,
        verbose_name="Restaurant Phone Number",
        validators=[
            RegexValidator(
                regex=r'^\+995\d{9}$',
                message="Phone number must be in the format +995XXXXXXXX and contain 12 digits."
            )
        ],
    )
    restaurant_logo = models.ImageField(
        blank=False, upload_to="restaurant/logos/", verbose_name="Restaurant Logo Image"
    )
    restaurant_background_image = models.ImageField(
        blank=False, upload_to="restaurant/backgrounds/", verbose_name="Restaurant Background Image"
    )

    def __str__(self):
        return self.restaurant_name


class DishCategory(models.Model):
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE, related_name="dish_categories")
    dish_category_name = models.CharField(blank=False, verbose_name="Dish category name", max_length=20)
    dish_category_description = models.TextField(blank=True, verbose_name="Dish category description", max_length=100)
    is_active_dish_category = models.BooleanField(default=True, verbose_name="Is dish category active")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    dish_category_photo = models.ImageField(blank=True, verbose_name="Dish category photo")

    def __str__(self):
        return self.dish_category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.dish_category_name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('dish-category-detail', kwargs={'slug': self.slug})


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
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    bar_category_photo = models.ImageField(blank=True, verbose_name="Bar category photo")

    def __str__(self):
        return self.bar_category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.bar_category_name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bar-category-detail', kwargs={'slug': self.slug})


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
