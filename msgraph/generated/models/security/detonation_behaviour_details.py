from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DetonationBehaviourDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The status of the action performed during detonation (e.g., 'Successful', 'Failed', 'Blocked').
    action_status: Optional[str] = None
    # Categorizes the capability or type of behavior observed.
    behaviour_capability: Optional[str] = None
    # Groups related behaviors together for classification purposes.
    behaviour_group: Optional[str] = None
    # More contextual information about the observed behavior or action.
    details: Optional[str] = None
    # The date and time when the behavior or action was observed during detonation.
    event_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The specific operation or action that was performed.
    operation: Optional[str] = None
    # The unique identifier of the process involved in the behavior.
    process_id: Optional[str] = None
    # The name of the process that performed or was involved in the behavior.
    process_name: Optional[str] = None
    # The target of the operation.
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetonationBehaviourDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetonationBehaviourDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetonationBehaviourDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionStatus": lambda n : setattr(self, 'action_status', n.get_str_value()),
            "behaviourCapability": lambda n : setattr(self, 'behaviour_capability', n.get_str_value()),
            "behaviourGroup": lambda n : setattr(self, 'behaviour_group', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "processId": lambda n : setattr(self, 'process_id', n.get_str_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
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
        writer.write_str_value("actionStatus", self.action_status)
        writer.write_str_value("behaviourCapability", self.behaviour_capability)
        writer.write_str_value("behaviourGroup", self.behaviour_group)
        writer.write_str_value("details", self.details)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operation", self.operation)
        writer.write_str_value("processId", self.process_id)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

