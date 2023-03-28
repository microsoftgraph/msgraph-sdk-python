from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import day_of_week, time_zone_base

class WorkingHours(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new workingHours and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The days of the week on which the user works.
        self._days_of_week: Optional[List[day_of_week.DayOfWeek]] = None
        # The time of the day that the user stops working.
        self._end_time: Optional[time] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time of the day that the user starts working.
        self._start_time: Optional[time] = None
        # The time zone to which the working hours apply.
        self._time_zone: Optional[time_zone_base.TimeZoneBase] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkingHours:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkingHours
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkingHours()
    
    @property
    def days_of_week(self,) -> Optional[List[day_of_week.DayOfWeek]]:
        """
        Gets the daysOfWeek property value. The days of the week on which the user works.
        Returns: Optional[List[day_of_week.DayOfWeek]]
        """
        return self._days_of_week
    
    @days_of_week.setter
    def days_of_week(self,value: Optional[List[day_of_week.DayOfWeek]] = None) -> None:
        """
        Sets the daysOfWeek property value. The days of the week on which the user works.
        Args:
            value: Value to set for the days_of_week property.
        """
        self._days_of_week = value
    
    @property
    def end_time(self,) -> Optional[time]:
        """
        Gets the endTime property value. The time of the day that the user stops working.
        Returns: Optional[time]
        """
        return self._end_time
    
    @end_time.setter
    def end_time(self,value: Optional[time] = None) -> None:
        """
        Sets the endTime property value. The time of the day that the user stops working.
        Args:
            value: Value to set for the end_time property.
        """
        self._end_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import day_of_week, time_zone_base

        fields: Dict[str, Callable[[Any], None]] = {
            "daysOfWeek": lambda n : setattr(self, 'days_of_week', n.get_collection_of_enum_values(day_of_week.DayOfWeek)),
            "endTime": lambda n : setattr(self, 'end_time', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_time_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_object_value(time_zone_base.TimeZoneBase)),
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
            value: Value to set for the odata_type property.
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
        writer.write_enum_value("daysOfWeek", self.days_of_week)
        writer.write_time_value("endTime", self.end_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("startTime", self.start_time)
        writer.write_object_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_time(self,) -> Optional[time]:
        """
        Gets the startTime property value. The time of the day that the user starts working.
        Returns: Optional[time]
        """
        return self._start_time
    
    @start_time.setter
    def start_time(self,value: Optional[time] = None) -> None:
        """
        Sets the startTime property value. The time of the day that the user starts working.
        Args:
            value: Value to set for the start_time property.
        """
        self._start_time = value
    
    @property
    def time_zone(self,) -> Optional[time_zone_base.TimeZoneBase]:
        """
        Gets the timeZone property value. The time zone to which the working hours apply.
        Returns: Optional[time_zone_base.TimeZoneBase]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[time_zone_base.TimeZoneBase] = None) -> None:
        """
        Sets the timeZone property value. The time zone to which the working hours apply.
        Args:
            value: Value to set for the time_zone property.
        """
        self._time_zone = value
    

