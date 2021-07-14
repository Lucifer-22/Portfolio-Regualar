# Generated by Django 3.2 on 2021-07-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_alter_skillset_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rating',
            field=models.PositiveIntegerField(choices=[('1', 'poor'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=2),
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skillrank',
            field=models.PositiveIntegerField(choices=[('1', 'poor'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=2),
        ),
    ]
