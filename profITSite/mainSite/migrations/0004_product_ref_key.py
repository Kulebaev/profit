# Generated by Django 4.2.4 on 2023-09-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ref_key',
            field=models.CharField(default='default_ref_key', max_length=255, verbose_name='Внешний код'),
        ),
    ]