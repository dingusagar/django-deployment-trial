# Generated by Django 2.0.7 on 2018-12-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktracker', '0002_work_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
