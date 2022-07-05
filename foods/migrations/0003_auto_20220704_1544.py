# Generated by Django 3.2 on 2022-07-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='name_ch',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название на китайском'),
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название на английском'),
        ),
    ]