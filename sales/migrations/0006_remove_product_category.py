# Generated by Django 4.0.4 on 2023-05-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_product_category_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
