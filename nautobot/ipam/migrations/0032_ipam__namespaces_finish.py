# Generated by Django 3.2.18 on 2023-05-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0031_ipam__prefix__add_parent"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vrf",
            unique_together={("namespace", "rd"), ("namespace", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="prefix",
            unique_together={("namespace", "network", "prefix_length")},
        ),
        migrations.AlterUniqueTogether(
            name="ipaddress",
            unique_together={("parent", "host")},
        ),
        migrations.RemoveField(
            model_name="ipaddress",
            name="vrf",
        ),
        migrations.RemoveField(
            model_name="prefix",
            name="vrf",
        ),
        migrations.RemoveField(
            model_name="vrf",
            name="enforce_unique",
        ),
        migrations.RenameField(
            model_name="vrf",
            old_name="prefixes_m2m",
            new_name="prefixes",
        ),
        migrations.AlterField(
            model_name="vrf",
            name="prefixes",
            field=models.ManyToManyField(related_name="vrfs", through="ipam.VRFPrefixAssignment", to="ipam.Prefix"),
        ),
    ]