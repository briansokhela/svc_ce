# Generated by Django 4.0.6 on 2023-02-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SVC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=7, null=True),
        ),
    ]
