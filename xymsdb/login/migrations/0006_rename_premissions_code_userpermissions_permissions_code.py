# Generated by Django 4.2.7 on 2023-11-20 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_userpermissions_premissions_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpermissions',
            old_name='premissions_code',
            new_name='permissions_code',
        ),
    ]
