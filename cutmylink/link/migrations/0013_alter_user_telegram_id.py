# Generated by Django 4.2 on 2023-04-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0012_alter_click_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(unique=True),
        ),
    ]