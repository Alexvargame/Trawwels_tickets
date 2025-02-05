# Generated by Django 4.1.7 on 2023-05-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0002_trainstatus_alter_railwaystations_city_trains'),
    ]

    operations = [
        migrations.AddField(
            model_name='railwaystations',
            name='neighbours',
            field=models.ManyToManyField(blank=True, related_name='neighbours_stations', to='railway.railwaystations', verbose_name='соседние станции'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='trains',
            name='status',
            field=models.CharField(blank=True, choices=[('Экспресс', 'Экспресс'), ('Скоростной', 'Скоростной')], max_length=100),
        ),
    ]
