# Generated by Django 4.0.2 on 2022-03-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='image_as_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
