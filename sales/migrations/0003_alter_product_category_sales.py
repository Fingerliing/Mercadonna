# Generated by Django 4.0.4 on 2023-05-05 09:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_product_category_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BIO', 'Bio et écologie'), ('FRUITS_ET_LEGUMES', 'Fruits et légumes'), ('VIANDE_ET_POISSON', 'Viande et poisson'), ('PAIN_ET_PATISSERIE', 'Pain et pâtisseries'), ('FRAIS', 'Produits frais'), ('SURGELE', 'Surgelés'), ('BOISSONS', 'Boissons'), ('EPICERIE_SALEE', 'Epicerie salée'), ('EPICERIE_SUCREE', 'Epicerie sucrée'), ('PRODUITS_DU_MONDE', 'Produits du monde')], max_length=32, null=True),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('percentage', models.DecimalField(decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.product')),
            ],
        ),
    ]
