from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AttendanceInterval(AdditionalDataHolder, Parsable):
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
        Instantiates a new attendanceInterval and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Duration of the meeting interval in seconds; that is, the difference between joinDateTime and leaveDateTime.
        self._duration_in_seconds: Optional[int] = None
        # The time the attendee joined in UTC.
        self._join_date_time: Optional[datetime] = None
        # The time the attendee left in UTC.
        self._leave_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttendanceInterval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttendanceInterval
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttendanceInterval()
    
    @property
    def duration_in_seconds(self,) -> Optional[int]:
        """
        Gets the durationInSeconds property value. Duration of the meeting interval in seconds; that is, the difference between joinDateTime and leaveDateTime.
        Returns: Optional[int]
        """
        return self._duration_in_seconds
    
    @duration_in_seconds.setter
    def duration_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInSeconds property value. Duration of the meeting interval in seconds; that is, the difference between joinDateTime and leaveDateTime.
        Args:
            value: Value to set for the durationInSeconds property.
        """
        self._duration_in_seconds = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "duration_in_seconds": lambda n : setattr(self, 'duration_in_seconds', n.get_int_value()),
            "join_date_time": lambda n : setattr(self, 'join_date_time', n.get_datetime_value()),
            "leave_date_time": lambda n : setattr(self, 'leave_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def join_date_time(self,) -> Optional[datetime]:
        """
        Gets the joinDateTime property value. The time the attendee joined in UTC.
        Returns: Optional[datetime]
        """
        return self._join_date_time
    
    @join_date_time.setter
    def join_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the joinDateTime property value. The time the attendee joined in UTC.
        Args:
            value: Value to set for the joinDateTime property.
        """
        self._join_date_time = value
    
    @property
    def leave_date_time(self,) -> Optional[datetime]:
        """
        Gets the leaveDateTime property value. The time the attendee left in UTC.
        Returns: Optional[datetime]
        """
        return self._leave_date_time
    
    @leave_date_time.setter
    def leave_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the leaveDateTime property value. The time the attendee left in UTC.
        Args:
            value: Value to set for the leaveDateTime property.
        """
        self._leave_date_time = value
    
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
        writer.write_int_value("durationInSeconds", self.duration_in_seconds)
        writer.write_datetime_value("joinDateTime", self.join_date_time)
        writer.write_datetime_value("leaveDateTime", self.leave_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

