# Generated by Django 2.1 on 2018-09-14 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shufic', '0002_video_video_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Video_date',
            field=models.DateTimeField(),
        ),
    ]
