from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')

class GetSchedulePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the getSchedule method.
    """
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
    def availability_view_interval(self,) -> Optional[int]:
        """
        Gets the availabilityViewInterval property value. The AvailabilityViewInterval property
        Returns: Optional[int]
        """
        return self._availability_view_interval
    
    @availability_view_interval.setter
    def availability_view_interval(self,value: Optional[int] = None) -> None:
        """
        Sets the availabilityViewInterval property value. The AvailabilityViewInterval property
        Args:
            value: Value to set for the AvailabilityViewInterval property.
        """
        self._availability_view_interval = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new getSchedulePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The AvailabilityViewInterval property
        self._availability_view_interval: Optional[int] = None
        # The EndTime property
        self._end_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The Schedules property
        self._schedules: Optional[List[str]] = None
        # The StartTime property
        self._start_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetSchedulePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetSchedulePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetSchedulePostRequestBody()
    
    @property
    def end_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the endTime property value. The EndTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end_time
    
    @end_time.setter
    def end_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the endTime property value. The EndTime property
        Args:
            value: Value to set for the EndTime property.
        """
        self._end_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "availability_view_interval": lambda n : setattr(self, 'availability_view_interval', n.get_int_value()),
            "end_time": lambda n : setattr(self, 'end_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "schedules": lambda n : setattr(self, 'schedules', n.get_collection_of_primitive_values(str)),
            "start_time": lambda n : setattr(self, 'start_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        return fields
    
    @property
    def schedules(self,) -> Optional[List[str]]:
        """
        Gets the schedules property value. The Schedules property
        Returns: Optional[List[str]]
        """
        return self._schedules
    
    @schedules.setter
    def schedules(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the schedules property value. The Schedules property
        Args:
            value: Value to set for the Schedules property.
        """
        self._schedules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("AvailabilityViewInterval", self.availability_view_interval)
        writer.write_object_value("EndTime", self.end_time)
        writer.write_collection_of_primitive_values("Schedules", self.schedules)
        writer.write_object_value("StartTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startTime property value. The StartTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_time
    
    @start_time.setter
    def start_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startTime property value. The StartTime property
        Args:
            value: Value to set for the StartTime property.
        """
        self._start_time = value
    

