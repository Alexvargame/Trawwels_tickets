# Generated by Django 4.1.7 on 2023-06-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0006_alter_railwaystations_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainstatus',
            name='speed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Скорость, км/ч'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Экспресс'), (2, 'Скоростной')], max_length=100),
        ),
    ]
