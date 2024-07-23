<!-- markdownlint-disable MD024 -->

# Nautobot v2.3

This document describes all new features and changes in Nautobot 2.3.

## Release Overview

### Added

#### Added an Optional `role` field to Interface and VMInterface models ([#4406](https://github.com/nautobot/nautobot/issues/4406))

Added an optional `role` field to Interface and VMInterface models to track common interface configurations. Now the users can create [Role](../user-guide/platform-functionality/role.md) instances that can be assigned to [interfaces](../user-guide/core-data-model/dcim/interface.md) and [vminterfaces](../user-guide/core-data-model/virtualization/vminterface.md).

#### Cloud Models ([#5716](https://github.com/nautobot/nautobot/issues/5716), [#5719](https://github.com/nautobot/nautobot/issues/5719), [#5721](https://github.com/nautobot/nautobot/issues/5721), [#5872](https://github.com/nautobot/nautobot/issues/5872))

Added the new models `CloudAccount`, `CloudResourceType`, `CloudNetwork`, and `CloudService` to support recording of cloud provider accounts (AWS, Azure, GCP, DigitalOcean, etc.), cloud resource types (AWS EC2, Azure Virtual Machine Service, Google App Engine, etc.), cloud services (specific instances of services described by cloud resource types) and cloud network objects (such as VPCs) in Nautobot.

#### Dynamic Group Enhancements

Dynamic Groups now have a `group_type` field, which specifies whether this group is defined by an object filter, defined by aggregating other groups via set operations, or defined via static assignment of objects as group members (this third type is new in Nautobot 2.3). Additionally, you can now assign a tenant and/or tags to each Dynamic Group.

A new model, `StaticGroupAssociation`, and associated REST API, have been added in support of the new "static" group type. See also "[Dynamic Group Cache Changes](#dynamic-group-cache-changes)" below.

For more details, refer to the [Dynamic Group](../user-guide/platform-functionality/dynamicgroup.md) documentation.

#### Object Metadata Models ([#5663](https://github.com/nautobot/nautobot/issues/5663))

Added [a set of functionality](../user-guide/platform-functionality/metadata.md) for defining and managing object metadata, that is to say, data _about_ the network data managed in Nautobot, such as data provenance, data ownership, and data classification. For more details, refer to the linked documentation.

#### Saved Views

Added the ability for users to save multiple configurations of list views (table columns, filtering, pagination and sorting) for ease of later use and reuse. Refer to the [Saved View](../user-guide/platform-functionality/savedview.md) documentation for more details and on how to use saved views.

### Changed

#### Dynamic Group Cache Changes

To improve performance of the Dynamic Groups feature, a number of changes have been made:

- Dynamic Groups now always use `StaticGroupAssociation` records as a database cache of their member objects, rather than optionally caching their members in Redis for a limited time period. For Dynamic Groups of types other than the new "static" group type, these `StaticGroupAssociation` records are hidden by default from the UI and REST API.
- The `DYNAMIC_GROUPS_MEMBER_CACHE_TIMEOUT` setting variable is deprecated, as it no longer influences Dynamic Group cache behavior.
- The APIs `DynamicGroup.members`, `DynamicGroup.count`, `DynamicGroup.has_member()`, and `object.dynamic_groups` now always use the database cache rather than being recalculated on the fly.
- The APIs `DynamicGroup.members_cached`, `DynamicGroup.members_cache_key`, `object.dynamic_groups_cached`, `object.dynamic_groups_list`, and `object.dynamic_groups_list_cached` are now deprecated.
- Editing a Dynamic Group definition refreshes its cached members and those of any "parent" groups that use it.
- Viewing a Dynamic Group detail view in the UI refreshes its cached members (only).
- A new System Job, `Refresh Dynamic Group Caches`, can be run or scheduled as apprropriate to refresh Dynamic Group member caches on demand.
- The existing API `DynamicGroup.update_cached_members()` can be called by Apps or Jobs needing to ensure that the cache is up-to-date for any given Dynamic Group.

#### Updated to Django 4.2

As Django 3.2 has reached end-of-life, Nautobot 2.3 requires Django 4.2, the next long-term-support (LTS) version of Django. There are a number of changes in Django itself as a result of this upgrade; Nautobot App maintainers are urged to review the Django release-notes ([4.0](https://docs.djangoproject.com/en/4.2/releases/4.0/), [4.1](https://docs.djangoproject.com/en/4.2/releases/4.1/), [4.2](https://docs.djangoproject.com/en/4.2/releases/4.2/)), especially the relevant "Backwards incompatible changes" sections, to proactively identify any impact to their Apps.

#### Log Cleanup as System Job ([#3749](https://github.com/nautobot/nautobot/issues/3749))

Cleanup of the change log (deletion of `ObjectChange` records older than a given cutoff) is now handled by the new `LogsCleanup` system Job, rather than occurring at random as a side effect of new change log records being created. Admins desiring automatic cleanup are encouraged to schedule this job to run at an appropriate interval suitable to your deployment's needs.

!!! info
    Setting [`CHANGELOG_RETENTION`](../user-guide/administration/configuration/optional-settings.md#changelog_retention) in your Nautobot configuration by itself no longer directly results in periodic cleanup of `ObjectChange` records. You must run (or schedule to periodically run) the `LogsCleanup` Job for this to occur.

As an additional enhancement, the `LogsCleanup` Job can also be used to cleanup `JobResult` records if desired as well.

<!-- towncrier release notes start -->