# Generated by Django 3.2.6 on 2021-08-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=2048)),
                ('short', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
