# Generated by Django 4.0.2 on 2022-02-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0003_tag_brand_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='소개'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(upload_to='brand/', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='info',
            field=models.TextField(verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='link',
            field=models.URLField(verbose_name='링크'),
        ),
    ]
