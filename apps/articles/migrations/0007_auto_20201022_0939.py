# Generated by Django 2.2 on 2020-10-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20201015_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_public',
            field=models.BooleanField(choices=[(1, 'Iedereen mag dit zien'), (0, 'Alleen voor leden op dit platform')], default=True),
        ),
    ]
