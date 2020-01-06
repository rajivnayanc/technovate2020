# Generated by Django 2.2 on 2019-10-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.TextField()),
                ('event_poster', models.ImageField(upload_to='pre_event_poster')),
                ('event_link', models.URLField()),
                ('event_date', models.CharField(max_length=50)),
            ],
        ),
    ]
