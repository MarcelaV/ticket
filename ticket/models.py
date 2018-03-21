# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
ABIERTO = 'ABIERTO'
PENDIENTE = 'PENDIENTE'
EN_PROCESO = 'EN_PROCESO'
RESUELTO = 'RESUELTO'
CERRADO = 'CERRADO'

STATUS = (
    (ABIERTO, 'Abierto'),
    (PENDIENTE, 'Pendiente'),
    (EN_PROCESO, 'En proceso'),
    (RESUELTO, 'Resuelto'),
    (CERRADO, 'Cerrado')
)

class NewTicket(models.Model):

    ticket_title = models.CharField(verbose_name='Título', max_length=50)
    ticket_description = models.TextField(verbose_name='Descripción',)
    ticket_status = models.CharField(verbose_name='Status', max_length=10, choices=STATUS)
    ticket_created_at = models.DateTimeField(verbose_name='F. creación', auto_now_add=True)

    def __unicode__(self):
        return self.ticket_title