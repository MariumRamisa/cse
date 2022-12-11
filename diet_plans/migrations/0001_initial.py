# Generated by Django 4.1.3 on 2022-11-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diet_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('diet_plan', models.CharField(max_length=200)),
            ],
        ),
    ]
