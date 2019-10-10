# Generated by Django 2.1.1 on 2019-10-03 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20191004_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.EventName')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester')),
                ('sy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.SY')),
            ],
        ),
    ]
