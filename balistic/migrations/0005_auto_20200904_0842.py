# Generated by Django 3.0.4 on 2020-09-04 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balistic', '0004_ballisticreport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ballisticreport',
            options={'verbose_name': 'Ballistic Report', 'verbose_name_plural': 'Ballistic Reports'},
        ),
        migrations.AlterField(
            model_name='ballisticreport',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='balistic.Ballistic', verbose_name='case'),
        ),
    ]
