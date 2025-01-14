from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .shared_p_c_account_deletion_policy_type import SharedPCAccountDeletionPolicyType

@dataclass
class SharedPCAccountManagerPolicy(AdditionalDataHolder, BackedModel, Parsable):
    """
    SharedPC Account Manager Policy. Only applies when the account manager is enabled.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Possible values for when accounts are deleted on a shared PC.
    account_deletion_policy: Optional[SharedPCAccountDeletionPolicyType] = None
    # Sets the percentage of available disk space a PC should have before it stops deleting cached shared PC accounts. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
    cache_accounts_above_disk_free_percentage: Optional[int] = None
    # Specifies when the accounts will start being deleted when they have not been logged on during the specified period, given as number of days. Only applies when AccountDeletionPolicy is DiskSpaceThreshold or DiskSpaceThresholdOrInactiveThreshold.
    inactive_threshold_days: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sets the percentage of disk space remaining on a PC before cached accounts will be deleted to free disk space. Accounts that have been inactive the longest will be deleted first. Only applies when AccountDeletionPolicy is DiskSpaceThresholdOrInactiveThreshold. Valid values 0 to 100
    remove_accounts_below_disk_free_percentage: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharedPCAccountManagerPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedPCAccountManagerPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharedPCAccountManagerPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .shared_p_c_account_deletion_policy_type import SharedPCAccountDeletionPolicyType

        from .shared_p_c_account_deletion_policy_type import SharedPCAccountDeletionPolicyType

        fields: dict[str, Callable[[Any], None]] = {
            "accountDeletionPolicy": lambda n : setattr(self, 'account_deletion_policy', n.get_enum_value(SharedPCAccountDeletionPolicyType)),
            "cacheAccountsAboveDiskFreePercentage": lambda n : setattr(self, 'cache_accounts_above_disk_free_percentage', n.get_int_value()),
            "inactiveThresholdDays": lambda n : setattr(self, 'inactive_threshold_days', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "removeAccountsBelowDiskFreePercentage": lambda n : setattr(self, 'remove_accounts_below_disk_free_percentage', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accountDeletionPolicy", self.account_deletion_policy)
        writer.write_int_value("cacheAccountsAboveDiskFreePercentage", self.cache_accounts_above_disk_free_percentage)
        writer.write_int_value("inactiveThresholdDays", self.inactive_threshold_days)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("removeAccountsBelowDiskFreePercentage", self.remove_accounts_below_disk_free_percentage)
        writer.write_additional_data_value(self.additional_data)
    

