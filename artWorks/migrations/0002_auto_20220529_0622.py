# Generated by Django 2.2.24 on 2022-05-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(max_length=12, verbose_name='年龄'),
        ),
    ]
