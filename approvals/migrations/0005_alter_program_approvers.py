# Generated by Django 3.2.18 on 2023-03-08 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approvals', '0004_auto_20230307_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='approvers',
            field=models.ManyToManyField(related_name='programs', to=settings.AUTH_USER_MODEL),
        ),
    ]
