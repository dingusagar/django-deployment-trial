# Generated by Django 2.0.7 on 2018-12-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
