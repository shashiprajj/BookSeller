# Generated by Django 3.1.1 on 2020-10-08 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201008_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='pdf_name',
        ),
    ]