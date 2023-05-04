from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, idle_session_sign_out, image_tagging_choice, sharing_capabilities, sharing_domain_restriction_mode

from . import entity

class SharepointSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new sharepointSettings and sets the default values.
        """
        super().__init__()
        # Collection of trusted domain GUIDs for the OneDrive sync app.
        self._allowed_domain_guids_for_sync_app: Optional[List[UUID]] = None
        # Collection of managed paths available for site creation. Read-only.
        self._available_managed_paths_for_site_creation: Optional[List[str]] = None
        # The number of days for preserving a deleted user's OneDrive.
        self._deleted_user_personal_site_retention_period_in_days: Optional[int] = None
        # Collection of file extensions not uploaded by the OneDrive sync app.
        self._excluded_file_extensions_for_sync_app: Optional[List[str]] = None
        # Specifies the idle session sign-out policies for the tenant.
        self._idle_session_sign_out: Optional[idle_session_sign_out.IdleSessionSignOut] = None
        # Specifies the image tagging option for the tenant. Possible values are: disabled, basic, enhanced.
        self._image_tagging_option: Optional[image_tagging_choice.ImageTaggingChoice] = None
        # Indicates whether comments are allowed on modern site pages in SharePoint.
        self._is_commenting_on_site_pages_enabled: Optional[bool] = None
        # Indicates whether push notifications are enabled for OneDrive events.
        self._is_file_activity_notification_enabled: Optional[bool] = None
        # Indicates whether legacy authentication protocols are enabled for the tenant.
        self._is_legacy_auth_protocols_enabled: Optional[bool] = None
        # Indicates whether if Fluid Framework is allowed on SharePoint sites.
        self._is_loop_enabled: Optional[bool] = None
        # Indicates whether files can be synced using the OneDrive sync app for Mac.
        self._is_mac_sync_app_enabled: Optional[bool] = None
        # Indicates whether guests must sign in using the same account to which sharing invitations are sent.
        self._is_require_accepting_user_to_match_invited_user_enabled: Optional[bool] = None
        # Indicates whether guests are allowed to reshare files, folders, and sites they don't own.
        self._is_resharing_by_external_users_enabled: Optional[bool] = None
        # Indicates whether mobile push notifications are enabled for SharePoint.
        self._is_share_point_mobile_notification_enabled: Optional[bool] = None
        # Indicates whether the newsfeed is allowed on the modern site pages in SharePoint.
        self._is_share_point_newsfeed_enabled: Optional[bool] = None
        # Indicates whether users are allowed to create sites.
        self._is_site_creation_enabled: Optional[bool] = None
        # Indicates whether the UI commands for creating sites are shown.
        self._is_site_creation_u_i_enabled: Optional[bool] = None
        # Indicates whether creating new modern pages is allowed on SharePoint sites.
        self._is_site_pages_creation_enabled: Optional[bool] = None
        # Indicates whether site storage space is automatically managed or if specific storage limits are set per site.
        self._is_sites_storage_limit_automatic: Optional[bool] = None
        # Indicates whether the sync button in OneDrive is hidden.
        self._is_sync_button_hidden_on_personal_site: Optional[bool] = None
        # Indicates whether users are allowed to sync files only on PCs joined to specific domains.
        self._is_unmanaged_sync_app_for_tenant_restricted: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The default OneDrive storage limit for all new and existing users who are assigned a qualifying license. Measured in megabytes (MB).
        self._personal_site_default_storage_limit_in_m_b: Optional[int] = None
        # Collection of email domains that are allowed for sharing outside the organization.
        self._sharing_allowed_domain_list: Optional[List[str]] = None
        # Collection of email domains that are blocked for sharing outside the organization.
        self._sharing_blocked_domain_list: Optional[List[str]] = None
        # Sharing capability for the tenant. Possible values are: disabled, externalUserSharingOnly, externalUserAndGuestSharing, existingExternalUserSharingOnly.
        self._sharing_capability: Optional[sharing_capabilities.SharingCapabilities] = None
        # Specifies the external sharing mode for domains. Possible values are: none, allowList, blockList.
        self._sharing_domain_restriction_mode: Optional[sharing_domain_restriction_mode.SharingDomainRestrictionMode] = None
        # The value of the team site managed path. This is the path under which new team sites will be created.
        self._site_creation_default_managed_path: Optional[str] = None
        # The default storage quota for a new site upon creation. Measured in megabytes (MB).
        self._site_creation_default_storage_limit_in_m_b: Optional[int] = None
        # The default timezone of a tenant for newly created sites. For a list of possible values, see SPRegionalSettings.TimeZones property.
        self._tenant_default_timezone: Optional[str] = None
    
    @property
    def allowed_domain_guids_for_sync_app(self,) -> Optional[List[UUID]]:
        """
        Gets the allowedDomainGuidsForSyncApp property value. Collection of trusted domain GUIDs for the OneDrive sync app.
        Returns: Optional[List[UUID]]
        """
        return self._allowed_domain_guids_for_sync_app
    
    @allowed_domain_guids_for_sync_app.setter
    def allowed_domain_guids_for_sync_app(self,value: Optional[List[UUID]] = None) -> None:
        """
        Sets the allowedDomainGuidsForSyncApp property value. Collection of trusted domain GUIDs for the OneDrive sync app.
        Args:
            value: Value to set for the allowed_domain_guids_for_sync_app property.
        """
        self._allowed_domain_guids_for_sync_app = value
    
    @property
    def available_managed_paths_for_site_creation(self,) -> Optional[List[str]]:
        """
        Gets the availableManagedPathsForSiteCreation property value. Collection of managed paths available for site creation. Read-only.
        Returns: Optional[List[str]]
        """
        return self._available_managed_paths_for_site_creation
    
    @available_managed_paths_for_site_creation.setter
    def available_managed_paths_for_site_creation(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the availableManagedPathsForSiteCreation property value. Collection of managed paths available for site creation. Read-only.
        Args:
            value: Value to set for the available_managed_paths_for_site_creation property.
        """
        self._available_managed_paths_for_site_creation = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharepointSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharepointSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharepointSettings()
    
    @property
    def deleted_user_personal_site_retention_period_in_days(self,) -> Optional[int]:
        """
        Gets the deletedUserPersonalSiteRetentionPeriodInDays property value. The number of days for preserving a deleted user's OneDrive.
        Returns: Optional[int]
        """
        return self._deleted_user_personal_site_retention_period_in_days
    
    @deleted_user_personal_site_retention_period_in_days.setter
    def deleted_user_personal_site_retention_period_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deletedUserPersonalSiteRetentionPeriodInDays property value. The number of days for preserving a deleted user's OneDrive.
        Args:
            value: Value to set for the deleted_user_personal_site_retention_period_in_days property.
        """
        self._deleted_user_personal_site_retention_period_in_days = value
    
    @property
    def excluded_file_extensions_for_sync_app(self,) -> Optional[List[str]]:
        """
        Gets the excludedFileExtensionsForSyncApp property value. Collection of file extensions not uploaded by the OneDrive sync app.
        Returns: Optional[List[str]]
        """
        return self._excluded_file_extensions_for_sync_app
    
    @excluded_file_extensions_for_sync_app.setter
    def excluded_file_extensions_for_sync_app(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludedFileExtensionsForSyncApp property value. Collection of file extensions not uploaded by the OneDrive sync app.
        Args:
            value: Value to set for the excluded_file_extensions_for_sync_app property.
        """
        self._excluded_file_extensions_for_sync_app = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, idle_session_sign_out, image_tagging_choice, sharing_capabilities, sharing_domain_restriction_mode

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedDomainGuidsForSyncApp": lambda n : setattr(self, 'allowed_domain_guids_for_sync_app', n.get_collection_of_primitive_values(UUID)),
            "availableManagedPathsForSiteCreation": lambda n : setattr(self, 'available_managed_paths_for_site_creation', n.get_collection_of_primitive_values(str)),
            "deletedUserPersonalSiteRetentionPeriodInDays": lambda n : setattr(self, 'deleted_user_personal_site_retention_period_in_days', n.get_int_value()),
            "excludedFileExtensionsForSyncApp": lambda n : setattr(self, 'excluded_file_extensions_for_sync_app', n.get_collection_of_primitive_values(str)),
            "idleSessionSignOut": lambda n : setattr(self, 'idle_session_sign_out', n.get_object_value(idle_session_sign_out.IdleSessionSignOut)),
            "imageTaggingOption": lambda n : setattr(self, 'image_tagging_option', n.get_enum_value(image_tagging_choice.ImageTaggingChoice)),
            "isCommentingOnSitePagesEnabled": lambda n : setattr(self, 'is_commenting_on_site_pages_enabled', n.get_bool_value()),
            "isFileActivityNotificationEnabled": lambda n : setattr(self, 'is_file_activity_notification_enabled', n.get_bool_value()),
            "isLegacyAuthProtocolsEnabled": lambda n : setattr(self, 'is_legacy_auth_protocols_enabled', n.get_bool_value()),
            "isLoopEnabled": lambda n : setattr(self, 'is_loop_enabled', n.get_bool_value()),
            "isMacSyncAppEnabled": lambda n : setattr(self, 'is_mac_sync_app_enabled', n.get_bool_value()),
            "isRequireAcceptingUserToMatchInvitedUserEnabled": lambda n : setattr(self, 'is_require_accepting_user_to_match_invited_user_enabled', n.get_bool_value()),
            "isResharingByExternalUsersEnabled": lambda n : setattr(self, 'is_resharing_by_external_users_enabled', n.get_bool_value()),
            "isSharePointMobileNotificationEnabled": lambda n : setattr(self, 'is_share_point_mobile_notification_enabled', n.get_bool_value()),
            "isSharePointNewsfeedEnabled": lambda n : setattr(self, 'is_share_point_newsfeed_enabled', n.get_bool_value()),
            "isSitesStorageLimitAutomatic": lambda n : setattr(self, 'is_sites_storage_limit_automatic', n.get_bool_value()),
            "isSiteCreationEnabled": lambda n : setattr(self, 'is_site_creation_enabled', n.get_bool_value()),
            "isSiteCreationUIEnabled": lambda n : setattr(self, 'is_site_creation_u_i_enabled', n.get_bool_value()),
            "isSitePagesCreationEnabled": lambda n : setattr(self, 'is_site_pages_creation_enabled', n.get_bool_value()),
            "isSyncButtonHiddenOnPersonalSite": lambda n : setattr(self, 'is_sync_button_hidden_on_personal_site', n.get_bool_value()),
            "isUnmanagedSyncAppForTenantRestricted": lambda n : setattr(self, 'is_unmanaged_sync_app_for_tenant_restricted', n.get_bool_value()),
            "personalSiteDefaultStorageLimitInMB": lambda n : setattr(self, 'personal_site_default_storage_limit_in_m_b', n.get_int_value()),
            "sharingAllowedDomainList": lambda n : setattr(self, 'sharing_allowed_domain_list', n.get_collection_of_primitive_values(str)),
            "sharingBlockedDomainList": lambda n : setattr(self, 'sharing_blocked_domain_list', n.get_collection_of_primitive_values(str)),
            "sharingCapability": lambda n : setattr(self, 'sharing_capability', n.get_enum_value(sharing_capabilities.SharingCapabilities)),
            "sharingDomainRestrictionMode": lambda n : setattr(self, 'sharing_domain_restriction_mode', n.get_enum_value(sharing_domain_restriction_mode.SharingDomainRestrictionMode)),
            "siteCreationDefaultManagedPath": lambda n : setattr(self, 'site_creation_default_managed_path', n.get_str_value()),
            "siteCreationDefaultStorageLimitInMB": lambda n : setattr(self, 'site_creation_default_storage_limit_in_m_b', n.get_int_value()),
            "tenantDefaultTimezone": lambda n : setattr(self, 'tenant_default_timezone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def idle_session_sign_out(self,) -> Optional[idle_session_sign_out.IdleSessionSignOut]:
        """
        Gets the idleSessionSignOut property value. Specifies the idle session sign-out policies for the tenant.
        Returns: Optional[idle_session_sign_out.IdleSessionSignOut]
        """
        return self._idle_session_sign_out
    
    @idle_session_sign_out.setter
    def idle_session_sign_out(self,value: Optional[idle_session_sign_out.IdleSessionSignOut] = None) -> None:
        """
        Sets the idleSessionSignOut property value. Specifies the idle session sign-out policies for the tenant.
        Args:
            value: Value to set for the idle_session_sign_out property.
        """
        self._idle_session_sign_out = value
    
    @property
    def image_tagging_option(self,) -> Optional[image_tagging_choice.ImageTaggingChoice]:
        """
        Gets the imageTaggingOption property value. Specifies the image tagging option for the tenant. Possible values are: disabled, basic, enhanced.
        Returns: Optional[image_tagging_choice.ImageTaggingChoice]
        """
        return self._image_tagging_option
    
    @image_tagging_option.setter
    def image_tagging_option(self,value: Optional[image_tagging_choice.ImageTaggingChoice] = None) -> None:
        """
        Sets the imageTaggingOption property value. Specifies the image tagging option for the tenant. Possible values are: disabled, basic, enhanced.
        Args:
            value: Value to set for the image_tagging_option property.
        """
        self._image_tagging_option = value
    
    @property
    def is_commenting_on_site_pages_enabled(self,) -> Optional[bool]:
        """
        Gets the isCommentingOnSitePagesEnabled property value. Indicates whether comments are allowed on modern site pages in SharePoint.
        Returns: Optional[bool]
        """
        return self._is_commenting_on_site_pages_enabled
    
    @is_commenting_on_site_pages_enabled.setter
    def is_commenting_on_site_pages_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCommentingOnSitePagesEnabled property value. Indicates whether comments are allowed on modern site pages in SharePoint.
        Args:
            value: Value to set for the is_commenting_on_site_pages_enabled property.
        """
        self._is_commenting_on_site_pages_enabled = value
    
    @property
    def is_file_activity_notification_enabled(self,) -> Optional[bool]:
        """
        Gets the isFileActivityNotificationEnabled property value. Indicates whether push notifications are enabled for OneDrive events.
        Returns: Optional[bool]
        """
        return self._is_file_activity_notification_enabled
    
    @is_file_activity_notification_enabled.setter
    def is_file_activity_notification_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFileActivityNotificationEnabled property value. Indicates whether push notifications are enabled for OneDrive events.
        Args:
            value: Value to set for the is_file_activity_notification_enabled property.
        """
        self._is_file_activity_notification_enabled = value
    
    @property
    def is_legacy_auth_protocols_enabled(self,) -> Optional[bool]:
        """
        Gets the isLegacyAuthProtocolsEnabled property value. Indicates whether legacy authentication protocols are enabled for the tenant.
        Returns: Optional[bool]
        """
        return self._is_legacy_auth_protocols_enabled
    
    @is_legacy_auth_protocols_enabled.setter
    def is_legacy_auth_protocols_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLegacyAuthProtocolsEnabled property value. Indicates whether legacy authentication protocols are enabled for the tenant.
        Args:
            value: Value to set for the is_legacy_auth_protocols_enabled property.
        """
        self._is_legacy_auth_protocols_enabled = value
    
    @property
    def is_loop_enabled(self,) -> Optional[bool]:
        """
        Gets the isLoopEnabled property value. Indicates whether if Fluid Framework is allowed on SharePoint sites.
        Returns: Optional[bool]
        """
        return self._is_loop_enabled
    
    @is_loop_enabled.setter
    def is_loop_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLoopEnabled property value. Indicates whether if Fluid Framework is allowed on SharePoint sites.
        Args:
            value: Value to set for the is_loop_enabled property.
        """
        self._is_loop_enabled = value
    
    @property
    def is_mac_sync_app_enabled(self,) -> Optional[bool]:
        """
        Gets the isMacSyncAppEnabled property value. Indicates whether files can be synced using the OneDrive sync app for Mac.
        Returns: Optional[bool]
        """
        return self._is_mac_sync_app_enabled
    
    @is_mac_sync_app_enabled.setter
    def is_mac_sync_app_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMacSyncAppEnabled property value. Indicates whether files can be synced using the OneDrive sync app for Mac.
        Args:
            value: Value to set for the is_mac_sync_app_enabled property.
        """
        self._is_mac_sync_app_enabled = value
    
    @property
    def is_require_accepting_user_to_match_invited_user_enabled(self,) -> Optional[bool]:
        """
        Gets the isRequireAcceptingUserToMatchInvitedUserEnabled property value. Indicates whether guests must sign in using the same account to which sharing invitations are sent.
        Returns: Optional[bool]
        """
        return self._is_require_accepting_user_to_match_invited_user_enabled
    
    @is_require_accepting_user_to_match_invited_user_enabled.setter
    def is_require_accepting_user_to_match_invited_user_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequireAcceptingUserToMatchInvitedUserEnabled property value. Indicates whether guests must sign in using the same account to which sharing invitations are sent.
        Args:
            value: Value to set for the is_require_accepting_user_to_match_invited_user_enabled property.
        """
        self._is_require_accepting_user_to_match_invited_user_enabled = value
    
    @property
    def is_resharing_by_external_users_enabled(self,) -> Optional[bool]:
        """
        Gets the isResharingByExternalUsersEnabled property value. Indicates whether guests are allowed to reshare files, folders, and sites they don't own.
        Returns: Optional[bool]
        """
        return self._is_resharing_by_external_users_enabled
    
    @is_resharing_by_external_users_enabled.setter
    def is_resharing_by_external_users_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isResharingByExternalUsersEnabled property value. Indicates whether guests are allowed to reshare files, folders, and sites they don't own.
        Args:
            value: Value to set for the is_resharing_by_external_users_enabled property.
        """
        self._is_resharing_by_external_users_enabled = value
    
    @property
    def is_share_point_mobile_notification_enabled(self,) -> Optional[bool]:
        """
        Gets the isSharePointMobileNotificationEnabled property value. Indicates whether mobile push notifications are enabled for SharePoint.
        Returns: Optional[bool]
        """
        return self._is_share_point_mobile_notification_enabled
    
    @is_share_point_mobile_notification_enabled.setter
    def is_share_point_mobile_notification_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSharePointMobileNotificationEnabled property value. Indicates whether mobile push notifications are enabled for SharePoint.
        Args:
            value: Value to set for the is_share_point_mobile_notification_enabled property.
        """
        self._is_share_point_mobile_notification_enabled = value
    
    @property
    def is_share_point_newsfeed_enabled(self,) -> Optional[bool]:
        """
        Gets the isSharePointNewsfeedEnabled property value. Indicates whether the newsfeed is allowed on the modern site pages in SharePoint.
        Returns: Optional[bool]
        """
        return self._is_share_point_newsfeed_enabled
    
    @is_share_point_newsfeed_enabled.setter
    def is_share_point_newsfeed_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSharePointNewsfeedEnabled property value. Indicates whether the newsfeed is allowed on the modern site pages in SharePoint.
        Args:
            value: Value to set for the is_share_point_newsfeed_enabled property.
        """
        self._is_share_point_newsfeed_enabled = value
    
    @property
    def is_site_creation_enabled(self,) -> Optional[bool]:
        """
        Gets the isSiteCreationEnabled property value. Indicates whether users are allowed to create sites.
        Returns: Optional[bool]
        """
        return self._is_site_creation_enabled
    
    @is_site_creation_enabled.setter
    def is_site_creation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSiteCreationEnabled property value. Indicates whether users are allowed to create sites.
        Args:
            value: Value to set for the is_site_creation_enabled property.
        """
        self._is_site_creation_enabled = value
    
    @property
    def is_site_creation_u_i_enabled(self,) -> Optional[bool]:
        """
        Gets the isSiteCreationUIEnabled property value. Indicates whether the UI commands for creating sites are shown.
        Returns: Optional[bool]
        """
        return self._is_site_creation_u_i_enabled
    
    @is_site_creation_u_i_enabled.setter
    def is_site_creation_u_i_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSiteCreationUIEnabled property value. Indicates whether the UI commands for creating sites are shown.
        Args:
            value: Value to set for the is_site_creation_u_i_enabled property.
        """
        self._is_site_creation_u_i_enabled = value
    
    @property
    def is_site_pages_creation_enabled(self,) -> Optional[bool]:
        """
        Gets the isSitePagesCreationEnabled property value. Indicates whether creating new modern pages is allowed on SharePoint sites.
        Returns: Optional[bool]
        """
        return self._is_site_pages_creation_enabled
    
    @is_site_pages_creation_enabled.setter
    def is_site_pages_creation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSitePagesCreationEnabled property value. Indicates whether creating new modern pages is allowed on SharePoint sites.
        Args:
            value: Value to set for the is_site_pages_creation_enabled property.
        """
        self._is_site_pages_creation_enabled = value
    
    @property
    def is_sites_storage_limit_automatic(self,) -> Optional[bool]:
        """
        Gets the isSitesStorageLimitAutomatic property value. Indicates whether site storage space is automatically managed or if specific storage limits are set per site.
        Returns: Optional[bool]
        """
        return self._is_sites_storage_limit_automatic
    
    @is_sites_storage_limit_automatic.setter
    def is_sites_storage_limit_automatic(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSitesStorageLimitAutomatic property value. Indicates whether site storage space is automatically managed or if specific storage limits are set per site.
        Args:
            value: Value to set for the is_sites_storage_limit_automatic property.
        """
        self._is_sites_storage_limit_automatic = value
    
    @property
    def is_sync_button_hidden_on_personal_site(self,) -> Optional[bool]:
        """
        Gets the isSyncButtonHiddenOnPersonalSite property value. Indicates whether the sync button in OneDrive is hidden.
        Returns: Optional[bool]
        """
        return self._is_sync_button_hidden_on_personal_site
    
    @is_sync_button_hidden_on_personal_site.setter
    def is_sync_button_hidden_on_personal_site(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSyncButtonHiddenOnPersonalSite property value. Indicates whether the sync button in OneDrive is hidden.
        Args:
            value: Value to set for the is_sync_button_hidden_on_personal_site property.
        """
        self._is_sync_button_hidden_on_personal_site = value
    
    @property
    def is_unmanaged_sync_app_for_tenant_restricted(self,) -> Optional[bool]:
        """
        Gets the isUnmanagedSyncAppForTenantRestricted property value. Indicates whether users are allowed to sync files only on PCs joined to specific domains.
        Returns: Optional[bool]
        """
        return self._is_unmanaged_sync_app_for_tenant_restricted
    
    @is_unmanaged_sync_app_for_tenant_restricted.setter
    def is_unmanaged_sync_app_for_tenant_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUnmanagedSyncAppForTenantRestricted property value. Indicates whether users are allowed to sync files only on PCs joined to specific domains.
        Args:
            value: Value to set for the is_unmanaged_sync_app_for_tenant_restricted property.
        """
        self._is_unmanaged_sync_app_for_tenant_restricted = value
    
    @property
    def personal_site_default_storage_limit_in_m_b(self,) -> Optional[int]:
        """
        Gets the personalSiteDefaultStorageLimitInMB property value. The default OneDrive storage limit for all new and existing users who are assigned a qualifying license. Measured in megabytes (MB).
        Returns: Optional[int]
        """
        return self._personal_site_default_storage_limit_in_m_b
    
    @personal_site_default_storage_limit_in_m_b.setter
    def personal_site_default_storage_limit_in_m_b(self,value: Optional[int] = None) -> None:
        """
        Sets the personalSiteDefaultStorageLimitInMB property value. The default OneDrive storage limit for all new and existing users who are assigned a qualifying license. Measured in megabytes (MB).
        Args:
            value: Value to set for the personal_site_default_storage_limit_in_m_b property.
        """
        self._personal_site_default_storage_limit_in_m_b = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_bool_value("isSitesStorageLimitAutomatic", self.is_sites_storage_limit_automatic)
        writer.write_bool_value("isSiteCreationEnabled", self.is_site_creation_enabled)
        writer.write_bool_value("isSiteCreationUIEnabled", self.is_site_creation_u_i_enabled)
        writer.write_bool_value("isSitePagesCreationEnabled", self.is_site_pages_creation_enabled)
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
    
    @property
    def sharing_allowed_domain_list(self,) -> Optional[List[str]]:
        """
        Gets the sharingAllowedDomainList property value. Collection of email domains that are allowed for sharing outside the organization.
        Returns: Optional[List[str]]
        """
        return self._sharing_allowed_domain_list
    
    @sharing_allowed_domain_list.setter
    def sharing_allowed_domain_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sharingAllowedDomainList property value. Collection of email domains that are allowed for sharing outside the organization.
        Args:
            value: Value to set for the sharing_allowed_domain_list property.
        """
        self._sharing_allowed_domain_list = value
    
    @property
    def sharing_blocked_domain_list(self,) -> Optional[List[str]]:
        """
        Gets the sharingBlockedDomainList property value. Collection of email domains that are blocked for sharing outside the organization.
        Returns: Optional[List[str]]
        """
        return self._sharing_blocked_domain_list
    
    @sharing_blocked_domain_list.setter
    def sharing_blocked_domain_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sharingBlockedDomainList property value. Collection of email domains that are blocked for sharing outside the organization.
        Args:
            value: Value to set for the sharing_blocked_domain_list property.
        """
        self._sharing_blocked_domain_list = value
    
    @property
    def sharing_capability(self,) -> Optional[sharing_capabilities.SharingCapabilities]:
        """
        Gets the sharingCapability property value. Sharing capability for the tenant. Possible values are: disabled, externalUserSharingOnly, externalUserAndGuestSharing, existingExternalUserSharingOnly.
        Returns: Optional[sharing_capabilities.SharingCapabilities]
        """
        return self._sharing_capability
    
    @sharing_capability.setter
    def sharing_capability(self,value: Optional[sharing_capabilities.SharingCapabilities] = None) -> None:
        """
        Sets the sharingCapability property value. Sharing capability for the tenant. Possible values are: disabled, externalUserSharingOnly, externalUserAndGuestSharing, existingExternalUserSharingOnly.
        Args:
            value: Value to set for the sharing_capability property.
        """
        self._sharing_capability = value
    
    @property
    def sharing_domain_restriction_mode(self,) -> Optional[sharing_domain_restriction_mode.SharingDomainRestrictionMode]:
        """
        Gets the sharingDomainRestrictionMode property value. Specifies the external sharing mode for domains. Possible values are: none, allowList, blockList.
        Returns: Optional[sharing_domain_restriction_mode.SharingDomainRestrictionMode]
        """
        return self._sharing_domain_restriction_mode
    
    @sharing_domain_restriction_mode.setter
    def sharing_domain_restriction_mode(self,value: Optional[sharing_domain_restriction_mode.SharingDomainRestrictionMode] = None) -> None:
        """
        Sets the sharingDomainRestrictionMode property value. Specifies the external sharing mode for domains. Possible values are: none, allowList, blockList.
        Args:
            value: Value to set for the sharing_domain_restriction_mode property.
        """
        self._sharing_domain_restriction_mode = value
    
    @property
    def site_creation_default_managed_path(self,) -> Optional[str]:
        """
        Gets the siteCreationDefaultManagedPath property value. The value of the team site managed path. This is the path under which new team sites will be created.
        Returns: Optional[str]
        """
        return self._site_creation_default_managed_path
    
    @site_creation_default_managed_path.setter
    def site_creation_default_managed_path(self,value: Optional[str] = None) -> None:
        """
        Sets the siteCreationDefaultManagedPath property value. The value of the team site managed path. This is the path under which new team sites will be created.
        Args:
            value: Value to set for the site_creation_default_managed_path property.
        """
        self._site_creation_default_managed_path = value
    
    @property
    def site_creation_default_storage_limit_in_m_b(self,) -> Optional[int]:
        """
        Gets the siteCreationDefaultStorageLimitInMB property value. The default storage quota for a new site upon creation. Measured in megabytes (MB).
        Returns: Optional[int]
        """
        return self._site_creation_default_storage_limit_in_m_b
    
    @site_creation_default_storage_limit_in_m_b.setter
    def site_creation_default_storage_limit_in_m_b(self,value: Optional[int] = None) -> None:
        """
        Sets the siteCreationDefaultStorageLimitInMB property value. The default storage quota for a new site upon creation. Measured in megabytes (MB).
        Args:
            value: Value to set for the site_creation_default_storage_limit_in_m_b property.
        """
        self._site_creation_default_storage_limit_in_m_b = value
    
    @property
    def tenant_default_timezone(self,) -> Optional[str]:
        """
        Gets the tenantDefaultTimezone property value. The default timezone of a tenant for newly created sites. For a list of possible values, see SPRegionalSettings.TimeZones property.
        Returns: Optional[str]
        """
        return self._tenant_default_timezone
    
    @tenant_default_timezone.setter
    def tenant_default_timezone(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDefaultTimezone property value. The default timezone of a tenant for newly created sites. For a list of possible values, see SPRegionalSettings.TimeZones property.
        Args:
            value: Value to set for the tenant_default_timezone property.
        """
        self._tenant_default_timezone = value
    

