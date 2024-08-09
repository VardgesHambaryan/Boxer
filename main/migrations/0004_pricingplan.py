# Generated by Django 5.1 on 2024-08-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Plan Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
            ],
        ),
    ]
