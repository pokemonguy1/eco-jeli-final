# Generated by Django 4.1.2 on 2022-10-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='date',
            field=models.DateField(verbose_name='Дата проведения'),
        ),
    ]