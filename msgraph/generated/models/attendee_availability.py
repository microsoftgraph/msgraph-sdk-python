from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendee_base = lazy_import('msgraph.generated.models.attendee_base')
free_busy_status = lazy_import('msgraph.generated.models.free_busy_status')

class AttendeeAvailability(AdditionalDataHolder, Parsable):
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
    def attendee(self,) -> Optional[attendee_base.AttendeeBase]:
        """
        Gets the attendee property value. The email address and type of attendee - whether it's a person or a resource, and whether required or optional if it's a person.
        Returns: Optional[attendee_base.AttendeeBase]
        """
        return self._attendee
    
    @attendee.setter
    def attendee(self,value: Optional[attendee_base.AttendeeBase] = None) -> None:
        """
        Sets the attendee property value. The email address and type of attendee - whether it's a person or a resource, and whether required or optional if it's a person.
        Args:
            value: Value to set for the attendee property.
        """
        self._attendee = value
    
    @property
    def availability(self,) -> Optional[free_busy_status.FreeBusyStatus]:
        """
        Gets the availability property value. The availability status of the attendee. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Returns: Optional[free_busy_status.FreeBusyStatus]
        """
        return self._availability
    
    @availability.setter
    def availability(self,value: Optional[free_busy_status.FreeBusyStatus] = None) -> None:
        """
        Sets the availability property value. The availability status of the attendee. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Args:
            value: Value to set for the availability property.
        """
        self._availability = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attendeeAvailability and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The email address and type of attendee - whether it's a person or a resource, and whether required or optional if it's a person.
        self._attendee: Optional[attendee_base.AttendeeBase] = None
        # The availability status of the attendee. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        self._availability: Optional[free_busy_status.FreeBusyStatus] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttendeeAvailability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttendeeAvailability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttendeeAvailability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attendee": lambda n : setattr(self, 'attendee', n.get_object_value(attendee_base.AttendeeBase)),
            "availability": lambda n : setattr(self, 'availability', n.get_enum_value(free_busy_status.FreeBusyStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("attendee", self.attendee)
        writer.write_enum_value("availability", self.availability)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

