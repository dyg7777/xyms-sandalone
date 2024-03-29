# Generated by Django 4.2.7 on 2023-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabasePath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, default='127.0.0.1', help_text='数据库连接地址', max_length=255, null=True)),
                ('port', models.CharField(blank=True, default='3306', help_text='数据库端口号', max_length=255, null=True)),
                ('db_name', models.CharField(blank=True, default='xyms_db', help_text='数据库名', max_length=255, null=True)),
                ('user_name', models.CharField(blank=True, default='root', help_text='用户名', max_length=255, null=True)),
                ('password', models.CharField(blank=True, default='53169549', help_text='密码', max_length=255, null=True)),
                ('charset', models.CharField(blank=True, default='utf-8', help_text='字符编码', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_name', models.CharField(default='', help_text='企业名称', max_length=255, unique=True)),
                ('enter_uncode', models.CharField(blank=True, default='', help_text='统一代码证号', max_length=255, null=True)),
                ('enter_author_start_date', models.DateTimeField(blank=True, help_text='授权开始时间', null=True)),
                ('enter_author_end_date', models.DateTimeField(blank=True, help_text='授权开始时间', null=True)),
                ('enter_code', models.CharField(blank=True, default='', help_text='企业码', max_length=255, null=True)),
                ('enter_author_code', models.CharField(blank=True, default='', help_text='授权码', max_length=255, null=True)),
                ('enter_free_credit', models.IntegerField(blank=True, default=50, help_text='授权额度', null=True)),
                ('version_number', models.CharField(blank=True, default='', help_text='版本号', max_length=255, null=True)),
                ('app_name', models.CharField(blank=True, default='', help_text='授权使用软件名称', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='login_logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_uuid', models.CharField(blank=True, default='', help_text='登录设备UUID每次更新', max_length=100, null=True)),
                ('login_time', models.DateTimeField(auto_now_add=True, help_text='登录时间')),
                ('logout_time', models.DateTimeField(auto_now_add=True, help_text='登出时间')),
                ('return_uuid', models.CharField(blank=True, default='', help_text='返回前端登录识别码', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgectPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectfile_path', models.CharField(blank=True, default='', help_text='程序工作目录', max_length=255, null=True, unique=True)),
                ('profiles_path', models.CharField(blank=True, default='', help_text='配置文件目录', max_length=255, null=True, unique=True)),
                ('tempfiles_path', models.CharField(blank=True, default='', help_text='临时文件目录', max_length=255, null=True, unique=True)),
                ('reportfile_path', models.CharField(blank=True, default='', help_text='报表文件目录', max_length=255, null=True, unique=True)),
                ('resourcefile_path', models.CharField(blank=True, default='', help_text='资源文件目录', max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RunDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_datetime', models.DateTimeField(help_text='系统执行时间')),
                ('real_datetime', models.DateTimeField(auto_now=True, help_text='本机时间')),
            ],
        ),
        migrations.CreateModel(
            name='User_local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='pbkdf2_sha256$600000$980513$AkfU8AiPz1H+nbPiK0qdc8doPY55C65ziluYKU5pAHE=', help_text='用户名', max_length=255, null=True, unique=True)),
                ('password', models.CharField(blank=True, default='pbkdf2_sha256$600000$1975217$cIG/fgs++BsR52DfcPKvrRRTVa/Z4/bvITlUlwxGdgM=', help_text='登录密码', max_length=255, null=True)),
                ('show_name', models.CharField(blank=True, default='鑫奕科创', help_text='用来显示用户名信息', max_length=255, null=True)),
                ('user_permissions', models.CharField(blank=True, default='0000', help_text='用户权限', max_length=50, null=True)),
                ('enter_name', models.CharField(blank=True, default='', help_text='账户所属企业名称', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions_code', models.CharField(blank=True, default='', help_text='权限ID', max_length=10, null=True)),
                ('permissions_name', models.CharField(blank=True, default='', help_text='权限名称', max_length=255, null=True, unique=True)),
            ],
        ),
    ]
