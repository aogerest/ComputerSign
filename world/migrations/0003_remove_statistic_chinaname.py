# Generated by Django 5.0.4 on 2024-05-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_statistic_matchsum_statistic_valid_passing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='chinaname',
        ),
    ]
