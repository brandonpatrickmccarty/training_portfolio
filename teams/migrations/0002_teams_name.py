# Generated by Django 5.1.7 on 2025-04-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='Name',
            field=models.CharField(default='null', max_length=75),
            preserve_default=False,
        ),
    ]
