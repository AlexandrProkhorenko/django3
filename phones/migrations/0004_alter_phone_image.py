# Generated by Django 4.0.3 on 2022-03-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image_alter_phone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.SlugField(null=True),
        ),
    ]
