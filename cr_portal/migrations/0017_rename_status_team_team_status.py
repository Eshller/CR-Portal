# Generated by Django 3.2.7 on 2022-06-28 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0016_auto_20220628_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='status',
            new_name='team_status',
        ),
    ]
