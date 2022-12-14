# Generated by Django 2.2.24 on 2022-05-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0014_remove_completeworksinfo_sharer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistinfo',
            old_name='art_field',
            new_name='artrategory',
        ),
        migrations.RenameField(
            model_name='artistinfo',
            old_name='art_school',
            new_name='artschool',
        ),
        migrations.RenameField(
            model_name='artistinfo',
            old_name='birth_place',
            new_name='birthplace',
        ),
        migrations.RenameField(
            model_name='artistinfo',
            old_name='birth_time',
            new_name='birthtime',
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]
