from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_call_event_type = lazy_import('msgraph.generated.models.teamwork_call_event_type')

class CallStartedEventMessageDetail(event_message_detail.EventMessageDetail):
    @property
    def call_event_type(self,) -> Optional[teamwork_call_event_type.TeamworkCallEventType]:
        """
        Gets the callEventType property value. Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        Returns: Optional[teamwork_call_event_type.TeamworkCallEventType]
        """
        return self._call_event_type
    
    @call_event_type.setter
    def call_event_type(self,value: Optional[teamwork_call_event_type.TeamworkCallEventType] = None) -> None:
        """
        Sets the callEventType property value. Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        Args:
            value: Value to set for the callEventType property.
        """
        self._call_event_type = value
    
    @property
    def call_id(self,) -> Optional[str]:
        """
        Gets the callId property value. Unique identifier of the call.
        Returns: Optional[str]
        """
        return self._call_id
    
    @call_id.setter
    def call_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callId property value. Unique identifier of the call.
        Args:
            value: Value to set for the callId property.
        """
        self._call_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CallStartedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callStartedEventMessageDetail"
        # Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        self._call_event_type: Optional[teamwork_call_event_type.TeamworkCallEventType] = None
        # Unique identifier of the call.
        self._call_id: Optional[str] = None
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallStartedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallStartedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallStartedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_event_type": lambda n : setattr(self, 'call_event_type', n.get_enum_value(teamwork_call_event_type.TeamworkCallEventType)),
            "call_id": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_str_value("callId", self.call_id)
        writer.write_object_value("initiator", self.initiator)
    

