# Generated by Django 3.2.5 on 2021-07-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('college', models.CharField(default='', max_length=70)),
                ('subject', models.CharField(default='', max_length=60)),
            ],
        ),
    ]
