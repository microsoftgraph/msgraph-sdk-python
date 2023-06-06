from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_propagation_status

@dataclass
class EventPropagationResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The name of the specific location in the workload associated with the event.
    location: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the workload associated with the event.
    service_name: Optional[str] = None
    # Indicates the status of the event creation request. The possible values are: none, inProcessing, failed, success, unknownFutureValue.
    status: Optional[event_propagation_status.EventPropagationStatus] = None
    # Additional information about the status of the event creation request.
    status_information: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventPropagationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventPropagationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventPropagationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_propagation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceName": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(event_propagation_status.EventPropagationStatus)),
            "statusInformation": lambda n : setattr(self, 'status_information', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusInformation", self.status_information)
        writer.write_additional_data_value(self.additional_data)
    

