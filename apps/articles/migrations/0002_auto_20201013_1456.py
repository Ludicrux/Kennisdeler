# Generated by Django 2.2 on 2020-10-13 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uploaded_file',
            field=models.FileField(blank=True, upload_to='documents/article-documents', verbose_name='articledoc'),
        ),
    ]
