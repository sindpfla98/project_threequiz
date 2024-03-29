# Generated by Django 2.2.1 on 2019-11-02 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='일시')),
                ('exp', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600)], verbose_name='경험치')),
                ('delivery', models.CharField(blank=True, choices=[('배송 중', '배송 중'), ('배송 완료', '배송 완료')], max_length=10, null=True, verbose_name='배달현황')),
            ],
            options={
                'verbose_name': '작물',
                'verbose_name_plural': '작물일지',
            },
        ),
        migrations.CreateModel(
            name='Growth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='상태명')),
            ],
            options={
                'verbose_name': '생육상태',
                'verbose_name_plural': '생육상태',
            },
        ),
        migrations.CreateModel(
            name='PlantState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=10, verbose_name='상태')),
                ('change', models.CharField(choices=[('+', '증가'), ('-', '감소')], max_length=5, verbose_name='증감구분')),
                ('change_exp', models.IntegerField(verbose_name='증감경험치')),
            ],
            options={
                'verbose_name': '작물상태',
                'verbose_name_plural': '작물상태',
            },
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='씨앗명')),
                ('photo', models.ImageField(upload_to='seed/', verbose_name='사진')),
                ('desc', models.TextField(max_length=300, verbose_name='설명')),
            ],
            options={
                'verbose_name': '씨앗',
                'verbose_name_plural': '씨앗정보',
            },
        ),
        migrations.CreateModel(
            name='SeedState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='seedState/', verbose_name='사진')),
            ],
            options={
                'verbose_name': '씨앗상태',
                'verbose_name_plural': '씨앗상태',
            },
        ),
        migrations.CreateModel(
            name='UserWeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '회원잡초',
                'verbose_name_plural': '회원잡초',
            },
        ),
        migrations.CreateModel(
            name='Weeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='weeds/', verbose_name='사진')),
            ],
            options={
                'verbose_name': '잡초',
                'verbose_name_plural': '잡초',
            },
        ),
    ]
