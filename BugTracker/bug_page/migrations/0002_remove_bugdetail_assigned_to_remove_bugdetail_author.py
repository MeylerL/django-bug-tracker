# Generated by Django 4.1.5 on 2023-01-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bug_page", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bugdetail",
            name="assigned_to",
        ),
        migrations.RemoveField(
            model_name="bugdetail",
            name="author",
        ),
    ]