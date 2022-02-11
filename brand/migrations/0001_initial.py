# Generated by Django 4.0.2 on 2022-02-10 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='브랜드명')),
                ('desc', models.CharField(max_length=100, verbose_name='브랜드 소개')),
                ('info', models.TextField(verbose_name='브랜드 설명')),
                ('image', models.ImageField(upload_to='brand/', verbose_name='브랜드 이미지')),
                ('link', models.URLField(verbose_name='브랜드 링크')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='영문 카테고리명')),
                ('name_ko', models.CharField(max_length=20, verbose_name='국문 카테고리명')),
            ],
        ),
        migrations.CreateModel(
            name='BrandLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]
