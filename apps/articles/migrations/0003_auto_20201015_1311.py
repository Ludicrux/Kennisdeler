# Generated by Django 2.2 on 2020-10-15 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201013_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Favoriet', 'verbose_name_plural': 'Favorieten'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Opleiding', 'verbose_name_plural': 'Opleidingen'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
