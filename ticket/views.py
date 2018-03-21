# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, request, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.base import View

from django.views.generic.list import ListView
from django.utils import timezone

import ticket
from ticket.forms import TicketForm
from ticket.models import NewTicket

class TicketListView(generic.ListView):

    model = NewTicket
    context_object_name = 'ticket_list'
    queryset = NewTicket.objects.all().order_by('-ticket_created_at')[:7]
    template_name = 'ticket/ticket_list.html'


class TicketCreate(CreateView):
    model = NewTicket
    form_class = TicketForm
    template_name = 'ticket/ticket_create.html'
    success_url = reverse_lazy('ticket:ticket_list')

class TicketDetail(View):
    def get(self, request, pk):
        posibles_tickets = NewTicket.objects.filter(pk=pk)
        ticket = posibles_tickets[0] if len(posibles_tickets) >=1 else None
        if ticket is not None:
            context = {
                'ticket': ticket
            }
            return render(request, 'ticket/detail.html', context)
        else:
            return HttpResponseNotFound('No hay')


def home(request):
    return render(request, 'ticket/home.html')