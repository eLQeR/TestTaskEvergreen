# Generated by Django 5.0.6 on 2024-06-27 10:53

import test_task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='header',
            field=models.ImageField(default='uploads/images/default_header.png', upload_to=test_task.models.create_header_image_path),
        ),
    ]