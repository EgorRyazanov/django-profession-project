# Generated by Django 4.1.5 on 2023-01-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_skillsperyears_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsperyears',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo', verbose_name='Фото'),
        ),
    ]