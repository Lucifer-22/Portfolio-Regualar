# Generated by Django 3.2 on 2021-07-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210706_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillset',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='competence/'),
        ),
    ]
