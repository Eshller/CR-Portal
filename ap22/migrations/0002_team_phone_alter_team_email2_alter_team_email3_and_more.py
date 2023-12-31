# Generated by Django 4.1 on 2022-10-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap22', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='email2',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='team',
            name='email3',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='team',
            name='email4',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='team',
            name='member2',
            field=models.CharField(blank=True, default='', max_length=240, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='member3',
            field=models.CharField(blank=True, default='', max_length=240, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='member4',
            field=models.CharField(blank=True, default='', max_length=240, verbose_name='Name'),
        ),
    ]
