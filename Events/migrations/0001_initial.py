# Generated by Django 2.2 on 2019-10-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_quote', models.TextField(blank=True, null=True)),
                ('event_quote_author', models.CharField(max_length=255, null=True)),
                ('event_1_Prize', models.CharField(max_length=255)),
                ('event_2_Prize', models.CharField(max_length=255)),
                ('event_3_Prize', models.CharField(max_length=255)),
                ('event_reg_active', models.BooleanField(default=True)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_head', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=10)),
                ('description_file', models.FileField(upload_to='cultural_docs')),
                ('event_logo', models.ImageField(upload_to='cultural_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Informal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_quote', models.TextField(blank=True, null=True)),
                ('event_quote_author', models.CharField(max_length=255, null=True)),
                ('event_1_Prize', models.CharField(blank=True, max_length=255, null=True)),
                ('event_2_Prize', models.CharField(blank=True, max_length=255, null=True)),
                ('event_3_Prize', models.CharField(blank=True, max_length=255, null=True)),
                ('event_reg_active', models.BooleanField(default=True)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_head', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=10)),
                ('description_file', models.FileField(upload_to='informal_docs')),
                ('event_logo', models.ImageField(upload_to='informal_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_quote', models.TextField(blank=True, null=True)),
                ('event_quote_author', models.CharField(max_length=255, null=True)),
                ('event_1_Prize', models.CharField(max_length=255)),
                ('event_2_Prize', models.CharField(max_length=255)),
                ('event_3_Prize', models.CharField(max_length=255)),
                ('event_reg_active', models.BooleanField(default=True)),
                ('event_description', models.TextField(blank=True, null=True)),
                ('event_head', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=10)),
                ('description_file', models.FileField(upload_to='technical_docs')),
                ('event_logo', models.ImageField(upload_to='technical_logo')),
            ],
        ),
    ]
