# Generated by Django 3.1.14 on 2022-10-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
