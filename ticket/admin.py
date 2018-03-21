# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from ticket.models import NewTicket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_title', 'ticket_status', 'ticket_created_at',)
    list_filter = ('ticket_status', 'ticket_created_at',)
    search_fields = ('ticket_title', 'ticket_description',)

    fieldsets = (
        ('Información de ticket', {
            'fields': ('ticket_title', 'ticket_description',),
            'classes': ('wide',)
        }),
        ('Status ticket', {
            'fields': ('ticket_status',),
            'classes': ('wide',)
        }),
    )



admin.site.register(NewTicket, TicketAdmin)