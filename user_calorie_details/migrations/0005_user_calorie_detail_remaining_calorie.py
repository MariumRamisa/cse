# Generated by Django 4.1.3 on 2022-12-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_calorie_details', '0004_alter_user_calorie_detail_calorie_intake'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_calorie_detail',
            name='remaining_calorie',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]