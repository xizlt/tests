# Generated by Django 3.1.7 on 2021-02-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210225_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='launch',
            old_name='created',
            new_name='update',
        ),
        migrations.AlterField(
            model_name='dataprofile',
            name='photo',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.URLField(),
        ),
    ]
