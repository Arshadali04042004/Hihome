# Generated by Django 3.1.7 on 2021-05-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210521_2117'),
    ]

    operations = [
        migrations.DeleteModel(
            name='myuploadfile',
        ),
        migrations.AlterField(
            model_name='registration',
            name='myfile',
            field=models.FileField(upload_to=''),
        ),
    ]
