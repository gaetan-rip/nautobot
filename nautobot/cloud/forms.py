from django import forms

from nautobot.cloud.models import CloudAccount
from nautobot.core.constants import CHARFIELD_MAX_LENGTH
from nautobot.core.forms import (
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    MultiValueCharField,
    TagFilterField,
)
from nautobot.dcim.models import Manufacturer
from nautobot.extras.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin
from nautobot.extras.models import SecretsGroup

#
# Cloud Account
#


class CloudAccountForm(NautobotModelForm):
    provider = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        help_text="Manufacturers are the recommended model to represent cloud providers.",
    )
    secrets_group = DynamicModelChoiceField(queryset=SecretsGroup.objects.all())

    class Meta:
        model = CloudAccount
        fields = [
            "account_number",
            "name",
            "description",
            "provider",
            "secrets_group",
            "tags",
        ]


class CloudAccountBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=CloudAccount.objects.all(), widget=forms.MultipleHiddenInput)
    secrets_group = DynamicModelChoiceField(queryset=SecretsGroup.objects.all(), required=False)
    provider = DynamicModelChoiceField(queryset=Manufacturer.objects.all(), required=False)
    description = forms.CharField(max_length=CHARFIELD_MAX_LENGTH, required=False)

    class Meta:
        nullable_fields = [
            "secrets_group",
            "description",
        ]


class CloudAccountFilterForm(NautobotFilterForm):
    model = CloudAccount
    field_order = [
        "q",
        "account_number",
        "name",
        "provider",
        "secrets_group",
        "tags",
    ]
    q = forms.CharField(required=False, label="Search")
    name = MultiValueCharField(required=False)
    account_number = MultiValueCharField(required=False)
    secrets_group = DynamicModelMultipleChoiceField(
        queryset=SecretsGroup.objects.all(), to_field_name="name", required=False
    )
    provider = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(), to_field_name="name", required=False
    )
    tags = TagFilterField(model)
