# Generated by Django 4.0.4 on 2023-05-11 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_remove_product_sales_sales_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='sales',
            new_name='product',
        ),
    ]
