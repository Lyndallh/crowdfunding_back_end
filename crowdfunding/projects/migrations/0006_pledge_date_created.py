# Generated by Django 4.2.3 on 2024-01-27 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
