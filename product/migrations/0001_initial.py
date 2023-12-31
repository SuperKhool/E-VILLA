# Generated by Django 4.2.7 on 2023-11-06 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50)),
                ('prod_img', models.ImageField(upload_to='product_image')),
                ('old_price', models.PositiveIntegerField()),
                ('new_price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=250)),
                ('catagoty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.catagory')),
            ],
        ),
    ]
