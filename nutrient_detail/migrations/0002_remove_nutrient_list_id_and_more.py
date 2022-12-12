# Generated by Django 4.1.3 on 2022-12-12 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_foodcalories_quantity'),
        ('nutrient_detail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrient_list',
            name='id',
        ),
        migrations.AlterField(
            model_name='nutrient_list',
            name='food_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='food.foodcalories'),
        ),
    ]