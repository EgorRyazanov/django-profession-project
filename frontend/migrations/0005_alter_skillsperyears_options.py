# Generated by Django 4.1.5 on 2023-01-10 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_skillsperyears'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillsperyears',
            options={'verbose_name': 'Навыки', 'verbose_name_plural': 'Навыки'},
        ),
    ]