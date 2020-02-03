# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("api_v2", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_timestamp",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                ("update_timestamp", models.DateTimeField(auto_now=True, null=True)),
                ("type", models.TextField(null=True)),
                ("value", models.TextField(null=True)),
                (
                    "credential",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="api_v2.Credential",
                    ),
                ),
            ],
            options={"db_table": "category"},
        )
    ]