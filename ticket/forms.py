# coding=utf-8
from django import forms

from ticket.models import NewTicket


class TicketForm(forms.ModelForm):
    class Meta:
        model = NewTicket

        fields = [
            'ticket_title',
            'ticket_description',
            'ticket_status',
        ]

        labels = {
            'ticket_title': 'Nombre',
            'ticket_description': 'Descripción',
            'ticket_status': 'Status',
        }

        widgets = {
            'ticket_title': forms.TextInput(attrs={'class': 'form-control'}),
            'ticket_description': forms.Textarea(attrs={'class': 'form-control'}),
            'ticket_status': forms.RadioSelect(),
        }