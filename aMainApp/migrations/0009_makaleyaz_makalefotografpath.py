# Generated by Django 4.1 on 2022-09-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMainApp', '0008_makaleyaz_makaleismi'),
    ]

    operations = [
        migrations.AddField(
            model_name='makaleyaz',
            name='makaleFotografPath',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
