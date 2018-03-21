# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegistroUsuario(CreateView):
    model = User
    template_name = 'users/registrar.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('ticket:ticket_list')






