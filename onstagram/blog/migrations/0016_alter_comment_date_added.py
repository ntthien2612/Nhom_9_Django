# Generated by Django 3.2.5 on 2022-11-14 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
