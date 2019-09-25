# Generated by Django 2.2.5 on 2019-09-19 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190919_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_publised',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 19, 23, 34, 46, 598909), verbose_name='date published'),
        ),
    ]
