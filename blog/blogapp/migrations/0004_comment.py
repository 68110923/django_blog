# Generated by Django 2.1.4 on 2020-04-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200423_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发布')),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Article')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.User')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
