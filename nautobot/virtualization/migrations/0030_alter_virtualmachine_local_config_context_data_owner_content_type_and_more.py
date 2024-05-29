# Generated by Django 4.2.9 on 2024-01-17 18:52

from django.db import migrations
import django.db.models.deletion

import nautobot.core.models.fields
import nautobot.extras.models.roles
import nautobot.extras.models.statuses
import nautobot.extras.utils


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0108_alter_configcontext_cluster_groups_and_more"),
        ("virtualization", "0029_add_role_field_to_interface_models"),
    ]

    operations = [
        migrations.AlterField(
            model_name="virtualmachine",
            name="local_config_context_data_owner_content_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="virtualmachine",
            name="local_config_context_schema",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="extras.configcontextschema"
            ),
        ),
        migrations.AlterField(
            model_name="virtualmachine",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.role"
            ),
        ),
        migrations.AlterField(
            model_name="virtualmachine",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
        migrations.AlterField(
            model_name="vminterface",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="extras.role"
            ),
        ),
        migrations.AlterField(
            model_name="vminterface",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, to="extras.status"
            ),
        ),
    ]
