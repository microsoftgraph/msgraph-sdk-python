from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call, online_meeting, presence
    from .call_records import call_record

class CloudCommunications(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudCommunications and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The callRecords property
        self._call_records: Optional[List[call_record.CallRecord]] = None
        # The calls property
        self._calls: Optional[List[call.Call]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The onlineMeetings property
        self._online_meetings: Optional[List[online_meeting.OnlineMeeting]] = None
        # The presences property
        self._presences: Optional[List[presence.Presence]] = None
    
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
            value: Value to set for the call_records property.
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
        from . import call, online_meeting, presence
        from .call_records import call_record

        fields: Dict[str, Callable[[Any], None]] = {
            "calls": lambda n : setattr(self, 'calls', n.get_collection_of_object_values(call.Call)),
            "callRecords": lambda n : setattr(self, 'call_records', n.get_collection_of_object_values(call_record.CallRecord)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(online_meeting.OnlineMeeting)),
            "presences": lambda n : setattr(self, 'presences', n.get_collection_of_object_values(presence.Presence)),
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
            value: Value to set for the online_meetings property.
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
        writer.write_collection_of_object_values("calls", self.calls)
        writer.write_collection_of_object_values("callRecords", self.call_records)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_collection_of_object_values("presences", self.presences)
        writer.write_additional_data_value(self.additional_data)
    

