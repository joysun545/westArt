# Generated by Django 2.2.24 on 2022-05-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0005_auto_20220530_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True, verbose_name='年龄'),
        ),
    ]
