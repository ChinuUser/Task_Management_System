# Generated by Django 5.1.3 on 2024-11-13 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Management_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=50)),
                ('em', models.CharField(max_length=50)),
                ('ph', models.BigIntegerField()),
                ('dg', models.CharField(max_length=50)),
                ('dp', models.CharField(max_length=50)),
                ('ofid', models.BigIntegerField()),
                ('pas', models.BigIntegerField()),
            ],
        ),
    ]