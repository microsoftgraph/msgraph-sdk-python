from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_item import ActionItem
    from .call_ai_insight_view_point import CallAiInsightViewPoint
    from .entity import Entity
    from .meeting_note import MeetingNote

from .entity import Entity

@dataclass
class CallAiInsight(Entity, Parsable):
    # The actionItems property
    action_items: Optional[list[ActionItem]] = None
    # The callId property
    call_id: Optional[str] = None
    # The contentCorrelationId property
    content_correlation_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The meetingNotes property
    meeting_notes: Optional[list[MeetingNote]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The viewpoint property
    viewpoint: Optional[CallAiInsightViewPoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallAiInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallAiInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallAiInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_item import ActionItem
        from .call_ai_insight_view_point import CallAiInsightViewPoint
        from .entity import Entity
        from .meeting_note import MeetingNote

        from .action_item import ActionItem
        from .call_ai_insight_view_point import CallAiInsightViewPoint
        from .entity import Entity
        from .meeting_note import MeetingNote

        fields: dict[str, Callable[[Any], None]] = {
            "actionItems": lambda n : setattr(self, 'action_items', n.get_collection_of_object_values(ActionItem)),
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "contentCorrelationId": lambda n : setattr(self, 'content_correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "meetingNotes": lambda n : setattr(self, 'meeting_notes', n.get_collection_of_object_values(MeetingNote)),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(CallAiInsightViewPoint)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("actionItems", self.action_items)
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("contentCorrelationId", self.content_correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("meetingNotes", self.meeting_notes)
        writer.write_object_value("viewpoint", self.viewpoint)
    

