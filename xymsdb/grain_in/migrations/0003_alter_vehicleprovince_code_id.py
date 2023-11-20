# Generated by Django 4.2.7 on 2023-11-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grain_in', '0002_alter_vehicleprovince_city_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleprovince',
            name='code_id',
            field=models.CharField(blank=True, default='', help_text='分类编号', max_length=10, null=True, unique=True),
        ),
    ]