# Generated by Django 3.0.8 on 2020-08-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.CharField(default='all', max_length=20),
        ),
    ]