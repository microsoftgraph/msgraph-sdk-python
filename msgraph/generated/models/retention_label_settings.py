from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security.behavior_during_retention_period import BehaviorDuringRetentionPeriod

@dataclass
class RetentionLabelSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Describes the item behavior during retention period. Possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue. Read-only.
    behavior_during_retention_period: Optional[BehaviorDuringRetentionPeriod] = None
    # Specifies whether updates to document content are allowed. Read-only.
    is_content_update_allowed: Optional[bool] = None
    # Specifies whether the document deletion is allowed. Read-only.
    is_delete_allowed: Optional[bool] = None
    # Specifies whether you're allowed to change the retention label on the document. Read-only.
    is_label_update_allowed: Optional[bool] = None
    # Specifies whether updates to the item metadata (for example, the Title field) are blocked. Read-only.
    is_metadata_update_allowed: Optional[bool] = None
    # Specifies whether the item is locked. Read-write.
    is_record_locked: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionLabelSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionLabelSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionLabelSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .security.behavior_during_retention_period import BehaviorDuringRetentionPeriod

        from .security.behavior_during_retention_period import BehaviorDuringRetentionPeriod

        fields: Dict[str, Callable[[Any], None]] = {
            "behaviorDuringRetentionPeriod": lambda n : setattr(self, 'behavior_during_retention_period', n.get_enum_value(BehaviorDuringRetentionPeriod)),
            "isContentUpdateAllowed": lambda n : setattr(self, 'is_content_update_allowed', n.get_bool_value()),
            "isDeleteAllowed": lambda n : setattr(self, 'is_delete_allowed', n.get_bool_value()),
            "isLabelUpdateAllowed": lambda n : setattr(self, 'is_label_update_allowed', n.get_bool_value()),
            "isMetadataUpdateAllowed": lambda n : setattr(self, 'is_metadata_update_allowed', n.get_bool_value()),
            "isRecordLocked": lambda n : setattr(self, 'is_record_locked', n.get_bool_value()),
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
        writer.write_enum_value("behaviorDuringRetentionPeriod", self.behavior_during_retention_period)
        writer.write_bool_value("isContentUpdateAllowed", self.is_content_update_allowed)
        writer.write_bool_value("isDeleteAllowed", self.is_delete_allowed)
        writer.write_bool_value("isLabelUpdateAllowed", self.is_label_update_allowed)
        writer.write_bool_value("isMetadataUpdateAllowed", self.is_metadata_update_allowed)
        writer.write_bool_value("isRecordLocked", self.is_record_locked)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

