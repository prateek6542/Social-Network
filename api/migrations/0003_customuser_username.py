# Generated by Django 3.0.5 on 2024-06-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240606_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='username', max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
