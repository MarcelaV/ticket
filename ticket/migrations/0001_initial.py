# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_title', models.CharField(max_length=50)),
                ('ticket_description', models.TextField()),
                ('ticket_status', models.CharField(choices=[('ABIERTO', 'Abierto'), ('PENDIENTE', 'Pendiente'), ('EN_PROCESO', 'En proceso'), ('RESUELTO', 'Resuelto'), ('CERRADO', 'Cerrado')], max_length=10)),
                ('ticket_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
