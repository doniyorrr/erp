# Generated by Django 3.2.7 on 2022-04-18 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0013_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.customuser'),
            preserve_default=False,
        ),
    ]