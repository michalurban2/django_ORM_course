# Generated by Django 4.1.6 on 2023-02-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_category_alter_product_options_remove_brand_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="brand_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=50, verbose_name="brand name"),
        ),
    ]
