# Generated by Django 3.2.12 on 2022-08-09 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20220804_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='tag',
            new_name='name',
        ),
    ]
