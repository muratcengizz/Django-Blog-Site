# Generated by Django 4.1 on 2022-09-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMainApp', '0007_makaleyaz_makaleninbenzersizidsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='makaleyaz',
            name='makaleismi',
            field=models.CharField(default='', max_length=200),
        ),
    ]