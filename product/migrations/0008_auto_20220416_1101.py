# Generated by Django 3.2.7 on 2022-04-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_moveproduct_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moveproduct',
            options={'verbose_name_plural': "Tovarlarni Ko'chirish"},
        ),
        migrations.RemoveField(
            model_name='moveproduct',
            name='received_date',
        ),
        migrations.AlterField(
            model_name='trashproduct',
            name='thrown_date',
            field=models.DateField(verbose_name='Musirga Chiqarib yuborilgan sana'),
        ),
    ]