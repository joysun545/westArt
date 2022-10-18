# Generated by Django 2.2.24 on 2022-05-29 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='ArtFieldInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=12, verbose_name='艺术类型')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标题')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], null=True, verbose_name='性别')),
                ('birth_time', models.CharField(max_length=12, null=True, verbose_name='出生时间')),
                ('birth_place', models.CharField(max_length=64, null=True, verbose_name='出生地')),
                ('art_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.ArtFieldInfo', verbose_name='艺术领域')),
            ],
        ),
        migrations.CreateModel(
            name='MuseumInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='博物馆名称')),
                ('country', models.CharField(max_length=16, verbose_name='博物馆所在国家')),
                ('city', models.CharField(max_length=32, verbose_name='博物馆所在城市')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools', models.CharField(max_length=32, verbose_name='流派')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.IntegerField(max_length=4, verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='CreationTypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_type', models.CharField(max_length=16, verbose_name='创作形式')),
                ('art_field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.ArtFieldInfo', verbose_name='艺术领域')),
            ],
        ),
        migrations.CreateModel(
            name='CompleteWorksInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='艺术品名称')),
                ('creation_time', models.CharField(max_length=32, verbose_name='创作时间')),
                ('art_creation_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.CreationTypeInfo', verbose_name='创作类型')),
                ('artist_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.ArtistInfo', verbose_name='艺术家姓名')),
                ('collection_museum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.MuseumInfo', verbose_name='收藏博物馆')),
            ],
        ),
        migrations.AddField(
            model_name='artistinfo',
            name='art_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artWorks.SchoolsInfo', verbose_name='艺术流派'),
        ),
    ]
