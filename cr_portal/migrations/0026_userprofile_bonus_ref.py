# Generated by Django 3.2.7 on 2022-07-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0025_userprofile_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bonus_ref',
            field=models.CharField(default='', max_length=200),
        ),
    ]
