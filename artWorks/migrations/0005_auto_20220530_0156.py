# Generated by Django 2.2.24 on 2022-05-30 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0004_userinfo_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='username',
        ),
    ]
