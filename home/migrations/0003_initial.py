# Generated by Django 4.2.7 on 2023-11-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.TextField(max_length=30)),
                ('mail', models.EmailField(max_length=50)),
                ('msg', models.TextField(max_length=10000)),
            ],
        ),
    ]