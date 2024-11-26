from django.db import models


class CallbackRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name="Client name")
    phone_number = models.CharField(max_length=20, verbose_name="Client phone number ")
    email = models.EmailField(verbose_name="Client E-mail")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Request Date and Time")

    class Meta:
        verbose_name = "Callback Request"
        verbose_name_plural = "Callback Requests"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.phone_number})"
