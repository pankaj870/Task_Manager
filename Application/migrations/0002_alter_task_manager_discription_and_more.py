# Generated by Django 5.1.7 on 2025-03-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_manager',
            name='discription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='name',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='status',
            field=models.CharField(choices=[('PAN', 'panding'), ('COM', 'complete'), ('REJ', 'rejected')], default='COM'),
        ),
    ]
