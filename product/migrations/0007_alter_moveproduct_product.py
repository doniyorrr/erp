# Generated by Django 3.2.7 on 2022-04-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_moveproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moveproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
