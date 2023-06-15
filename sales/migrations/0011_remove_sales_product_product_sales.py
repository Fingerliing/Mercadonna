# Generated by Django 4.0.4 on 2023-05-11 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_alter_sales_end_date_alter_sales_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sales.sales'),
        ),
    ]