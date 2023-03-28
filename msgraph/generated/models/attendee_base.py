from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendee_type = lazy_import('msgraph.generated.models.attendee_type')
recipient = lazy_import('msgraph.generated.models.recipient')

class AttendeeBase(recipient.Recipient):
    def __init__(self,) -> None:
        """
        Instantiates a new AttendeeBase and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.attendeeBase"
        # The type of attendee. The possible values are: required, optional, resource. Currently if the attendee is a person, findMeetingTimes always considers the person is of the Required type.
        self._type: Optional[attendee_type.AttendeeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttendeeBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttendeeBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttendeeBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attendee_type.AttendeeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("type", self.type)
    
    @property
    def type(self,) -> Optional[attendee_type.AttendeeType]:
        """
        Gets the type property value. The type of attendee. The possible values are: required, optional, resource. Currently if the attendee is a person, findMeetingTimes always considers the person is of the Required type.
        Returns: Optional[attendee_type.AttendeeType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[attendee_type.AttendeeType] = None) -> None:
        """
        Sets the type property value. The type of attendee. The possible values are: required, optional, resource. Currently if the attendee is a person, findMeetingTimes always considers the person is of the Required type.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

