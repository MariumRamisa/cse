# Generated by Django 4.1.3 on 2022-12-04 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_food_intake_details', '0001_initial'),
        ('user_calorie_details', '0002_remove_user_calorie_detail_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_calorie_detail',
            name='remaining_calorie',
        ),
        migrations.AlterField(
            model_name='user_calorie_detail',
            name='calorie_intake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_food_intake_details.user_food_intake_detail'),
        ),
    ]
