# Generated by Django 2.2 on 2020-10-12 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'], unique=True)),
                ('short_desc', models.CharField(max_length=120)),
                ('long_desc', models.TextField(blank=True, max_length=1500)),
                ('image', models.ImageField(upload_to='images/article-images', verbose_name='articleimg')),
                ('uploaded_file', models.FileField(upload_to='documents/article-documents', verbose_name='articledoc')),
                ('level', models.IntegerField(choices=[(1, 'Niveau 1'), (2, 'Niveau 2'), (3, 'Niveau 3'), (4, 'Niveau 4')], default=1)),
                ('file_type', models.CharField(choices=[('3DB', '3D-beeld'), ('ANI', 'Animaties'), ('DID', 'Didactische werkvorm'), ('GRO', '(Groeps)opdracht'), ('PRE', 'Presentatie'), ('TOE', 'Toets'), ('NVT', 'N.v.t.')], default='3DB', max_length=3)),
                ('is_public', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('downloads', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Artikel',
                'verbose_name_plural': 'Artikelen',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('image', models.ImageField(upload_to='images/subject-images/')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.Subject'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='articles.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', through='articles.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='user_favorites',
            field=models.ManyToManyField(blank=True, related_name='user_favorites', through='articles.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
