# Generated by Django 2.2.24 on 2022-05-31 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0016_schoolsinfo_artcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistinfo',
            name='artschool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.SchoolsInfo', verbose_name='艺术流派'),
        ),
    ]
