# Generated by Django 2.2.24 on 2022-05-31 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artWorks', '0015_auto_20220531_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolsinfo',
            name='artcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.ArtCategoryInfo', verbose_name='艺术门类'),
        ),
    ]
