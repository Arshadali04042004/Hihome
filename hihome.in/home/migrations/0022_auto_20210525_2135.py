# Generated by Django 3.1.7 on 2021-05-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_myuploadfile_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuploadfile',
            name='f_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
