from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class OnPremisesDirectorySynchronizationFeature(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesDirectorySynchronizationFeature and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Used to block cloud object takeover via source anchor hard match if enabled.
        self._block_cloud_object_takeover_through_hard_match_enabled: Optional[bool] = None
        # Use to block soft match for all objects if enabled for the  tenant. Customers are encouraged to enable this feature and keep it enabled until soft matching is required again for their tenancy. This flag should be enabled again after any soft matching has been completed and is no longer needed.
        self._block_soft_match_enabled: Optional[bool] = None
        # When true, persists the values of Mobile and OtherMobile in on-premises AD during sync cycles instead of values of MobilePhone or AlternateMobilePhones in Azure AD.
        self._bypass_dir_sync_overrides_enabled: Optional[bool] = None
        # Used to indicate that cloud password policy applies to users whose passwords are synchronized from on-premises.
        self._cloud_password_policy_for_password_synced_users_enabled: Optional[bool] = None
        # Used to enable concurrent user credentials update in OrgId.
        self._concurrent_credential_update_enabled: Optional[bool] = None
        # Used to enable concurrent user creation in OrgId.
        self._concurrent_org_id_provisioning_enabled: Optional[bool] = None
        # Used to indicate that device write-back is enabled.
        self._device_writeback_enabled: Optional[bool] = None
        # Used to indicate that directory extensions are being synced from on-premises AD to Azure AD.
        self._directory_extensions_enabled: Optional[bool] = None
        # Used to indicate that for a Microsoft Forefront Online Protection for Exchange (FOPE) migrated tenant, the conflicting proxy address should be migrated over.
        self._fope_conflict_resolution_enabled: Optional[bool] = None
        # Used to enable object-level group writeback feature for additional group types.
        self._group_write_back_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Used to indicate on-premise password synchronization is enabled.
        self._password_sync_enabled: Optional[bool] = None
        # Used to indicate that writeback of password resets from Azure AD to on-premises AD is enabled.
        self._password_writeback_enabled: Optional[bool] = None
        # Used to indicate that we should quarantine objects with conflicting proxy address.
        self._quarantine_upon_proxy_addresses_conflict_enabled: Optional[bool] = None
        # Used to indicate that we should quarantine objects conflicting with duplicate userPrincipalName.
        self._quarantine_upon_upn_conflict_enabled: Optional[bool] = None
        # Used to indicate that we should soft match objects based on userPrincipalName.
        self._soft_match_on_upn_enabled: Optional[bool] = None
        # Used to indicate that we should synchronize userPrincipalName objects for managed users with licenses.
        self._synchronize_upn_for_managed_users_enabled: Optional[bool] = None
        # Used to indicate that Microsoft 365 Group write-back is enabled.
        self._unified_group_writeback_enabled: Optional[bool] = None
        # Used to indicate that feature to force password change for a user on logon is enabled while synchronizing on-premise credentials.
        self._user_force_password_change_on_logon_enabled: Optional[bool] = None
        # Used to indicate that user writeback is enabled.
        self._user_writeback_enabled: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def block_cloud_object_takeover_through_hard_match_enabled(self,) -> Optional[bool]:
        """
        Gets the blockCloudObjectTakeoverThroughHardMatchEnabled property value. Used to block cloud object takeover via source anchor hard match if enabled.
        Returns: Optional[bool]
        """
        return self._block_cloud_object_takeover_through_hard_match_enabled
    
    @block_cloud_object_takeover_through_hard_match_enabled.setter
    def block_cloud_object_takeover_through_hard_match_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockCloudObjectTakeoverThroughHardMatchEnabled property value. Used to block cloud object takeover via source anchor hard match if enabled.
        Args:
            value: Value to set for the block_cloud_object_takeover_through_hard_match_enabled property.
        """
        self._block_cloud_object_takeover_through_hard_match_enabled = value
    
    @property
    def block_soft_match_enabled(self,) -> Optional[bool]:
        """
        Gets the blockSoftMatchEnabled property value. Use to block soft match for all objects if enabled for the  tenant. Customers are encouraged to enable this feature and keep it enabled until soft matching is required again for their tenancy. This flag should be enabled again after any soft matching has been completed and is no longer needed.
        Returns: Optional[bool]
        """
        return self._block_soft_match_enabled
    
    @block_soft_match_enabled.setter
    def block_soft_match_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockSoftMatchEnabled property value. Use to block soft match for all objects if enabled for the  tenant. Customers are encouraged to enable this feature and keep it enabled until soft matching is required again for their tenancy. This flag should be enabled again after any soft matching has been completed and is no longer needed.
        Args:
            value: Value to set for the block_soft_match_enabled property.
        """
        self._block_soft_match_enabled = value
    
    @property
    def bypass_dir_sync_overrides_enabled(self,) -> Optional[bool]:
        """
        Gets the bypassDirSyncOverridesEnabled property value. When true, persists the values of Mobile and OtherMobile in on-premises AD during sync cycles instead of values of MobilePhone or AlternateMobilePhones in Azure AD.
        Returns: Optional[bool]
        """
        return self._bypass_dir_sync_overrides_enabled
    
    @bypass_dir_sync_overrides_enabled.setter
    def bypass_dir_sync_overrides_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the bypassDirSyncOverridesEnabled property value. When true, persists the values of Mobile and OtherMobile in on-premises AD during sync cycles instead of values of MobilePhone or AlternateMobilePhones in Azure AD.
        Args:
            value: Value to set for the bypass_dir_sync_overrides_enabled property.
        """
        self._bypass_dir_sync_overrides_enabled = value
    
    @property
    def cloud_password_policy_for_password_synced_users_enabled(self,) -> Optional[bool]:
        """
        Gets the cloudPasswordPolicyForPasswordSyncedUsersEnabled property value. Used to indicate that cloud password policy applies to users whose passwords are synchronized from on-premises.
        Returns: Optional[bool]
        """
        return self._cloud_password_policy_for_password_synced_users_enabled
    
    @cloud_password_policy_for_password_synced_users_enabled.setter
    def cloud_password_policy_for_password_synced_users_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the cloudPasswordPolicyForPasswordSyncedUsersEnabled property value. Used to indicate that cloud password policy applies to users whose passwords are synchronized from on-premises.
        Args:
            value: Value to set for the cloud_password_policy_for_password_synced_users_enabled property.
        """
        self._cloud_password_policy_for_password_synced_users_enabled = value
    
    @property
    def concurrent_credential_update_enabled(self,) -> Optional[bool]:
        """
        Gets the concurrentCredentialUpdateEnabled property value. Used to enable concurrent user credentials update in OrgId.
        Returns: Optional[bool]
        """
        return self._concurrent_credential_update_enabled
    
    @concurrent_credential_update_enabled.setter
    def concurrent_credential_update_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the concurrentCredentialUpdateEnabled property value. Used to enable concurrent user credentials update in OrgId.
        Args:
            value: Value to set for the concurrent_credential_update_enabled property.
        """
        self._concurrent_credential_update_enabled = value
    
    @property
    def concurrent_org_id_provisioning_enabled(self,) -> Optional[bool]:
        """
        Gets the concurrentOrgIdProvisioningEnabled property value. Used to enable concurrent user creation in OrgId.
        Returns: Optional[bool]
        """
        return self._concurrent_org_id_provisioning_enabled
    
    @concurrent_org_id_provisioning_enabled.setter
    def concurrent_org_id_provisioning_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the concurrentOrgIdProvisioningEnabled property value. Used to enable concurrent user creation in OrgId.
        Args:
            value: Value to set for the concurrent_org_id_provisioning_enabled property.
        """
        self._concurrent_org_id_provisioning_enabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronizationFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationFeature
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesDirectorySynchronizationFeature()
    
    @property
    def device_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceWritebackEnabled property value. Used to indicate that device write-back is enabled.
        Returns: Optional[bool]
        """
        return self._device_writeback_enabled
    
    @device_writeback_enabled.setter
    def device_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceWritebackEnabled property value. Used to indicate that device write-back is enabled.
        Args:
            value: Value to set for the device_writeback_enabled property.
        """
        self._device_writeback_enabled = value
    
    @property
    def directory_extensions_enabled(self,) -> Optional[bool]:
        """
        Gets the directoryExtensionsEnabled property value. Used to indicate that directory extensions are being synced from on-premises AD to Azure AD.
        Returns: Optional[bool]
        """
        return self._directory_extensions_enabled
    
    @directory_extensions_enabled.setter
    def directory_extensions_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the directoryExtensionsEnabled property value. Used to indicate that directory extensions are being synced from on-premises AD to Azure AD.
        Args:
            value: Value to set for the directory_extensions_enabled property.
        """
        self._directory_extensions_enabled = value
    
    @property
    def fope_conflict_resolution_enabled(self,) -> Optional[bool]:
        """
        Gets the fopeConflictResolutionEnabled property value. Used to indicate that for a Microsoft Forefront Online Protection for Exchange (FOPE) migrated tenant, the conflicting proxy address should be migrated over.
        Returns: Optional[bool]
        """
        return self._fope_conflict_resolution_enabled
    
    @fope_conflict_resolution_enabled.setter
    def fope_conflict_resolution_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the fopeConflictResolutionEnabled property value. Used to indicate that for a Microsoft Forefront Online Protection for Exchange (FOPE) migrated tenant, the conflicting proxy address should be migrated over.
        Args:
            value: Value to set for the fope_conflict_resolution_enabled property.
        """
        self._fope_conflict_resolution_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "blockCloudObjectTakeoverThroughHardMatchEnabled": lambda n : setattr(self, 'block_cloud_object_takeover_through_hard_match_enabled', n.get_bool_value()),
            "blockSoftMatchEnabled": lambda n : setattr(self, 'block_soft_match_enabled', n.get_bool_value()),
            "bypassDirSyncOverridesEnabled": lambda n : setattr(self, 'bypass_dir_sync_overrides_enabled', n.get_bool_value()),
            "cloudPasswordPolicyForPasswordSyncedUsersEnabled": lambda n : setattr(self, 'cloud_password_policy_for_password_synced_users_enabled', n.get_bool_value()),
            "concurrentCredentialUpdateEnabled": lambda n : setattr(self, 'concurrent_credential_update_enabled', n.get_bool_value()),
            "concurrentOrgIdProvisioningEnabled": lambda n : setattr(self, 'concurrent_org_id_provisioning_enabled', n.get_bool_value()),
            "deviceWritebackEnabled": lambda n : setattr(self, 'device_writeback_enabled', n.get_bool_value()),
            "directoryExtensionsEnabled": lambda n : setattr(self, 'directory_extensions_enabled', n.get_bool_value()),
            "fopeConflictResolutionEnabled": lambda n : setattr(self, 'fope_conflict_resolution_enabled', n.get_bool_value()),
            "groupWriteBackEnabled": lambda n : setattr(self, 'group_write_back_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordSyncEnabled": lambda n : setattr(self, 'password_sync_enabled', n.get_bool_value()),
            "passwordWritebackEnabled": lambda n : setattr(self, 'password_writeback_enabled', n.get_bool_value()),
            "quarantineUponProxyAddressesConflictEnabled": lambda n : setattr(self, 'quarantine_upon_proxy_addresses_conflict_enabled', n.get_bool_value()),
            "quarantineUponUpnConflictEnabled": lambda n : setattr(self, 'quarantine_upon_upn_conflict_enabled', n.get_bool_value()),
            "softMatchOnUpnEnabled": lambda n : setattr(self, 'soft_match_on_upn_enabled', n.get_bool_value()),
            "synchronizeUpnForManagedUsersEnabled": lambda n : setattr(self, 'synchronize_upn_for_managed_users_enabled', n.get_bool_value()),
            "unifiedGroupWritebackEnabled": lambda n : setattr(self, 'unified_group_writeback_enabled', n.get_bool_value()),
            "userForcePasswordChangeOnLogonEnabled": lambda n : setattr(self, 'user_force_password_change_on_logon_enabled', n.get_bool_value()),
            "userWritebackEnabled": lambda n : setattr(self, 'user_writeback_enabled', n.get_bool_value()),
        }
        return fields
    
    @property
    def group_write_back_enabled(self,) -> Optional[bool]:
        """
        Gets the groupWriteBackEnabled property value. Used to enable object-level group writeback feature for additional group types.
        Returns: Optional[bool]
        """
        return self._group_write_back_enabled
    
    @group_write_back_enabled.setter
    def group_write_back_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the groupWriteBackEnabled property value. Used to enable object-level group writeback feature for additional group types.
        Args:
            value: Value to set for the group_write_back_enabled property.
        """
        self._group_write_back_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def password_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the passwordSyncEnabled property value. Used to indicate on-premise password synchronization is enabled.
        Returns: Optional[bool]
        """
        return self._password_sync_enabled
    
    @password_sync_enabled.setter
    def password_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordSyncEnabled property value. Used to indicate on-premise password synchronization is enabled.
        Args:
            value: Value to set for the password_sync_enabled property.
        """
        self._password_sync_enabled = value
    
    @property
    def password_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the passwordWritebackEnabled property value. Used to indicate that writeback of password resets from Azure AD to on-premises AD is enabled.
        Returns: Optional[bool]
        """
        return self._password_writeback_enabled
    
    @password_writeback_enabled.setter
    def password_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordWritebackEnabled property value. Used to indicate that writeback of password resets from Azure AD to on-premises AD is enabled.
        Args:
            value: Value to set for the password_writeback_enabled property.
        """
        self._password_writeback_enabled = value
    
    @property
    def quarantine_upon_proxy_addresses_conflict_enabled(self,) -> Optional[bool]:
        """
        Gets the quarantineUponProxyAddressesConflictEnabled property value. Used to indicate that we should quarantine objects with conflicting proxy address.
        Returns: Optional[bool]
        """
        return self._quarantine_upon_proxy_addresses_conflict_enabled
    
    @quarantine_upon_proxy_addresses_conflict_enabled.setter
    def quarantine_upon_proxy_addresses_conflict_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the quarantineUponProxyAddressesConflictEnabled property value. Used to indicate that we should quarantine objects with conflicting proxy address.
        Args:
            value: Value to set for the quarantine_upon_proxy_addresses_conflict_enabled property.
        """
        self._quarantine_upon_proxy_addresses_conflict_enabled = value
    
    @property
    def quarantine_upon_upn_conflict_enabled(self,) -> Optional[bool]:
        """
        Gets the quarantineUponUpnConflictEnabled property value. Used to indicate that we should quarantine objects conflicting with duplicate userPrincipalName.
        Returns: Optional[bool]
        """
        return self._quarantine_upon_upn_conflict_enabled
    
    @quarantine_upon_upn_conflict_enabled.setter
    def quarantine_upon_upn_conflict_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the quarantineUponUpnConflictEnabled property value. Used to indicate that we should quarantine objects conflicting with duplicate userPrincipalName.
        Args:
            value: Value to set for the quarantine_upon_upn_conflict_enabled property.
        """
        self._quarantine_upon_upn_conflict_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("blockCloudObjectTakeoverThroughHardMatchEnabled", self.block_cloud_object_takeover_through_hard_match_enabled)
        writer.write_bool_value("blockSoftMatchEnabled", self.block_soft_match_enabled)
        writer.write_bool_value("bypassDirSyncOverridesEnabled", self.bypass_dir_sync_overrides_enabled)
        writer.write_bool_value("cloudPasswordPolicyForPasswordSyncedUsersEnabled", self.cloud_password_policy_for_password_synced_users_enabled)
        writer.write_bool_value("concurrentCredentialUpdateEnabled", self.concurrent_credential_update_enabled)
        writer.write_bool_value("concurrentOrgIdProvisioningEnabled", self.concurrent_org_id_provisioning_enabled)
        writer.write_bool_value("deviceWritebackEnabled", self.device_writeback_enabled)
        writer.write_bool_value("directoryExtensionsEnabled", self.directory_extensions_enabled)
        writer.write_bool_value("fopeConflictResolutionEnabled", self.fope_conflict_resolution_enabled)
        writer.write_bool_value("groupWriteBackEnabled", self.group_write_back_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("passwordSyncEnabled", self.password_sync_enabled)
        writer.write_bool_value("passwordWritebackEnabled", self.password_writeback_enabled)
        writer.write_bool_value("quarantineUponProxyAddressesConflictEnabled", self.quarantine_upon_proxy_addresses_conflict_enabled)
        writer.write_bool_value("quarantineUponUpnConflictEnabled", self.quarantine_upon_upn_conflict_enabled)
        writer.write_bool_value("softMatchOnUpnEnabled", self.soft_match_on_upn_enabled)
        writer.write_bool_value("synchronizeUpnForManagedUsersEnabled", self.synchronize_upn_for_managed_users_enabled)
        writer.write_bool_value("unifiedGroupWritebackEnabled", self.unified_group_writeback_enabled)
        writer.write_bool_value("userForcePasswordChangeOnLogonEnabled", self.user_force_password_change_on_logon_enabled)
        writer.write_bool_value("userWritebackEnabled", self.user_writeback_enabled)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def soft_match_on_upn_enabled(self,) -> Optional[bool]:
        """
        Gets the softMatchOnUpnEnabled property value. Used to indicate that we should soft match objects based on userPrincipalName.
        Returns: Optional[bool]
        """
        return self._soft_match_on_upn_enabled
    
    @soft_match_on_upn_enabled.setter
    def soft_match_on_upn_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the softMatchOnUpnEnabled property value. Used to indicate that we should soft match objects based on userPrincipalName.
        Args:
            value: Value to set for the soft_match_on_upn_enabled property.
        """
        self._soft_match_on_upn_enabled = value
    
    @property
    def synchronize_upn_for_managed_users_enabled(self,) -> Optional[bool]:
        """
        Gets the synchronizeUpnForManagedUsersEnabled property value. Used to indicate that we should synchronize userPrincipalName objects for managed users with licenses.
        Returns: Optional[bool]
        """
        return self._synchronize_upn_for_managed_users_enabled
    
    @synchronize_upn_for_managed_users_enabled.setter
    def synchronize_upn_for_managed_users_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the synchronizeUpnForManagedUsersEnabled property value. Used to indicate that we should synchronize userPrincipalName objects for managed users with licenses.
        Args:
            value: Value to set for the synchronize_upn_for_managed_users_enabled property.
        """
        self._synchronize_upn_for_managed_users_enabled = value
    
    @property
    def unified_group_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the unifiedGroupWritebackEnabled property value. Used to indicate that Microsoft 365 Group write-back is enabled.
        Returns: Optional[bool]
        """
        return self._unified_group_writeback_enabled
    
    @unified_group_writeback_enabled.setter
    def unified_group_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the unifiedGroupWritebackEnabled property value. Used to indicate that Microsoft 365 Group write-back is enabled.
        Args:
            value: Value to set for the unified_group_writeback_enabled property.
        """
        self._unified_group_writeback_enabled = value
    
    @property
    def user_force_password_change_on_logon_enabled(self,) -> Optional[bool]:
        """
        Gets the userForcePasswordChangeOnLogonEnabled property value. Used to indicate that feature to force password change for a user on logon is enabled while synchronizing on-premise credentials.
        Returns: Optional[bool]
        """
        return self._user_force_password_change_on_logon_enabled
    
    @user_force_password_change_on_logon_enabled.setter
    def user_force_password_change_on_logon_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userForcePasswordChangeOnLogonEnabled property value. Used to indicate that feature to force password change for a user on logon is enabled while synchronizing on-premise credentials.
        Args:
            value: Value to set for the user_force_password_change_on_logon_enabled property.
        """
        self._user_force_password_change_on_logon_enabled = value
    
    @property
    def user_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the userWritebackEnabled property value. Used to indicate that user writeback is enabled.
        Returns: Optional[bool]
        """
        return self._user_writeback_enabled
    
    @user_writeback_enabled.setter
    def user_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userWritebackEnabled property value. Used to indicate that user writeback is enabled.
        Args:
            value: Value to set for the user_writeback_enabled property.
        """
        self._user_writeback_enabled = value
    

