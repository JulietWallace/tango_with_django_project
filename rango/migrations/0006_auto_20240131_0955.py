# Generated by Django 2.2 on 2024-01-31 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_alter_category_options_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
