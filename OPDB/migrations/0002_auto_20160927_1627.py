# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OPDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_decription',
            field=models.TextField(default=b'Briefly decribe what is in the photo'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_name',
            field=models.CharField(default=b'ImageName', max_length=50),
        ),
    ]
