# Generated by Django 4.2.7 on 2023-12-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_user_local_password_alter_user_local_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_logs',
            name='login_user_id',
            field=models.CharField(blank=True, default='', help_text='登录的用户ID', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='login_logs',
            name='logout_time',
            field=models.DateTimeField(help_text='登出时间'),
        ),
    ]
