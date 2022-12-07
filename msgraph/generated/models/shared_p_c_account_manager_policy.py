from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

shared_p_c_account_deletion_policy_type = lazy_import('msgraph.generated.models.shared_p_c_account_deletion_policy_type')

class SharedPCAccountManagerPolicy(AdditionalDataHolder, Parsable):
    """
    SharedPC Account Manager Policy. Only applies when the account manager is enabled.
    """
    @property
    def account_deletion_policy(self,) -> Optional[shared_p_c_account_deletion_policy_type.SharedPCAccountDeletionPolicyType]:
        """
        Gets the accountDeletionPolicy property value. Possible values for when accounts are deleted on a shared PC.
        Returns: Optional[shared_p_c_account_deletion_policy_type.SharedPCAccountDeletionPolicyType]
        """
        return self._account_deletion_policy
    
    @account_deletion_policy.setter
    def account_deletion_policy(self,value: Optional[shared_p_c_account_deletion_policy_type.SharedPCAccountDeletionPolicyType] = None) -> None:
        """
        Sets the accountDeletionPolicy property value. Possible values for when accounts are deleted on a shared PC.
        Args:
            value: Value to set for the accountDeletionPolicy property.
        """
        self._account_deletion_policy = value
    
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
    def cache_accounts_above_disk_free_percentage(self,) -> Optional[int]:
        """
        Gets the cacheAccountsAboveDiskFreePercentage property value. Sets the percentage of available disk space a PC should have before it stops deleting cached shared PC accounts. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._cache_accounts_above_disk_free_percentage
    
    @cache_accounts_above_disk_free_percentage.setter
    def cache_accounts_above_disk_free_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the cacheAccountsAboveDiskFreePercentage property value. Sets the percentage of available disk space a PC should have before it stops deleting cached shared PC accounts. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        Args:
            value: Value to set for the cacheAccountsAboveDiskFreePercentage property.
        """
        self._cache_accounts_above_disk_free_percentage = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sharedPCAccountManagerPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Possible values for when accounts are deleted on a shared PC.
        self._account_deletion_policy: Optional[shared_p_c_account_deletion_policy_type.SharedPCAccountDeletionPolicyType] = None
        # Sets the percentage of available disk space a PC should have before it stops deleting cached shared PC accounts. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        self._cache_accounts_above_disk_free_percentage: Optional[int] = None
        # Specifies when the accounts will start being deleted when they have not been logged on during the specified period, given as number of days. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold.
        self._inactive_threshold_days: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Sets the percentage of disk space remaining on a PC before cached accounts will be deleted to free disk space. Accounts that have been inactive the longest will be deleted first. Only applies when AccountDeletionPolicy is DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        self._remove_accounts_below_disk_free_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedPCAccountManagerPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedPCAccountManagerPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedPCAccountManagerPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_deletion_policy": lambda n : setattr(self, 'account_deletion_policy', n.get_enum_value(shared_p_c_account_deletion_policy_type.SharedPCAccountDeletionPolicyType)),
            "cache_accounts_above_disk_free_percentage": lambda n : setattr(self, 'cache_accounts_above_disk_free_percentage', n.get_int_value()),
            "inactive_threshold_days": lambda n : setattr(self, 'inactive_threshold_days', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remove_accounts_below_disk_free_percentage": lambda n : setattr(self, 'remove_accounts_below_disk_free_percentage', n.get_int_value()),
        }
        return fields
    
    @property
    def inactive_threshold_days(self,) -> Optional[int]:
        """
        Gets the inactiveThresholdDays property value. Specifies when the accounts will start being deleted when they have not been logged on during the specified period, given as number of days. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold.
        Returns: Optional[int]
        """
        return self._inactive_threshold_days
    
    @inactive_threshold_days.setter
    def inactive_threshold_days(self,value: Optional[int] = None) -> None:
        """
        Sets the inactiveThresholdDays property value. Specifies when the accounts will start being deleted when they have not been logged on during the specified period, given as number of days. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold.
        Args:
            value: Value to set for the inactiveThresholdDays property.
        """
        self._inactive_threshold_days = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remove_accounts_below_disk_free_percentage(self,) -> Optional[int]:
        """
        Gets the removeAccountsBelowDiskFreePercentage property value. Sets the percentage of disk space remaining on a PC before cached accounts will be deleted to free disk space. Accounts that have been inactive the longest will be deleted first. Only applies when AccountDeletionPolicy is DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._remove_accounts_below_disk_free_percentage
    
    @remove_accounts_below_disk_free_percentage.setter
    def remove_accounts_below_disk_free_percentage(self,value: Optional[int] = None) -> None:
        """
        Sets the removeAccountsBelowDiskFreePercentage property value. Sets the percentage of disk space remaining on a PC before cached accounts will be deleted to free disk space. Accounts that have been inactive the longest will be deleted first. Only applies when AccountDeletionPolicy is DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
        Args:
            value: Value to set for the removeAccountsBelowDiskFreePercentage property.
        """
        self._remove_accounts_below_disk_free_percentage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("accountDeletionPolicy", self.account_deletion_policy)
        writer.write_int_value("cacheAccountsAboveDiskFreePercentage", self.cache_accounts_above_disk_free_percentage)
        writer.write_int_value("inactiveThresholdDays", self.inactive_threshold_days)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("removeAccountsBelowDiskFreePercentage", self.remove_accounts_below_disk_free_percentage)
        writer.write_additional_data_value(self.additional_data)
    

