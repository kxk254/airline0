# Generated by Django 5.0.7 on 2024-07-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
