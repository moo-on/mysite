# Generated by Django 3.1.3 on 2021-04-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20210414_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
