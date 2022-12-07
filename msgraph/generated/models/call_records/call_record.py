from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
call_type = lazy_import('msgraph.generated.models.call_records.call_type')
modality = lazy_import('msgraph.generated.models.call_records.modality')
session = lazy_import('msgraph.generated.models.call_records.session')

class CallRecord(entity.Entity):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new callRecord and sets the default values.
        """
        super().__init__()
        # UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._end_date_time: Optional[datetime] = None
        # Meeting URL associated to the call. May not be available for a peerToPeer call record type.
        self._join_web_url: Optional[str] = None
        # UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_modified_date_time: Optional[datetime] = None
        # List of all the modalities used in the call. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        self._modalities: Optional[List[modality.Modality]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The organizing party's identity.
        self._organizer: Optional[identity_set.IdentitySet] = None
        # List of distinct identities involved in the call.
        self._participants: Optional[List[identity_set.IdentitySet]] = None
        # List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.
        self._sessions: Optional[List[session.Session]] = None
        # UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._start_date_time: Optional[datetime] = None
        # The type property
        self._type: Optional[call_type.CallType] = None
        # Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.
        self._version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallRecord()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "modalities": lambda n : setattr(self, 'modalities', n.get_collection_of_enum_values(modality.Modality)),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(identity_set.IdentitySet)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(identity_set.IdentitySet)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(session.Session)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(call_type.CallType)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def join_web_url(self,) -> Optional[str]:
        """
        Gets the joinWebUrl property value. Meeting URL associated to the call. May not be available for a peerToPeer call record type.
        Returns: Optional[str]
        """
        return self._join_web_url
    
    @join_web_url.setter
    def join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinWebUrl property value. Meeting URL associated to the call. May not be available for a peerToPeer call record type.
        Args:
            value: Value to set for the joinWebUrl property.
        """
        self._join_web_url = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the modalities property value. List of all the modalities used in the call. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        Returns: Optional[List[modality.Modality]]
        """
        return self._modalities
    
    @modalities.setter
    def modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the modalities property value. List of all the modalities used in the call. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
        Args:
            value: Value to set for the modalities property.
        """
        self._modalities = value
    
    @property
    def organizer(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the organizer property value. The organizing party's identity.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._organizer
    
    @organizer.setter
    def organizer(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the organizer property value. The organizing party's identity.
        Args:
            value: Value to set for the organizer property.
        """
        self._organizer = value
    
    @property
    def participants(self,) -> Optional[List[identity_set.IdentitySet]]:
        """
        Gets the participants property value. List of distinct identities involved in the call.
        Returns: Optional[List[identity_set.IdentitySet]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[identity_set.IdentitySet]] = None) -> None:
        """
        Sets the participants property value. List of distinct identities involved in the call.
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("modalities", self.modalities)
        writer.write_object_value("organizer", self.organizer)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("version", self.version)
    
    @property
    def sessions(self,) -> Optional[List[session.Session]]:
        """
        Gets the sessions property value. List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.
        Returns: Optional[List[session.Session]]
        """
        return self._sessions
    
    @sessions.setter
    def sessions(self,value: Optional[List[session.Session]] = None) -> None:
        """
        Sets the sessions property value. List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.
        Args:
            value: Value to set for the sessions property.
        """
        self._sessions = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def type(self,) -> Optional[call_type.CallType]:
        """
        Gets the type property value. The type property
        Returns: Optional[call_type.CallType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[call_type.CallType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

