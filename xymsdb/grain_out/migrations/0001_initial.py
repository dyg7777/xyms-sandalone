# Generated by Django 4.2.7 on 2023-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcquisitionVarieties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AV_name', models.CharField(default='玉米', help_text='发货品种', max_length=255, null=True, unique=True)),
                ('find_code', models.CharField(default='', help_text='查询编码', max_length=255, null=True, unique=True)),
                ('py_abbreviation', models.CharField(default='', help_text='拼音简写', max_length=255, null=True)),
                ('acquisitioncaps', models.DecimalField(decimal_places=4, help_text='发货上限', max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerForGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerforgoods_name', models.CharField(default='企业私有', help_text='货权人名称', max_length=255, null=True, unique=True)),
                ('ownerforgoods_uncode', models.CharField(default='', help_text='货权人代码', max_length=100, null=True)),
                ('ownerforgoods_phonenumber', models.CharField(default='', help_text='货权人联系方式', max_length=100, null=True)),
                ('co_owners', models.CharField(help_text='货物共有人', max_length=255, null=True)),
            ],
        ),
    ]
