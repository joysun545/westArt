# Generated by Django 2.2.24 on 2022-05-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0011_auto_20220530_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creationtypeinfo',
            name='creationtype',
            field=models.CharField(max_length=16, verbose_name='创作类型'),
        ),
    ]
