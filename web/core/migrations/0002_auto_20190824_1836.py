# Generated by Django 2.2.4 on 2019-08-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfe',
            name='xml',
            field=models.CharField(max_length=50000, verbose_name='XML'),
        ),
    ]