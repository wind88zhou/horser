# Generated by Django 3.0.8 on 2020-07-04 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interface_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name', models.CharField(max_length=20, verbose_name='接口名')),
                ('interface_type', models.CharField(max_length=20, verbose_name='接口类型')),
                ('input_fileld_list', models.CharField(max_length=200, verbose_name='输入字段列表')),
                ('input_fileld_type_list', models.CharField(max_length=200, verbose_name='输入字段类型列表')),
                ('assert_filed_list', models.CharField(max_length=200, verbose_name='断言字段列表')),
                ('assert_filed_type_list', models.CharField(max_length=200, verbose_name='断言类型列表')),
                ('match_list', models.CharField(max_length=200, verbose_name='匹配内容列表')),
                ('assert_result_list', models.CharField(max_length=200, verbose_name='断言结果列表')),
                ('belong_subsys', models.CharField(max_length=20, verbose_name='所属子系统')),
                ('belong_git_base', models.CharField(blank=True, max_length=100, verbose_name='所属git代码库')),
                ('belong_svn_base', models.CharField(blank=True, max_length=100, verbose_name='所属svn代码库')),
                ('created_time', models.DateTimeField(blank=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(blank=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '接口信息表',
                'ordering': ['-updated_time'],
            },
        ),
        migrations.CreateModel(
            name='User_Group_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_brief', models.CharField(max_length=50, verbose_name='组简介')),
            ],
            options={
                'verbose_name': '用户组表',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, verbose_name='用户名')),
                ('user_role', models.CharField(max_length=20, verbose_name='用户角色')),
                ('password', models.CharField(max_length=20, verbose_name='用户密码')),
            ],
            options={
                'verbose_name': '用户表',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User_Group_Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horsequick.User_Group_Info', verbose_name='所属组id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horsequick.User_Info', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '用户与组关系表',
                'ordering': ['-id'],
            },
        ),
    ]
