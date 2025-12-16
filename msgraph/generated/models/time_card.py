from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .confirmed_by import ConfirmedBy
    from .item_body import ItemBody
    from .time_card_break import TimeCardBreak
    from .time_card_entry import TimeCardEntry
    from .time_card_event import TimeCardEvent
    from .time_card_state import TimeCardState

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class TimeCard(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.timeCard"
    # The list of breaks associated with the timeCard.
    breaks: Optional[list[TimeCardBreak]] = None
    # The clock-in event of the timeCard.
    clock_in_event: Optional[TimeCardEvent] = None
    # The clock-out event of the timeCard.
    clock_out_event: Optional[TimeCardEvent] = None
    # Indicates whether this timeCard entry is confirmed. The possible values are: none, user, manager, unknownFutureValue.
    confirmed_by: Optional[ConfirmedBy] = None
    # Notes about the timeCard.
    notes: Optional[ItemBody] = None
    # The original timeCardEntry of the timeCard before it was edited.
    original_entry: Optional[TimeCardEntry] = None
    # The current state of the timeCard during its life cycle. The possible values are: clockedIn, onBreak, clockedOut, unknownFutureValue.
    state: Optional[TimeCardState] = None
    # User ID to which the timeCard belongs.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeCard:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeCard
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeCard()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .confirmed_by import ConfirmedBy
        from .item_body import ItemBody
        from .time_card_break import TimeCardBreak
        from .time_card_entry import TimeCardEntry
        from .time_card_event import TimeCardEvent
        from .time_card_state import TimeCardState

        from .change_tracked_entity import ChangeTrackedEntity
        from .confirmed_by import ConfirmedBy
        from .item_body import ItemBody
        from .time_card_break import TimeCardBreak
        from .time_card_entry import TimeCardEntry
        from .time_card_event import TimeCardEvent
        from .time_card_state import TimeCardState

        fields: dict[str, Callable[[Any], None]] = {
            "breaks": lambda n : setattr(self, 'breaks', n.get_collection_of_object_values(TimeCardBreak)),
            "clockInEvent": lambda n : setattr(self, 'clock_in_event', n.get_object_value(TimeCardEvent)),
            "clockOutEvent": lambda n : setattr(self, 'clock_out_event', n.get_object_value(TimeCardEvent)),
            "confirmedBy": lambda n : setattr(self, 'confirmed_by', n.get_collection_of_enum_values(ConfirmedBy)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "originalEntry": lambda n : setattr(self, 'original_entry', n.get_object_value(TimeCardEntry)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(TimeCardState)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("breaks", self.breaks)
        writer.write_object_value("clockInEvent", self.clock_in_event)
        writer.write_object_value("clockOutEvent", self.clock_out_event)
        writer.write_enum_value("confirmedBy", self.confirmed_by)
        writer.write_object_value("notes", self.notes)
        writer.write_object_value("originalEntry", self.original_entry)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userId", self.user_id)
    

