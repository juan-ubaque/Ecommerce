# Generated by Django 4.1.7 on 2023-03-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name_categories',
            field=models.TextField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
