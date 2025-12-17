from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .idle_session_sign_out import IdleSessionSignOut
    from .image_tagging_choice import ImageTaggingChoice
    from .sharing_capabilities import SharingCapabilities
    from .sharing_domain_restriction_mode import SharingDomainRestrictionMode

from .entity import Entity

@dataclass
class SharepointSettings(Entity, Parsable):
    # Collection of trusted domain GUIDs for the OneDrive sync app.
    allowed_domain_guids_for_sync_app: Optional[list[UUID]] = None
    # Collection of managed paths available for site creation. Read-only.
    available_managed_paths_for_site_creation: Optional[list[str]] = None
    # The number of days for preserving a deleted user's OneDrive.
    deleted_user_personal_site_retention_period_in_days: Optional[int] = None
    # Collection of file extensions not uploaded by the OneDrive sync app.
    excluded_file_extensions_for_sync_app: Optional[list[str]] = None
    # Specifies the idle session sign-out policies for the tenant.
    idle_session_sign_out: Optional[IdleSessionSignOut] = None
    # Specifies the image tagging option for the tenant. The possible values are: disabled, basic, enhanced.
    image_tagging_option: Optional[ImageTaggingChoice] = None
    # Indicates whether comments are allowed on modern site pages in SharePoint.
    is_commenting_on_site_pages_enabled: Optional[bool] = None
    # Indicates whether push notifications are enabled for OneDrive events.
    is_file_activity_notification_enabled: Optional[bool] = None
    # Indicates whether legacy authentication protocols are enabled for the tenant.
    is_legacy_auth_protocols_enabled: Optional[bool] = None
    # Indicates whether if Fluid Framework is allowed on SharePoint sites.
    is_loop_enabled: Optional[bool] = None
    # Indicates whether files can be synced using the OneDrive sync app for Mac.
    is_mac_sync_app_enabled: Optional[bool] = None
    # Indicates whether guests must sign in using the same account to which sharing invitations are sent.
    is_require_accepting_user_to_match_invited_user_enabled: Optional[bool] = None
    # Indicates whether guests are allowed to reshare files, folders, and sites they don't own.
    is_resharing_by_external_users_enabled: Optional[bool] = None
    # Indicates whether mobile push notifications are enabled for SharePoint.
    is_share_point_mobile_notification_enabled: Optional[bool] = None
    # Indicates whether the newsfeed is allowed on the modern site pages in SharePoint.
    is_share_point_newsfeed_enabled: Optional[bool] = None
    # Indicates whether users are allowed to create sites.
    is_site_creation_enabled: Optional[bool] = None
    # Indicates whether the UI commands for creating sites are shown.
    is_site_creation_u_i_enabled: Optional[bool] = None
    # Indicates whether creating new modern pages is allowed on SharePoint sites.
    is_site_pages_creation_enabled: Optional[bool] = None
    # Indicates whether site storage space is automatically managed or if specific storage limits are set per site.
    is_sites_storage_limit_automatic: Optional[bool] = None
    # Indicates whether the sync button in OneDrive is hidden.
    is_sync_button_hidden_on_personal_site: Optional[bool] = None
    # Indicates whether users are allowed to sync files only on PCs joined to specific domains.
    is_unmanaged_sync_app_for_tenant_restricted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The default OneDrive storage limit for all new and existing users who are assigned a qualifying license. Measured in megabytes (MB).
    personal_site_default_storage_limit_in_m_b: Optional[int] = None
    # Collection of email domains that are allowed for sharing outside the organization.
    sharing_allowed_domain_list: Optional[list[str]] = None
    # Collection of email domains that are blocked for sharing outside the organization.
    sharing_blocked_domain_list: Optional[list[str]] = None
    # Sharing capability for the tenant. The possible values are: disabled, externalUserSharingOnly, externalUserAndGuestSharing, existingExternalUserSharingOnly.
    sharing_capability: Optional[SharingCapabilities] = None
    # Specifies the external sharing mode for domains. The possible values are: none, allowList, blockList.
    sharing_domain_restriction_mode: Optional[SharingDomainRestrictionMode] = None
    # The value of the team site managed path. This is the path under which new team sites will be created.
    site_creation_default_managed_path: Optional[str] = None
    # The default storage quota for a new site upon creation. Measured in megabytes (MB).
    site_creation_default_storage_limit_in_m_b: Optional[int] = None
    # The default timezone of a tenant for newly created sites. For a list of possible values, see SPRegionalSettings.TimeZones property.
    tenant_default_timezone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharepointSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharepointSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharepointSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .idle_session_sign_out import IdleSessionSignOut
        from .image_tagging_choice import ImageTaggingChoice
        from .sharing_capabilities import SharingCapabilities
        from .sharing_domain_restriction_mode import SharingDomainRestrictionMode

        from .entity import Entity
        from .idle_session_sign_out import IdleSessionSignOut
        from .image_tagging_choice import ImageTaggingChoice
        from .sharing_capabilities import SharingCapabilities
        from .sharing_domain_restriction_mode import SharingDomainRestrictionMode

        fields: dict[str, Callable[[Any], None]] = {
            "allowedDomainGuidsForSyncApp": lambda n : setattr(self, 'allowed_domain_guids_for_sync_app', n.get_collection_of_primitive_values(UUID)),
            "availableManagedPathsForSiteCreation": lambda n : setattr(self, 'available_managed_paths_for_site_creation', n.get_collection_of_primitive_values(str)),
            "deletedUserPersonalSiteRetentionPeriodInDays": lambda n : setattr(self, 'deleted_user_personal_site_retention_period_in_days', n.get_int_value()),
            "excludedFileExtensionsForSyncApp": lambda n : setattr(self, 'excluded_file_extensions_for_sync_app', n.get_collection_of_primitive_values(str)),
            "idleSessionSignOut": lambda n : setattr(self, 'idle_session_sign_out', n.get_object_value(IdleSessionSignOut)),
            "imageTaggingOption": lambda n : setattr(self, 'image_tagging_option', n.get_enum_value(ImageTaggingChoice)),
            "isCommentingOnSitePagesEnabled": lambda n : setattr(self, 'is_commenting_on_site_pages_enabled', n.get_bool_value()),
            "isFileActivityNotificationEnabled": lambda n : setattr(self, 'is_file_activity_notification_enabled', n.get_bool_value()),
            "isLegacyAuthProtocolsEnabled": lambda n : setattr(self, 'is_legacy_auth_protocols_enabled', n.get_bool_value()),
            "isLoopEnabled": lambda n : setattr(self, 'is_loop_enabled', n.get_bool_value()),
            "isMacSyncAppEnabled": lambda n : setattr(self, 'is_mac_sync_app_enabled', n.get_bool_value()),
            "isRequireAcceptingUserToMatchInvitedUserEnabled": lambda n : setattr(self, 'is_require_accepting_user_to_match_invited_user_enabled', n.get_bool_value()),
            "isResharingByExternalUsersEnabled": lambda n : setattr(self, 'is_resharing_by_external_users_enabled', n.get_bool_value()),
            "isSharePointMobileNotificationEnabled": lambda n : setattr(self, 'is_share_point_mobile_notification_enabled', n.get_bool_value()),
            "isSharePointNewsfeedEnabled": lambda n : setattr(self, 'is_share_point_newsfeed_enabled', n.get_bool_value()),
            "isSiteCreationEnabled": lambda n : setattr(self, 'is_site_creation_enabled', n.get_bool_value()),
            "isSiteCreationUIEnabled": lambda n : setattr(self, 'is_site_creation_u_i_enabled', n.get_bool_value()),
            "isSitePagesCreationEnabled": lambda n : setattr(self, 'is_site_pages_creation_enabled', n.get_bool_value()),
            "isSitesStorageLimitAutomatic": lambda n : setattr(self, 'is_sites_storage_limit_automatic', n.get_bool_value()),
            "isSyncButtonHiddenOnPersonalSite": lambda n : setattr(self, 'is_sync_button_hidden_on_personal_site', n.get_bool_value()),
            "isUnmanagedSyncAppForTenantRestricted": lambda n : setattr(self, 'is_unmanaged_sync_app_for_tenant_restricted', n.get_bool_value()),
            "personalSiteDefaultStorageLimitInMB": lambda n : setattr(self, 'personal_site_default_storage_limit_in_m_b', n.get_int_value()),
            "sharingAllowedDomainList": lambda n : setattr(self, 'sharing_allowed_domain_list', n.get_collection_of_primitive_values(str)),
            "sharingBlockedDomainList": lambda n : setattr(self, 'sharing_blocked_domain_list', n.get_collection_of_primitive_values(str)),
            "sharingCapability": lambda n : setattr(self, 'sharing_capability', n.get_enum_value(SharingCapabilities)),
            "sharingDomainRestrictionMode": lambda n : setattr(self, 'sharing_domain_restriction_mode', n.get_enum_value(SharingDomainRestrictionMode)),
            "siteCreationDefaultManagedPath": lambda n : setattr(self, 'site_creation_default_managed_path', n.get_str_value()),
            "siteCreationDefaultStorageLimitInMB": lambda n : setattr(self, 'site_creation_default_storage_limit_in_m_b', n.get_int_value()),
            "tenantDefaultTimezone": lambda n : setattr(self, 'tenant_default_timezone', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("allowedDomainGuidsForSyncApp", self.allowed_domain_guids_for_sync_app)
        writer.write_collection_of_primitive_values("availableManagedPathsForSiteCreation", self.available_managed_paths_for_site_creation)
        writer.write_int_value("deletedUserPersonalSiteRetentionPeriodInDays", self.deleted_user_personal_site_retention_period_in_days)
        writer.write_collection_of_primitive_values("excludedFileExtensionsForSyncApp", self.excluded_file_extensions_for_sync_app)
        writer.write_object_value("idleSessionSignOut", self.idle_session_sign_out)
        writer.write_enum_value("imageTaggingOption", self.image_tagging_option)
        writer.write_bool_value("isCommentingOnSitePagesEnabled", self.is_commenting_on_site_pages_enabled)
        writer.write_bool_value("isFileActivityNotificationEnabled", self.is_file_activity_notification_enabled)
        writer.write_bool_value("isLegacyAuthProtocolsEnabled", self.is_legacy_auth_protocols_enabled)
        writer.write_bool_value("isLoopEnabled", self.is_loop_enabled)
        writer.write_bool_value("isMacSyncAppEnabled", self.is_mac_sync_app_enabled)
        writer.write_bool_value("isRequireAcceptingUserToMatchInvitedUserEnabled", self.is_require_accepting_user_to_match_invited_user_enabled)
        writer.write_bool_value("isResharingByExternalUsersEnabled", self.is_resharing_by_external_users_enabled)
        writer.write_bool_value("isSharePointMobileNotificationEnabled", self.is_share_point_mobile_notification_enabled)
        writer.write_bool_value("isSharePointNewsfeedEnabled", self.is_share_point_newsfeed_enabled)
        writer.write_bool_value("isSiteCreationEnabled", self.is_site_creation_enabled)
        writer.write_bool_value("isSiteCreationUIEnabled", self.is_site_creation_u_i_enabled)
        writer.write_bool_value("isSitePagesCreationEnabled", self.is_site_pages_creation_enabled)
        writer.write_bool_value("isSitesStorageLimitAutomatic", self.is_sites_storage_limit_automatic)
        writer.write_bool_value("isSyncButtonHiddenOnPersonalSite", self.is_sync_button_hidden_on_personal_site)
        writer.write_bool_value("isUnmanagedSyncAppForTenantRestricted", self.is_unmanaged_sync_app_for_tenant_restricted)
        writer.write_int_value("personalSiteDefaultStorageLimitInMB", self.personal_site_default_storage_limit_in_m_b)
        writer.write_collection_of_primitive_values("sharingAllowedDomainList", self.sharing_allowed_domain_list)
        writer.write_collection_of_primitive_values("sharingBlockedDomainList", self.sharing_blocked_domain_list)
        writer.write_enum_value("sharingCapability", self.sharing_capability)
        writer.write_enum_value("sharingDomainRestrictionMode", self.sharing_domain_restriction_mode)
        writer.write_str_value("siteCreationDefaultManagedPath", self.site_creation_default_managed_path)
        writer.write_int_value("siteCreationDefaultStorageLimitInMB", self.site_creation_default_storage_limit_in_m_b)
        writer.write_str_value("tenantDefaultTimezone", self.tenant_default_timezone)
    

