# Generated by Django 2.2 on 2020-10-15 14:56

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201015_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[300, 300], upload_to='images/subject-images'),
        ),
    ]
