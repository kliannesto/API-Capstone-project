# Generated by Django 2.1.1 on 2020-03-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_smslogs_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]