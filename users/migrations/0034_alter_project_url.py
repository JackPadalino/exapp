# Generated by Django 4.0 on 2022-06-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(default='https://www.youtube.com/watch?v=XIMLoLxmTDw', max_length=1000),
        ),
    ]
