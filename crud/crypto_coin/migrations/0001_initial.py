# Generated by Django 4.2.2 on 2023-06-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=200)),
                ('coin_price', models.IntegerField()),
                ('coin_exchange', models.CharField(max_length=200)),
            ],
        ),
    ]
