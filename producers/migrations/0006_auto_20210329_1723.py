# Generated by Django 3.1.7 on 2021-03-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0005_auto_20210329_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='picture',
            field=models.ImageField(default='producers/default.jpg', upload_to='producers'),
        ),
    ]
