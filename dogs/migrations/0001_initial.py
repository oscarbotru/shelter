# Generated by Django 4.2.1 on 2023-05-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Кличка')),
                ('category', models.CharField(max_length=100, verbose_name='Порода')),
                ('phot', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='Фото')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
            },
        ),
    ]
