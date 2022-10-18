# Generated by Django 2.2.24 on 2022-06-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0020_auto_20220601_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='graduatedfrom',
            new_name='graduated',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=16, null=True, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(max_length=16, null=True, verbose_name='国家'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='saysomethingmore',
            field=models.TextField(max_length=280, null=True, verbose_name='再说点什么'),
        ),
    ]
