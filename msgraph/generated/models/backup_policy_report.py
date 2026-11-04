from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .backup_count_statistics import BackupCountStatistics

@dataclass
class BackupPolicyReport(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The ID of the backup policy.
    backup_policy_id: Optional[str] = None
    # The countStatistics property
    count_statistics: Optional[BackupCountStatistics] = None
    # The display name of the backup policy.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupPolicyReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupPolicyReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupPolicyReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .backup_count_statistics import BackupCountStatistics

        from .backup_count_statistics import BackupCountStatistics

        fields: dict[str, Callable[[Any], None]] = {
            "backupPolicyId": lambda n : setattr(self, 'backup_policy_id', n.get_str_value()),
            "countStatistics": lambda n : setattr(self, 'count_statistics', n.get_object_value(BackupCountStatistics)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("backupPolicyId", self.backup_policy_id)
        writer.write_object_value("countStatistics", self.count_statistics)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

