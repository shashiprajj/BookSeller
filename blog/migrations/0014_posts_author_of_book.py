# Generated by Django 3.1.1 on 2020-10-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_pdfs'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Author_of_book',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
