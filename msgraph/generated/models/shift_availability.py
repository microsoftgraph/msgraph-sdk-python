from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

patterned_recurrence = lazy_import('msgraph.generated.models.patterned_recurrence')
time_range = lazy_import('msgraph.generated.models.time_range')

class ShiftAvailability(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new shiftAvailability and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the pattern for recurrence
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The time slot(s) preferred by the user.
        self._time_slots: Optional[List[time_range.TimeRange]] = None
        # Specifies the time zone for the indicated time.
        self._time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ShiftAvailability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ShiftAvailability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ShiftAvailability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "time_slots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(time_range.TimeRange)),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
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
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. Specifies the pattern for recurrence
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. Specifies the pattern for recurrence
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_slots(self,) -> Optional[List[time_range.TimeRange]]:
        """
        Gets the timeSlots property value. The time slot(s) preferred by the user.
        Returns: Optional[List[time_range.TimeRange]]
        """
        return self._time_slots
    
    @time_slots.setter
    def time_slots(self,value: Optional[List[time_range.TimeRange]] = None) -> None:
        """
        Sets the timeSlots property value. The time slot(s) preferred by the user.
        Args:
            value: Value to set for the timeSlots property.
        """
        self._time_slots = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. Specifies the time zone for the indicated time.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. Specifies the time zone for the indicated time.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    

