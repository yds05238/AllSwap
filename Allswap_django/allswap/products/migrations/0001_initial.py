# Generated by Django 3.0.1 on 2020-01-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('courseID', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]