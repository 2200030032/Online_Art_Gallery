# Generated by Django 4.2.11 on 2024-04-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='book',
            new_name='art',
        ),
    ]
