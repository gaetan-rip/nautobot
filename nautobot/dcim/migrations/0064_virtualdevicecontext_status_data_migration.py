from django.db import migrations

from nautobot.extras.management import clear_status_choices, populate_status_choices


def populate_virtual_device_context_status(apps, schema_editor):
    """
    Create default Status records for the VirtualDeviceContext content-type.
    """
    # Create VirtualDeviceContext Statuses and add dcim.VirtualDeviceContext to its content_types
    populate_status_choices(apps, schema_editor, models=["dcim.VirtualDeviceContext"])


def clear_virtual_device_context_status(apps, schema_editor):
    """
    Clear the status field on all VirtualDeviceContext, and de-link/delete all Status records from the VirtualDeviceContext content-type.
    """
    VirtualDeviceContext = apps.get_model("dcim.VirtualDeviceContext")

    for vdc in VirtualDeviceContext.objects.filter(status__isnull=False):
        vdc.status = None
        vdc.save()

    clear_status_choices(apps, schema_editor, models=["dcim.VirtualDeviceContext"])


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0063_virtualdevicecontext_interface_vdcs"),
    ]

    operations = [
        migrations.RunPython(populate_virtual_device_context_status, clear_virtual_device_context_status),
    ]