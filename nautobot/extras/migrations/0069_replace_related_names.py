# Generated by Django 3.2.16 on 2023-02-08 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.utils


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0068_remove_site_and_region_attributes_from_config_context"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computedfield",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=nautobot.extras.utils.FeatureQuery("custom_fields"),
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computed_fields",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="configcontext",
            name="owner_content_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="config_contexts",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="configcontext",
            name="schema",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="config_contexts",
                to="extras.configcontextschema",
            ),
        ),
        migrations.AlterField(
            model_name="configcontextschema",
            name="owner_content_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                limit_choices_to=nautobot.extras.utils.FeatureQuery("config_context_owners"),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="config_context_schemas",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="customfieldchoice",
            name="field",
            field=models.ForeignKey(
                limit_choices_to=models.Q(("type__in", ["select", "multi-select"])),
                on_delete=django.db.models.deletion.CASCADE,
                related_name="custom_field_choices",
                to="extras.customfield",
            ),
        ),
        migrations.AlterField(
            model_name="customlink",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=nautobot.extras.utils.FeatureQuery("custom_links"),
                on_delete=django.db.models.deletion.CASCADE,
                related_name="custom_links",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="dynamicgroup",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dynamic_groups",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="exporttemplate",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to=nautobot.extras.utils.FeatureQuery("export_templates"),
                on_delete=django.db.models.deletion.CASCADE,
                related_name="export_templates",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="gitrepository",
            name="secrets_group",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="git_repositories",
                to="extras.secretsgroup",
            ),
        ),
        migrations.AlterField(
            model_name="imageattachment",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image_attachments",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="jobhook",
            name="job",
            field=models.ForeignKey(
                limit_choices_to={"is_job_hook_receiver": True},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_hooks",
                to="extras.job",
            ),
        ),
        migrations.AlterField(
            model_name="joblogentry",
            name="job_result",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="job_log_entries", to="extras.jobresult"
            ),
        ),
        migrations.AlterField(
            model_name="jobresult",
            name="job_model",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="job_results",
                to="extras.job",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="assigned_object_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="notes", to="contenttypes.contenttype"
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="notes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="objectchange",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="object_changes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="relationshipassociation",
            name="relationship",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="relationship_associations",
                to="extras.relationship",
            ),
        ),
        migrations.AlterField(
            model_name="secretsgroup",
            name="secrets",
            field=models.ManyToManyField(
                blank=True, related_name="secrets_groups", through="extras.SecretsGroupAssociation", to="extras.Secret"
            ),
        ),
        migrations.AlterField(
            model_name="secretsgroupassociation",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="secrets_group_associations",
                to="extras.secretsgroup",
            ),
        ),
        migrations.AlterField(
            model_name="secretsgroupassociation",
            name="secret",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="secrets_group_associations",
                to="extras.secret",
            ),
        ),
    ]