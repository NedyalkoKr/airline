# Generated by Django 2.1.3 on 2018-11-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20181126_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flight.Flight')),
            ],
        ),
    ]
