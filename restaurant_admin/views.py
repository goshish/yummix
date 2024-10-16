from django.shortcuts import redirect, render
from django.views.generic import ListView


class AdminMain(ListView):
    template_name = 'promo/promo-main.html'
