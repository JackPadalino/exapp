# Generated by Django 4.0 on 2022-06-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_galleryphoto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='school_year',
            field=models.IntegerField(default=2022),
        ),
    ]
