# Generated by Django 2.2.3 on 2019-07-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('department', models.CharField(choices=[('RH', 'Human Resources'), ('ADM', 'Administration'), ('DEV', 'Development'), ('IT', 'Information Technology Manager')], max_length=100)),
            ],
        ),
    ]
