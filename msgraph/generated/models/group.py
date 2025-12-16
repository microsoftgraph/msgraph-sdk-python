from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_role_assignment import AppRoleAssignment
    from .assigned_label import AssignedLabel
    from .assigned_license import AssignedLicense
    from .calendar import Calendar
    from .conversation import Conversation
    from .conversation_thread import ConversationThread
    from .directory_object import DirectoryObject
    from .drive import Drive
    from .event import Event
    from .extension import Extension
    from .group_lifecycle_policy import GroupLifecyclePolicy
    from .group_setting import GroupSetting
    from .license_processing_state import LicenseProcessingState
    from .onenote import Onenote
    from .on_premises_provisioning_error import OnPremisesProvisioningError
    from .on_premises_sync_behavior import OnPremisesSyncBehavior
    from .planner_group import PlannerGroup
    from .profile_photo import ProfilePhoto
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .service_provisioning_error import ServiceProvisioningError
    from .site import Site
    from .team import Team

from .directory_object import DirectoryObject

@dataclass
class Group(DirectoryObject, Parsable):
    """
    Represents a Microsoft Entra group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.group"
    # The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post.
    accepted_senders: Optional[list[DirectoryObject]] = None
    # Indicates if people external to the organization can send messages to the group. The default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    allow_external_senders: Optional[bool] = None
    # Represents the app roles granted to a group for an application. Supports $expand.
    app_role_assignments: Optional[list[AppRoleAssignment]] = None
    # The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and a supported administrator role.
    assigned_labels: Optional[list[AssignedLabel]] = None
    # The licenses that are assigned to the group. Returned only on $select. Supports $filter (eq). Read-only.
    assigned_licenses: Optional[list[AssignedLicense]] = None
    # Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    auto_subscribe_new_members: Optional[bool] = None
    # The group's calendar. Read-only.
    calendar: Optional[Calendar] = None
    # The calendar view for the calendar. Read-only.
    calendar_view: Optional[list[Event]] = None
    # Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
    classification: Optional[str] = None
    # The group's conversations.
    conversations: Optional[list[Conversation]] = None
    # Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only.
    created_on_behalf_of: Optional[DirectoryObject] = None
    # An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    description: Optional[str] = None
    # The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # The group's default drive. Read-only.
    drive: Optional[Drive] = None
    # The group's drives. Read-only.
    drives: Optional[list[Drive]] = None
    # The group's calendar events.
    events: Optional[list[Event]] = None
    # Timestamp of when the group is set to expire. It's null for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the groupLifecyclePolicy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # The collection of open extensions defined for the group. Read-only. Nullable.
    extensions: Optional[list[Extension]] = None
    # The collection of lifecycle policies for this group. Read-only. Nullable.
    group_lifecycle_policies: Optional[list[GroupLifecyclePolicy]] = None
    # Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).
    group_types: Optional[list[str]] = None
    # Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example. Supports $filter (eq).
    has_members_with_license_errors: Optional[bool] = None
    # True if the group isn't displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. The default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    hide_from_address_lists: Optional[bool] = None
    # True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    hide_from_outlook_clients: Optional[bool] = None
    # When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the /group/{groupId}/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.
    is_archived: Optional[bool] = None
    # Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true, visibility must be Hidden, and the group can't be a dynamic group (that is, groupTypes can't contain DynamicMembership). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Microsoft Entra role assignmentsUsing this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports $filter (eq, ne, not).
    is_assignable_to_role: Optional[bool] = None
    # Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Returned only on $select.
    is_management_restricted: Optional[bool] = None
    # Indicates whether the signed-in user is subscribed to receive email conversations. The default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    is_subscribed_by_mail: Optional[bool] = None
    # Indicates the status of the group license assignment to all group members. The default value is false. Read-only. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete.Returned only on $select. Read-only.
    license_processing_state: Optional[LicenseProcessingState] = None
    # The SMTP address for the group, for example, 'serviceadmins@contoso.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    mail: Optional[str] = None
    # Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not).
    mail_enabled: Optional[bool] = None
    # The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following characters: @ () / [] ' ; : <> , SPACE. Required. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    mail_nickname: Optional[str] = None
    # Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.
    member_of: Optional[list[DirectoryObject]] = None
    # The members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).
    members: Optional[list[DirectoryObject]] = None
    # A list of group members with license errors from this group-based license assignment. Read-only.
    members_with_license_errors: Optional[list[DirectoryObject]] = None
    # The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
    membership_rule: Optional[str] = None
    # Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).
    membership_rule_processing_state: Optional[str] = None
    # Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.
    on_premises_domain_name: Optional[str] = None
    # Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in).
    on_premises_last_sync_date_time: Optional[datetime.datetime] = None
    # Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.
    on_premises_net_bios_name: Optional[str] = None
    # Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).
    on_premises_provisioning_errors: Optional[list[OnPremisesProvisioningError]] = None
    # Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.
    on_premises_sam_account_name: Optional[str] = None
    # Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports $filter (eq including on null values).
    on_premises_security_identifier: Optional[str] = None
    # The onPremisesSyncBehavior property
    on_premises_sync_behavior: Optional[OnPremisesSyncBehavior] = None
    # true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
    on_premises_sync_enabled: Optional[bool] = None
    # The onenote property
    onenote: Optional[Onenote] = None
    # The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner. A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related known issue. For security groups, the admin user isn't automatically added to this collection. For more information, see the related known issue. Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).
    owners: Optional[list[DirectoryObject]] = None
    # The permissionGrants property
    permission_grants: Optional[list[ResourceSpecificPermissionGrant]] = None
    # The group's profile photo
    photo: Optional[ProfilePhoto] = None
    # The profile photos owned by the group. Read-only. Nullable.
    photos: Optional[list[ProfilePhoto]] = None
    # Entry-point to Planner resource that might exist for a Unified Group.
    planner: Optional[PlannerGroup] = None
    # The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the Directory.ReadWrite.All permission and the user be assigned at least one of the following Microsoft Entra roles: User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.
    preferred_data_location: Optional[str] = None
    # The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    preferred_language: Optional[str] = None
    # Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
    proxy_addresses: Optional[list[str]] = None
    # The list of users or groups not allowed to create posts or calendar events in this group. Nullable
    rejected_senders: Optional[list[DirectoryObject]] = None
    # Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
    renewed_date_time: Optional[datetime.datetime] = None
    # Specifies whether the group is a security group. Required. Returned by default. Supports $filter (eq, ne, not, in).
    security_enabled: Optional[bool] = None
    # Security identifier of the group, used in Windows scenarios. Read-only. Returned by default.
    security_identifier: Optional[str] = None
    # Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports $filter (eq, not, for isResolved and serviceInstance).
    service_provisioning_errors: Optional[list[ServiceProvisioningError]] = None
    # Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable.
    settings: Optional[list[GroupSetting]] = None
    # The list of SharePoint sites in this group. Access the default site with /sites/root.
    sites: Optional[list[Site]] = None
    # The team associated with this group.
    team: Optional[Team] = None
    # Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange, or Red. Returned by default.
    theme: Optional[str] = None
    # The group's conversation threads. Nullable.
    threads: Optional[list[ConversationThread]] = None
    # The groups that a group is a member of, either directly or through nested membership. Nullable.
    transitive_member_of: Optional[list[DirectoryObject]] = None
    # The direct and transitive members of a group. Nullable.
    transitive_members: Optional[list[DirectoryObject]] = None
    # The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only.
    unique_name: Optional[str] = None
    # Count of conversations that received new posts since the signed-in user last visited the group. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).
    unseen_count: Optional[int] = None
    # Specifies the group join policy and group content visibility for groups. The possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as Private by default, and the Microsoft 365 group is Public. Groups assignable to roles are always Private. To learn more, see group visibility options. Returned by default. Nullable.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Group:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Group
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Group()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_role_assignment import AppRoleAssignment
        from .assigned_label import AssignedLabel
        from .assigned_license import AssignedLicense
        from .calendar import Calendar
        from .conversation import Conversation
        from .conversation_thread import ConversationThread
        from .directory_object import DirectoryObject
        from .drive import Drive
        from .event import Event
        from .extension import Extension
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_setting import GroupSetting
        from .license_processing_state import LicenseProcessingState
        from .onenote import Onenote
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .planner_group import PlannerGroup
        from .profile_photo import ProfilePhoto
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .service_provisioning_error import ServiceProvisioningError
        from .site import Site
        from .team import Team

        from .app_role_assignment import AppRoleAssignment
        from .assigned_label import AssignedLabel
        from .assigned_license import AssignedLicense
        from .calendar import Calendar
        from .conversation import Conversation
        from .conversation_thread import ConversationThread
        from .directory_object import DirectoryObject
        from .drive import Drive
        from .event import Event
        from .extension import Extension
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_setting import GroupSetting
        from .license_processing_state import LicenseProcessingState
        from .onenote import Onenote
        from .on_premises_provisioning_error import OnPremisesProvisioningError
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .planner_group import PlannerGroup
        from .profile_photo import ProfilePhoto
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .service_provisioning_error import ServiceProvisioningError
        from .site import Site
        from .team import Team

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedSenders": lambda n : setattr(self, 'accepted_senders', n.get_collection_of_object_values(DirectoryObject)),
            "allowExternalSenders": lambda n : setattr(self, 'allow_external_senders', n.get_bool_value()),
            "appRoleAssignments": lambda n : setattr(self, 'app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "assignedLabels": lambda n : setattr(self, 'assigned_labels', n.get_collection_of_object_values(AssignedLabel)),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(AssignedLicense)),
            "autoSubscribeNewMembers": lambda n : setattr(self, 'auto_subscribe_new_members', n.get_bool_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_object_value(Calendar)),
            "calendarView": lambda n : setattr(self, 'calendar_view', n.get_collection_of_object_values(Event)),
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "conversations": lambda n : setattr(self, 'conversations', n.get_collection_of_object_values(Conversation)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdOnBehalfOf": lambda n : setattr(self, 'created_on_behalf_of', n.get_object_value(DirectoryObject)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(Drive)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(Event)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "groupLifecyclePolicies": lambda n : setattr(self, 'group_lifecycle_policies', n.get_collection_of_object_values(GroupLifecyclePolicy)),
            "groupTypes": lambda n : setattr(self, 'group_types', n.get_collection_of_primitive_values(str)),
            "hasMembersWithLicenseErrors": lambda n : setattr(self, 'has_members_with_license_errors', n.get_bool_value()),
            "hideFromAddressLists": lambda n : setattr(self, 'hide_from_address_lists', n.get_bool_value()),
            "hideFromOutlookClients": lambda n : setattr(self, 'hide_from_outlook_clients', n.get_bool_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isAssignableToRole": lambda n : setattr(self, 'is_assignable_to_role', n.get_bool_value()),
            "isManagementRestricted": lambda n : setattr(self, 'is_management_restricted', n.get_bool_value()),
            "isSubscribedByMail": lambda n : setattr(self, 'is_subscribed_by_mail', n.get_bool_value()),
            "licenseProcessingState": lambda n : setattr(self, 'license_processing_state', n.get_object_value(LicenseProcessingState)),
            "mail": lambda n : setattr(self, 'mail', n.get_str_value()),
            "mailEnabled": lambda n : setattr(self, 'mail_enabled', n.get_bool_value()),
            "mailNickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "memberOf": lambda n : setattr(self, 'member_of', n.get_collection_of_object_values(DirectoryObject)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(DirectoryObject)),
            "membersWithLicenseErrors": lambda n : setattr(self, 'members_with_license_errors', n.get_collection_of_object_values(DirectoryObject)),
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "membershipRuleProcessingState": lambda n : setattr(self, 'membership_rule_processing_state', n.get_str_value()),
            "onPremisesDomainName": lambda n : setattr(self, 'on_premises_domain_name', n.get_str_value()),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesNetBiosName": lambda n : setattr(self, 'on_premises_net_bios_name', n.get_str_value()),
            "onPremisesProvisioningErrors": lambda n : setattr(self, 'on_premises_provisioning_errors', n.get_collection_of_object_values(OnPremisesProvisioningError)),
            "onPremisesSamAccountName": lambda n : setattr(self, 'on_premises_sam_account_name', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "onPremisesSyncBehavior": lambda n : setattr(self, 'on_premises_sync_behavior', n.get_object_value(OnPremisesSyncBehavior)),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(Onenote)),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(DirectoryObject)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(ResourceSpecificPermissionGrant)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(ProfilePhoto)),
            "photos": lambda n : setattr(self, 'photos', n.get_collection_of_object_values(ProfilePhoto)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(PlannerGroup)),
            "preferredDataLocation": lambda n : setattr(self, 'preferred_data_location', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "proxyAddresses": lambda n : setattr(self, 'proxy_addresses', n.get_collection_of_primitive_values(str)),
            "rejectedSenders": lambda n : setattr(self, 'rejected_senders', n.get_collection_of_object_values(DirectoryObject)),
            "renewedDateTime": lambda n : setattr(self, 'renewed_date_time', n.get_datetime_value()),
            "securityEnabled": lambda n : setattr(self, 'security_enabled', n.get_bool_value()),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
            "serviceProvisioningErrors": lambda n : setattr(self, 'service_provisioning_errors', n.get_collection_of_object_values(ServiceProvisioningError)),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(GroupSetting)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(Site)),
            "team": lambda n : setattr(self, 'team', n.get_object_value(Team)),
            "theme": lambda n : setattr(self, 'theme', n.get_str_value()),
            "threads": lambda n : setattr(self, 'threads', n.get_collection_of_object_values(ConversationThread)),
            "transitiveMemberOf": lambda n : setattr(self, 'transitive_member_of', n.get_collection_of_object_values(DirectoryObject)),
            "transitiveMembers": lambda n : setattr(self, 'transitive_members', n.get_collection_of_object_values(DirectoryObject)),
            "uniqueName": lambda n : setattr(self, 'unique_name', n.get_str_value()),
            "unseenCount": lambda n : setattr(self, 'unseen_count', n.get_int_value()),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("acceptedSenders", self.accepted_senders)
        writer.write_bool_value("allowExternalSenders", self.allow_external_senders)
        writer.write_collection_of_object_values("appRoleAssignments", self.app_role_assignments)
        writer.write_collection_of_object_values("assignedLabels", self.assigned_labels)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_bool_value("autoSubscribeNewMembers", self.auto_subscribe_new_members)
        writer.write_object_value("calendar", self.calendar)
        writer.write_collection_of_object_values("calendarView", self.calendar_view)
        writer.write_str_value("classification", self.classification)
        writer.write_collection_of_object_values("conversations", self.conversations)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("createdOnBehalfOf", self.created_on_behalf_of)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("groupLifecyclePolicies", self.group_lifecycle_policies)
        writer.write_collection_of_primitive_values("groupTypes", self.group_types)
        writer.write_bool_value("hasMembersWithLicenseErrors", self.has_members_with_license_errors)
        writer.write_bool_value("hideFromAddressLists", self.hide_from_address_lists)
        writer.write_bool_value("hideFromOutlookClients", self.hide_from_outlook_clients)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isAssignableToRole", self.is_assignable_to_role)
        writer.write_bool_value("isManagementRestricted", self.is_management_restricted)
        writer.write_bool_value("isSubscribedByMail", self.is_subscribed_by_mail)
        writer.write_object_value("licenseProcessingState", self.license_processing_state)
        writer.write_str_value("mail", self.mail)
        writer.write_bool_value("mailEnabled", self.mail_enabled)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_collection_of_object_values("memberOf", self.member_of)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("membersWithLicenseErrors", self.members_with_license_errors)
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_str_value("membershipRuleProcessingState", self.membership_rule_processing_state)
        writer.write_str_value("onPremisesDomainName", self.on_premises_domain_name)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_str_value("onPremisesNetBiosName", self.on_premises_net_bios_name)
        writer.write_collection_of_object_values("onPremisesProvisioningErrors", self.on_premises_provisioning_errors)
        writer.write_str_value("onPremisesSamAccountName", self.on_premises_sam_account_name)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_object_value("onPremisesSyncBehavior", self.on_premises_sync_behavior)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_object_value("photo", self.photo)
        writer.write_collection_of_object_values("photos", self.photos)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("preferredDataLocation", self.preferred_data_location)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_collection_of_primitive_values("proxyAddresses", self.proxy_addresses)
        writer.write_collection_of_object_values("rejectedSenders", self.rejected_senders)
        writer.write_datetime_value("renewedDateTime", self.renewed_date_time)
        writer.write_bool_value("securityEnabled", self.security_enabled)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_collection_of_object_values("serviceProvisioningErrors", self.service_provisioning_errors)
        writer.write_collection_of_object_values("settings", self.settings)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_object_value("team", self.team)
        writer.write_str_value("theme", self.theme)
        writer.write_collection_of_object_values("threads", self.threads)
        writer.write_collection_of_object_values("transitiveMemberOf", self.transitive_member_of)
        writer.write_collection_of_object_values("transitiveMembers", self.transitive_members)
        writer.write_str_value("uniqueName", self.unique_name)
        writer.write_int_value("unseenCount", self.unseen_count)
        writer.write_str_value("visibility", self.visibility)
    

