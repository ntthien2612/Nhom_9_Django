# Generated by Django 3.2.5 on 2022-11-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_date_posted_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(),
        ),
    ]
