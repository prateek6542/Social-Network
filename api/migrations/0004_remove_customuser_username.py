# Generated by Django 3.0.5 on 2024-06-06 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
