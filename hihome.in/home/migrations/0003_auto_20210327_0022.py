# Generated by Django 3.1.7 on 2021-03-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210327_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='zipc',
            new_name='zip',
        ),
    ]
