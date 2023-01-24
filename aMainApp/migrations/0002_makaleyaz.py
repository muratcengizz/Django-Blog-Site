# Generated by Django 4.1 on 2022-09-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='makaleYaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('paragraf1', models.TextField(max_length=1000)),
                ('paragraf2', models.TextField(max_length=1000)),
                ('paragraf3', models.TextField(max_length=1000)),
                ('paragraf4', models.TextField(max_length=1000)),
            ],
        ),
    ]