from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
endpoint = lazy_import('msgraph.generated.models.call_records.endpoint')
failure_info = lazy_import('msgraph.generated.models.call_records.failure_info')
modality = lazy_import('msgraph.generated.models.call_records.modality')
segment = lazy_import('msgraph.generated.models.call_records.segment')

class Session(entity.Entity):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    @property
    def callee(self,) -> Optional[endpoint.Endpoint]:
        """
        Gets the callee property value. Endpoint that answered the session.
        Returns: Optional[endpoint.Endpoint]
        """
        return self._callee
    
    @callee.setter
    def callee(self,value: Optional[endpoint.Endpoint] = None) -> None:
        """
        Sets the callee property value. Endpoint that answered the session.
        Args:
            value: Value to set for the callee property.
        """
        self._callee = value
    
    @property
    def caller(self,) -> Optional[endpoint.Endpoint]:
        """
        Gets the caller property value. Endpoint that initiated the session.
        Returns: Optional[endpoint.Endpoint]
        """
        return self._caller
    
    @caller.setter
    def caller(self,value: Optional[endpoint.Endpoint] = None) -> None:
        """
        Sets the caller property value. Endpoint that initiated the session.
        Args:
            value: Value to set for the caller property.
        """
        self._caller = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new session and sets the default values.
        """
        super().__init__()
        # Endpoint that answered the session.
        self._callee: Optional[endpoint.Endpoint] = None
        # Endpoint that initiated the session.
        self._caller: Optional[endpoint.Endpoint] = None
        # UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._end_date_time: Optional[datetime] = None
        # Failure information associated with the session if the session failed.
        self._failure_info: Optional[failure_info.FailureInfo] = None
        # List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        self._modalities: Optional[List[modality.Modality]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The list of segments involved in the session. Read-only. Nullable.
        self._segments: Optional[List[segment.Segment]] = None
        # UTC time when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Session:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Session
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Session()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def failure_info(self,) -> Optional[failure_info.FailureInfo]:
        """
        Gets the failureInfo property value. Failure information associated with the session if the session failed.
        Returns: Optional[failure_info.FailureInfo]
        """
        return self._failure_info
    
    @failure_info.setter
    def failure_info(self,value: Optional[failure_info.FailureInfo] = None) -> None:
        """
        Sets the failureInfo property value. Failure information associated with the session if the session failed.
        Args:
            value: Value to set for the failureInfo property.
        """
        self._failure_info = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callee": lambda n : setattr(self, 'callee', n.get_object_value(endpoint.Endpoint)),
            "caller": lambda n : setattr(self, 'caller', n.get_object_value(endpoint.Endpoint)),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failure_info": lambda n : setattr(self, 'failure_info', n.get_object_value(failure_info.FailureInfo)),
            "modalities": lambda n : setattr(self, 'modalities', n.get_collection_of_enum_values(modality.Modality)),
            "segments": lambda n : setattr(self, 'segments', n.get_collection_of_object_values(segment.Segment)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the modalities property value. List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        Returns: Optional[List[modality.Modality]]
        """
        return self._modalities
    
    @modalities.setter
    def modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the modalities property value. List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        Args:
            value: Value to set for the modalities property.
        """
        self._modalities = value
    
    @property
    def segments(self,) -> Optional[List[segment.Segment]]:
        """
        Gets the segments property value. The list of segments involved in the session. Read-only. Nullable.
        Returns: Optional[List[segment.Segment]]
        """
        return self._segments
    
    @segments.setter
    def segments(self,value: Optional[List[segment.Segment]] = None) -> None:
        """
        Sets the segments property value. The list of segments involved in the session. Read-only. Nullable.
        Args:
            value: Value to set for the segments property.
        """
        self._segments = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("callee", self.callee)
        writer.write_object_value("caller", self.caller)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("failureInfo", self.failure_info)
        writer.write_enum_value("modalities", self.modalities)
        writer.write_collection_of_object_values("segments", self.segments)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. UTC time when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. UTC time when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

