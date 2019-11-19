# Generated by Django 2.2.7 on 2019-11-19 12:56

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceDateRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='extra_attribute',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='marketplace.PriceDateRange'),
        ),
    ]