# Generated by Django 2.0 on 2017-12-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='text',
            field=models.TextField(),
        ),
    ]
