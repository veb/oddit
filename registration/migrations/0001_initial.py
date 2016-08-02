# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=224, verbose_name='activation key')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
        ),
    ]
