# Generated by Django 3.0.5 on 2021-03-27 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("user", "user"),
                    ("moderator", "moderator"),
                    ("admin", "admin"),
                ],
                default="user",
                max_length=20,
            ),
        ),
    ]
