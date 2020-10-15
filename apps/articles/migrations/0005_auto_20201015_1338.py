# Generated by Django 2.2 on 2020-10-15 13:38

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201015_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[1000, 500], upload_to='images/article-images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, size=[40, 40], upload_to='images/article-thumbnail'),
        ),
    ]