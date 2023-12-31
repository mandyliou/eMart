# Generated by Django 4.2.5 on 2023-10-03 05:58

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_remove_product_stripe_price_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductAttachment",
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
                (
                    "file",
                    models.FileField(
                        storage=django.core.files.storage.FileSystemStorage(
                            location="/Users/mandyliou/dev/micro-ecommerce/local_cdn/protected"
                        ),
                        upload_to=products.models.handle_product_attachment_upload,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                ("is_free", models.BooleanField(default=False)),
                ("active", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
