# Generated by Django 3.1.7 on 2021-05-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210427_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='myfile',
            field=models.FileField(upload_to=''),
        ),
    ]
