# Generated by Django 4.1.2 on 2022-11-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_author_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]