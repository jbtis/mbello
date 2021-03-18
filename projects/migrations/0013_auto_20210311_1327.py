# Generated by Django 3.1.7 on 2021-03-11 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20210311_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
