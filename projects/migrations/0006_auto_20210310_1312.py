# Generated by Django 3.1.7 on 2021-03-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210310_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/img/'),
        ),
    ]
