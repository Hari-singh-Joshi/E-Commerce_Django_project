# Generated by Django 5.1.1 on 2024-09-09 05:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Product_image",
            new_name="product_image",
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("mobile", models.IntegerField(default=0)),
                ("zipcode", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AndhraPradesh", "AndhraPradesh"),
                            ("ArunachalPradesh", "ArunachalPradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Chhattisgarh", "Chhattisgarh"),
                            ("Goa", "Goa"),
                            ("Gujarat", "Gujarat"),
                            ("Haryana", "Haryana"),
                            ("HimachalPradesh", "HimachalPradesh"),
                            ("Jharkhand", "Jharkhand"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("MadhyaPradesh", "MadhyaPradesh"),
                            ("Maharashtra", "Maharashtra"),
                            ("Manipur", "Manipur"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Nagaland", "Nagaland"),
                            ("Odisha", "Odisha"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Sikkim", "Sikkim"),
                            ("TamilNadu", "TamilNadu"),
                            ("Telangana", "Telangana"),
                            ("Tripura", "Tripura"),
                            ("UttarPradesh", "UttarPradesh"),
                            ("Uttarakhand", "Uttarakhand"),
                            ("WestBengal", "WestBengal"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
