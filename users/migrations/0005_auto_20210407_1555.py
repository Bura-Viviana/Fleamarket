# Generated by Django 3.1.7 on 2021-04-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210407_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='state',
            field=models.CharField(default='prcossesing', max_length=250),
        ),
    ]