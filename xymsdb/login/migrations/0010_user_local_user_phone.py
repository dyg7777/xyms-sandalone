# Generated by Django 4.2.7 on 2024-01-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_remove_user_local_enter_name_user_local_enter_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_local',
            name='user_phone',
            field=models.CharField(blank=True, default='xykc@xy2cn.cn', help_text='用户电子信箱', max_length=30, null=True),
        ),
    ]
