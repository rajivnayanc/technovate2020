# Generated by Django 2.2 on 2020-01-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
