# Generated by Django 4.0.3 on 2022-03-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=10),
        ),
    ]