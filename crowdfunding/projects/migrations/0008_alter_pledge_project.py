# Generated by Django 4.2.3 on 2024-02-18 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_enddatetime_project_date_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project'),
        ),
    ]
