# Generated by Django 3.0.4 on 2020-09-14 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('balistic', '0006_auto_20200914_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballisticreport',
            name='approved',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer_approval', to=settings.AUTH_USER_MODEL, verbose_name='approved by'),
        ),
        migrations.AlterField(
            model_name='ballisticreport',
            name='reported_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='officer_report', to=settings.AUTH_USER_MODEL, verbose_name='reported by'),
        ),
    ]
