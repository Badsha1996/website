# Generated by Django 2.1.5 on 2019-02-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_tutorial_vid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='vid',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='thumb',
            field=models.ImageField(blank=True, default='b.png', upload_to=''),
        ),
    ]