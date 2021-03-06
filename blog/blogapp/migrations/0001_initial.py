# Generated by Django 2.1.4 on 2020-04-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField(max_length=15)),
                ('username', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=128)),
                ('sex', models.ImageField(choices=[(0, '女'), (1, '男'), (2, None)], default=2, upload_to='', verbose_name='性别')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
