from django.db import models
from django.core.exceptions import ValidationError


def validate_georgian_phone_number(value):
    if not value.startswith('+995'):
        raise ValidationError("Phone number must start with '+995'.")
    if len(value) != 13:  # +995 + 9 цифр
        raise ValidationError("Phone number must contain exactly 12 digits including the country code.")
    if not value[1:].isdigit():  # Игнорируем первый символ '+' и проверяем остальные
        raise ValidationError("Phone number must contain only digits after '+'.")


class CallbackRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Phone Number",
        validators=[validate_georgian_phone_number]
    )
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Callback Request"
        verbose_name_plural = "Callback Requests"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ||| {self.phone_number} ||| ({self.created_at})"
