# Generated by Django 3.0.1 on 2020-01-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200127_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
