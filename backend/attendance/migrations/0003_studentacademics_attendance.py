# Generated by Django 2.2.5 on 2022-02-10 10:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20220210_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentacademics',
            name='attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Attendance'),
            preserve_default=False,
        ),
    ]
