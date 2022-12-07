from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
free_busy_status = lazy_import('msgraph.generated.models.free_busy_status')

class ScheduleItem(AdditionalDataHolder, Parsable):
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
        Instantiates a new scheduleItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date, time, and time zone that the corresponding event ends.
        self._end: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The sensitivity of the corresponding event. True if the event is marked private, false otherwise. Optional.
        self._is_private: Optional[bool] = None
        # The location where the corresponding event is held or attended from. Optional.
        self._location: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date, time, and time zone that the corresponding event starts.
        self._start: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The availability status of the user or resource during the corresponding event. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        self._status: Optional[free_busy_status.FreeBusyStatus] = None
        # The corresponding event's subject line. Optional.
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScheduleItem()
    
    @property
    def end(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the end property value. The date, time, and time zone that the corresponding event ends.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end
    
    @end.setter
    def end(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the end property value. The date, time, and time zone that the corresponding event ends.
        Args:
            value: Value to set for the end property.
        """
        self._end = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end": lambda n : setattr(self, 'end', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "is_private": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(free_busy_status.FreeBusyStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        return fields
    
    @property
    def is_private(self,) -> Optional[bool]:
        """
        Gets the isPrivate property value. The sensitivity of the corresponding event. True if the event is marked private, false otherwise. Optional.
        Returns: Optional[bool]
        """
        return self._is_private
    
    @is_private.setter
    def is_private(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPrivate property value. The sensitivity of the corresponding event. True if the event is marked private, false otherwise. Optional.
        Args:
            value: Value to set for the isPrivate property.
        """
        self._is_private = value
    
    @property
    def location(self,) -> Optional[str]:
        """
        Gets the location property value. The location where the corresponding event is held or attended from. Optional.
        Returns: Optional[str]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[str] = None) -> None:
        """
        Sets the location property value. The location where the corresponding event is held or attended from. Optional.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
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
        writer.write_object_value("end", self.end)
        writer.write_bool_value("isPrivate", self.is_private)
        writer.write_str_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("start", self.start)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the start property value. The date, time, and time zone that the corresponding event starts.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start
    
    @start.setter
    def start(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the start property value. The date, time, and time zone that the corresponding event starts.
        Args:
            value: Value to set for the start property.
        """
        self._start = value
    
    @property
    def status(self,) -> Optional[free_busy_status.FreeBusyStatus]:
        """
        Gets the status property value. The availability status of the user or resource during the corresponding event. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Returns: Optional[free_busy_status.FreeBusyStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[free_busy_status.FreeBusyStatus] = None) -> None:
        """
        Sets the status property value. The availability status of the user or resource during the corresponding event. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The corresponding event's subject line. Optional.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The corresponding event's subject line. Optional.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

