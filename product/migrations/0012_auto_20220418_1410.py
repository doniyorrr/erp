# Generated by Django 3.2.7 on 2022-04-18 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_supplier_user'),
        ('product', '0011_alter_product_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.market'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
    ]