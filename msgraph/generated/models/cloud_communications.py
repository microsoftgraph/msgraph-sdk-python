from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

call = lazy_import('msgraph.generated.models.call')
entity = lazy_import('msgraph.generated.models.entity')
online_meeting = lazy_import('msgraph.generated.models.online_meeting')
presence = lazy_import('msgraph.generated.models.presence')
call_record = lazy_import('msgraph.generated.models.call_records.call_record')

class CloudCommunications(entity.Entity):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    @property
    def call_records(self,) -> Optional[List[call_record.CallRecord]]:
        """
        Gets the callRecords property value. The callRecords property
        Returns: Optional[List[call_record.CallRecord]]
        """
        return self._call_records
    
    @call_records.setter
    def call_records(self,value: Optional[List[call_record.CallRecord]] = None) -> None:
        """
        Sets the callRecords property value. The callRecords property
        Args:
            value: Value to set for the callRecords property.
        """
        self._call_records = value
    
    @property
    def calls(self,) -> Optional[List[call.Call]]:
        """
        Gets the calls property value. The calls property
        Returns: Optional[List[call.Call]]
        """
        return self._calls
    
    @calls.setter
    def calls(self,value: Optional[List[call.Call]] = None) -> None:
        """
        Sets the calls property value. The calls property
        Args:
            value: Value to set for the calls property.
        """
        self._calls = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudCommunications and sets the default values.
        """
        super().__init__()
        # The callRecords property
        self._call_records: Optional[List[call_record.CallRecord]] = None
        # The calls property
        self._calls: Optional[List[call.Call]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The onlineMeetings property
        self._online_meetings: Optional[List[online_meeting.OnlineMeeting]] = None
        # The presences property
        self._presences: Optional[List[presence.Presence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudCommunications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudCommunications
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudCommunications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_records": lambda n : setattr(self, 'call_records', n.get_collection_of_object_values(call_record.CallRecord)),
            "calls": lambda n : setattr(self, 'calls', n.get_collection_of_object_values(call.Call)),
            "online_meetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(online_meeting.OnlineMeeting)),
            "presences": lambda n : setattr(self, 'presences', n.get_collection_of_object_values(presence.Presence)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def online_meetings(self,) -> Optional[List[online_meeting.OnlineMeeting]]:
        """
        Gets the onlineMeetings property value. The onlineMeetings property
        Returns: Optional[List[online_meeting.OnlineMeeting]]
        """
        return self._online_meetings
    
    @online_meetings.setter
    def online_meetings(self,value: Optional[List[online_meeting.OnlineMeeting]] = None) -> None:
        """
        Sets the onlineMeetings property value. The onlineMeetings property
        Args:
            value: Value to set for the onlineMeetings property.
        """
        self._online_meetings = value
    
    @property
    def presences(self,) -> Optional[List[presence.Presence]]:
        """
        Gets the presences property value. The presences property
        Returns: Optional[List[presence.Presence]]
        """
        return self._presences
    
    @presences.setter
    def presences(self,value: Optional[List[presence.Presence]] = None) -> None:
        """
        Sets the presences property value. The presences property
        Args:
            value: Value to set for the presences property.
        """
        self._presences = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("callRecords", self.call_records)
        writer.write_collection_of_object_values("calls", self.calls)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_collection_of_object_values("presences", self.presences)
    

