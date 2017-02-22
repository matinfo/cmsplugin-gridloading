# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_gridloading', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gridloadingitemplugin',
            name='link_text',
        ),
    ]
