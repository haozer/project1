# Generated by Django 3.0.3 on 2020-08-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=264, unique=True)),
                ('forename', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
            ],
        ),
    ]
