# Generated by Django 3.1.7 on 2021-03-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210327_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='competetion',
            new_name='competetions',
        ),
    ]
