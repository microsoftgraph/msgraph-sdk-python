from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message = lazy_import('msgraph.generated.models.event_message')
response_type = lazy_import('msgraph.generated.models.response_type')
time_slot = lazy_import('msgraph.generated.models.time_slot')

class EventMessageResponse(event_message.EventMessage):
    def __init__(self,) -> None:
        """
        Instantiates a new EventMessageResponse and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.eventMessageResponse"
        # The proposedNewTime property
        self._proposed_new_time: Optional[time_slot.TimeSlot] = None
        # The responseType property
        self._response_type: Optional[response_type.ResponseType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessageResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventMessageResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "proposed_new_time": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(time_slot.TimeSlot)),
            "response_type": lambda n : setattr(self, 'response_type', n.get_enum_value(response_type.ResponseType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proposed_new_time(self,) -> Optional[time_slot.TimeSlot]:
        """
        Gets the proposedNewTime property value. The proposedNewTime property
        Returns: Optional[time_slot.TimeSlot]
        """
        return self._proposed_new_time
    
    @proposed_new_time.setter
    def proposed_new_time(self,value: Optional[time_slot.TimeSlot] = None) -> None:
        """
        Sets the proposedNewTime property value. The proposedNewTime property
        Args:
            value: Value to set for the proposedNewTime property.
        """
        self._proposed_new_time = value
    
    @property
    def response_type(self,) -> Optional[response_type.ResponseType]:
        """
        Gets the responseType property value. The responseType property
        Returns: Optional[response_type.ResponseType]
        """
        return self._response_type
    
    @response_type.setter
    def response_type(self,value: Optional[response_type.ResponseType] = None) -> None:
        """
        Sets the responseType property value. The responseType property
        Args:
            value: Value to set for the responseType property.
        """
        self._response_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_enum_value("responseType", self.response_type)
    

