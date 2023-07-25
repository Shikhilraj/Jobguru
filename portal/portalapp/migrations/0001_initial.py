# Generated by Django 4.2.2 on 2023-06-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('birthday', models.DateField()),
                ('password', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
