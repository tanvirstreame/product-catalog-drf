# Generated by Django 2.2.7 on 2019-11-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20191119_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='marketplace.PriceDateRange'),
        ),
    ]
