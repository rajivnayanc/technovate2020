# Generated by Django 2.2 on 2019-10-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultural',
            name='event_1_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cultural',
            name='event_2_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cultural',
            name='event_3_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='event_1_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='event_2_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='technical',
            name='event_3_Prize',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
