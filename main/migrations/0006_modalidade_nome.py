# Generated by Django 2.1.2 on 2018-11-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181124_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='modalidade',
            name='nome',
            field=models.CharField(default='a', max_length=60),
        ),
    ]
