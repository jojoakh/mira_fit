# Generated by Django 5.1.6 on 2025-02-28 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='plan.plan'),
        ),
    ]
