# Generated by Django 5.1.6 on 2025-02-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_review_plan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
