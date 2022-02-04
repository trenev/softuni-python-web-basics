# Generated by Django 4.0.1 on 2022-01-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'In progress'), (3, 'Complete')], default=1),
        ),
    ]
