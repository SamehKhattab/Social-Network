# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofilemanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]
