# Generated by Django 3.0.8 on 2020-07-19 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200719_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='description_long',
        ),
    ]
