# Generated by Django 2.1.1 on 2019-10-02 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(unique=True),
        ),
    ]