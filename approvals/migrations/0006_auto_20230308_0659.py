# Generated by Django 3.2.18 on 2023-03-08 06:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approvals', '0005_alter_program_approvers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='approvers',
            new_name='default_approvers',
        ),
        migrations.AddField(
            model_name='program',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
