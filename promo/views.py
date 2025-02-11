from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from .forms import CustomUserCreationForm, CallbackRequestForm
from django.contrib import messages
from restaurant_admin.models import RestaurantInfo
from django.contrib.auth import logout, authenticate, login
from .forms import LoginUserForm


class PromoMainPageView(TemplateView):
    template_name = 'promo/promo-main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем форму в контекст
        context['callback_form'] = CallbackRequestForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('promo-main')
        else:
            context = self.get_context_data()
            context['callback_form'] = form
            return self.render_to_response(context)


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-main')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'promo/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('admin-main'))
    else:
        form = LoginUserForm()
    form = LoginUserForm
    return render(request, 'promo/login.html', {'form': form})
