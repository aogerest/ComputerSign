# Generated by Django 5.0.4 on 2024-05-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_remove_statistic_chinaname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='player_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='球员ID'),
        ),
    ]
