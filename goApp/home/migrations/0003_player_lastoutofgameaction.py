# Generated by Django 3.0.8 on 2020-07-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200717_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='lastOutOfGameAction',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
