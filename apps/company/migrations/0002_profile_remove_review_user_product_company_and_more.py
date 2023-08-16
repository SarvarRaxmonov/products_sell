# Generated by Django 4.2.1 on 2023-08-16 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("username", models.CharField(max_length=500)),
                ("image", models.ImageField(upload_to="profile_images/")),
            ],
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
        migrations.AddField(
            model_name="product",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="company.company",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="review",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_company",
                to="company.company",
            ),
        ),
    ]
