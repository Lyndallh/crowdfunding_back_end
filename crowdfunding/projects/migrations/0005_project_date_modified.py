# Generated by Django 4.2.3 on 2024-01-27 01:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_enddatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
