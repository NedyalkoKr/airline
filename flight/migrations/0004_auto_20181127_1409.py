# Generated by Django 2.1.3 on 2018-11-27 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='flights',
            new_name='flight',
        ),
    ]