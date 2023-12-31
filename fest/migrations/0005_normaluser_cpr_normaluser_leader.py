# Generated by Django 4.1 on 2023-01-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fest', '0004_event_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='cpr',
            field=models.BooleanField(default=False, verbose_name='CPR Workshop'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='leader',
            field=models.BooleanField(default=False, verbose_name='Leadership Program'),
        ),
    ]
