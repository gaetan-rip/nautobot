# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 20:10
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0020_ipaddress_add_role_carp'),
        ('dcim', '0049_rackreservation_change_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='mode',
            field=models.PositiveSmallIntegerField(blank=True, choices=[[100, 'Access'], [200, 'Tagged'], [300, 'Tagged All']], null=True),
        ),
        migrations.AddField(
            model_name='interface',
            name='tagged_vlans',
            field=models.ManyToManyField(blank=True, related_name='interfaces_as_tagged', to='ipam.VLAN', verbose_name='Tagged VLANs'),
        ),
        migrations.AddField(
            model_name='interface',
            name='untagged_vlan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interfaces_as_untagged', to='ipam.VLAN', verbose_name='Untagged VLAN'),
        ),
    ]