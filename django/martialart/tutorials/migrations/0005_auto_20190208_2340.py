# Generated by Django 2.1.5 on 2019-02-08 18:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20190208_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
