# Generated by Django 2.2.24 on 2021-11-12 16:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contents",
            new_name="Content",
        ),
    ]
