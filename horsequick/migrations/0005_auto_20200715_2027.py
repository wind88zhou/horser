# Generated by Django 3.0.8 on 2020-07-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horsequick', '0004_auto_20200715_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface_info',
            name='input_demo_list',
            field=models.CharField(max_length=200, null=True, verbose_name='输入字段实例列表'),
        ),
        migrations.AddField(
            model_name='interface_info',
            name='input_need_list',
            field=models.CharField(max_length=200, null=True, verbose_name='输入字段必需列表'),
        ),
    ]
