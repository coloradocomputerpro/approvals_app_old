# Generated by Django 3.2.18 on 2023-03-07 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('approvals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('end_client', 'End Client'), ('systems_integrator', 'Systems Integrator'), ('gov_body', 'Government Body'), ('vendor_pm', 'Vendor PM'), ('vendor_dev', 'Vendor Developer'), ('vendor_adm', 'Vendor Administrator')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='approvers',
            field=models.ManyToManyField(blank=True, to='approvals.Approver'),
        ),
    ]