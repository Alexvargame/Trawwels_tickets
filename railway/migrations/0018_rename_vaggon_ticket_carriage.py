# Generated by Django 4.1.7 on 2023-06-26 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0017_alter_scheduletrains_options_scheduletrains_on_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='vaggon',
            new_name='carriage',
        ),
    ]
