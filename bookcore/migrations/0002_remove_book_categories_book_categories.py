# Generated by Django 4.1.4 on 2023-01-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='bookcore.category'),
        ),
    ]
