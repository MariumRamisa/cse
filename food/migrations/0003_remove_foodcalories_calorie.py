# Generated by Django 4.1.3 on 2022-12-21 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_foodcalories_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodcalories',
            name='calorie',
        ),
    ]
