# Generated by Django 3.1.1 on 2020-10-09 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_posts_author_of_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdfs',
            old_name='pdf_name',
            new_name='EBook_name',
        ),
        migrations.RenameField(
            model_name='pdfs',
            old_name='pdf_file',
            new_name='Upload_EBook',
        ),
    ]