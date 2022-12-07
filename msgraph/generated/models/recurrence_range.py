from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

recurrence_range_type = lazy_import('msgraph.generated.models.recurrence_range_type')

class RecurrenceRange(AdditionalDataHolder, Parsable):
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
        Instantiates a new recurrenceRange and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date to stop applying the recurrence pattern. Depending on the recurrence pattern of the event, the last occurrence of the meeting may not be this date. Required if type is endDate.
        self._end_date: Optional[Date] = None
        # The number of times to repeat the event. Required and must be positive if type is numbered.
        self._number_of_occurrences: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Time zone for the startDate and endDate properties. Optional. If not specified, the time zone of the event is used.
        self._recurrence_time_zone: Optional[str] = None
        # The date to start applying the recurrence pattern. The first occurrence of the meeting may be this date or later, depending on the recurrence pattern of the event. Must be the same value as the start property of the recurring event. Required.
        self._start_date: Optional[Date] = None
        # The recurrence range. The possible values are: endDate, noEnd, numbered. Required.
        self._type: Optional[recurrence_range_type.RecurrenceRangeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecurrenceRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecurrenceRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecurrenceRange()
    
    @property
    def end_date(self,) -> Optional[Date]:
        """
        Gets the endDate property value. The date to stop applying the recurrence pattern. Depending on the recurrence pattern of the event, the last occurrence of the meeting may not be this date. Required if type is endDate.
        Returns: Optional[Date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the endDate property value. The date to stop applying the recurrence pattern. Depending on the recurrence pattern of the event, the last occurrence of the meeting may not be this date. Required if type is endDate.
        Args:
            value: Value to set for the endDate property.
        """
        self._end_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date": lambda n : setattr(self, 'end_date', n.get_object_value(Date)),
            "number_of_occurrences": lambda n : setattr(self, 'number_of_occurrences', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence_time_zone": lambda n : setattr(self, 'recurrence_time_zone', n.get_str_value()),
            "start_date": lambda n : setattr(self, 'start_date', n.get_object_value(Date)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(recurrence_range_type.RecurrenceRangeType)),
        }
        return fields
    
    @property
    def number_of_occurrences(self,) -> Optional[int]:
        """
        Gets the numberOfOccurrences property value. The number of times to repeat the event. Required and must be positive if type is numbered.
        Returns: Optional[int]
        """
        return self._number_of_occurrences
    
    @number_of_occurrences.setter
    def number_of_occurrences(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfOccurrences property value. The number of times to repeat the event. Required and must be positive if type is numbered.
        Args:
            value: Value to set for the numberOfOccurrences property.
        """
        self._number_of_occurrences = value
    
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
    def recurrence_time_zone(self,) -> Optional[str]:
        """
        Gets the recurrenceTimeZone property value. Time zone for the startDate and endDate properties. Optional. If not specified, the time zone of the event is used.
        Returns: Optional[str]
        """
        return self._recurrence_time_zone
    
    @recurrence_time_zone.setter
    def recurrence_time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the recurrenceTimeZone property value. Time zone for the startDate and endDate properties. Optional. If not specified, the time zone of the event is used.
        Args:
            value: Value to set for the recurrenceTimeZone property.
        """
        self._recurrence_time_zone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("endDate", self.end_date)
        writer.write_int_value("numberOfOccurrences", self.number_of_occurrences)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recurrenceTimeZone", self.recurrence_time_zone)
        writer.write_object_value("startDate", self.start_date)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date(self,) -> Optional[Date]:
        """
        Gets the startDate property value. The date to start applying the recurrence pattern. The first occurrence of the meeting may be this date or later, depending on the recurrence pattern of the event. Must be the same value as the start property of the recurring event. Required.
        Returns: Optional[Date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the startDate property value. The date to start applying the recurrence pattern. The first occurrence of the meeting may be this date or later, depending on the recurrence pattern of the event. Must be the same value as the start property of the recurring event. Required.
        Args:
            value: Value to set for the startDate property.
        """
        self._start_date = value
    
    @property
    def type(self,) -> Optional[recurrence_range_type.RecurrenceRangeType]:
        """
        Gets the type property value. The recurrence range. The possible values are: endDate, noEnd, numbered. Required.
        Returns: Optional[recurrence_range_type.RecurrenceRangeType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[recurrence_range_type.RecurrenceRangeType] = None) -> None:
        """
        Sets the type property value. The recurrence range. The possible values are: endDate, noEnd, numbered. Required.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

