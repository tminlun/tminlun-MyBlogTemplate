# Generated by Django 2.0 on 2018-10-13 04:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20181012_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容'),
        ),
    ]
