# Generated by Django 3.1.6 on 2021-02-23 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['data_created'],
            },
        ),
    ]
