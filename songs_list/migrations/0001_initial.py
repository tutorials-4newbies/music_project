# Generated by Django 4.0 on 2021-12-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
            ],
        ),
    ]
