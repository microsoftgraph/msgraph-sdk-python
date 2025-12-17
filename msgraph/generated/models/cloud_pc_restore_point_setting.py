from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_restore_point_frequency_type import CloudPcRestorePointFrequencyType

@dataclass
class CloudPcRestorePointSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The time interval in hours to take snapshots (restore points) of a Cloud PC automatically. The possible values are: default, fourHours, sixHours, twelveHours, sixteenHours, twentyFourHours, unknownFutureValue. The default value is default that indicates that the time interval for automatic capturing of restore point snapshots is set to 12 hours.
    frequency_type: Optional[CloudPcRestorePointFrequencyType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If true, the user has the ability to use snapshots to restore Cloud PCs. If false, non-admin users can't use snapshots to restore the Cloud PC.
    user_restore_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcRestorePointSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRestorePointSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcRestorePointSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_restore_point_frequency_type import CloudPcRestorePointFrequencyType

        from .cloud_pc_restore_point_frequency_type import CloudPcRestorePointFrequencyType

        fields: dict[str, Callable[[Any], None]] = {
            "frequencyType": lambda n : setattr(self, 'frequency_type', n.get_enum_value(CloudPcRestorePointFrequencyType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userRestoreEnabled": lambda n : setattr(self, 'user_restore_enabled', n.get_bool_value()),
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
        writer.write_enum_value("frequencyType", self.frequency_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("userRestoreEnabled", self.user_restore_enabled)
        writer.write_additional_data_value(self.additional_data)
    

