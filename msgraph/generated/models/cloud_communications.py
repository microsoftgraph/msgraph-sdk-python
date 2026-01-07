from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .adhoc_call import AdhocCall
    from .call import Call
    from .call_records.call_record import CallRecord
    from .online_meeting import OnlineMeeting
    from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
    from .presence import Presence

@dataclass
class CloudCommunications(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a container that exposes navigation properties for cloud communications resources.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The adhocCalls property
    adhoc_calls: Optional[list[AdhocCall]] = None
    # The callRecords property
    call_records: Optional[list[CallRecord]] = None
    # The calls property
    calls: Optional[list[Call]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of structured question-and-answer (Q&A) threads in Teams directly associated with online meetings.
    online_meeting_conversations: Optional[list[OnlineMeetingEngagementConversation]] = None
    # The onlineMeetings property
    online_meetings: Optional[list[OnlineMeeting]] = None
    # The presences property
    presences: Optional[list[Presence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudCommunications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudCommunications
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudCommunications()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .adhoc_call import AdhocCall
        from .call import Call
        from .call_records.call_record import CallRecord
        from .online_meeting import OnlineMeeting
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
        from .presence import Presence

        from .adhoc_call import AdhocCall
        from .call import Call
        from .call_records.call_record import CallRecord
        from .online_meeting import OnlineMeeting
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
        from .presence import Presence

        fields: dict[str, Callable[[Any], None]] = {
            "adhocCalls": lambda n : setattr(self, 'adhoc_calls', n.get_collection_of_object_values(AdhocCall)),
            "callRecords": lambda n : setattr(self, 'call_records', n.get_collection_of_object_values(CallRecord)),
            "calls": lambda n : setattr(self, 'calls', n.get_collection_of_object_values(Call)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onlineMeetingConversations": lambda n : setattr(self, 'online_meeting_conversations', n.get_collection_of_object_values(OnlineMeetingEngagementConversation)),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(OnlineMeeting)),
            "presences": lambda n : setattr(self, 'presences', n.get_collection_of_object_values(Presence)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("adhocCalls", self.adhoc_calls)
        writer.write_collection_of_object_values("callRecords", self.call_records)
        writer.write_collection_of_object_values("calls", self.calls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("onlineMeetingConversations", self.online_meeting_conversations)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
        writer.write_collection_of_object_values("presences", self.presences)
        writer.write_additional_data_value(self.additional_data)
    

