# Generated by Django 4.1 on 2023-06-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0033_alter_team_crid1_alter_team_crid2_alter_team_crid3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='proof2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='task2_status',
            field=models.BooleanField(default='False'),
        ),
    ]