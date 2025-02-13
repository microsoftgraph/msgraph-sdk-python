from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .item_body import ItemBody

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class DayNote(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.dayNote"
    # The date of the day note.
    day_note_date: Optional[datetime.date] = None
    # The draft version of this day note that is viewable by managers. Only contentType text is supported.
    draft_day_note: Optional[ItemBody] = None
    # The shared version of this day note that is viewable by both employees and managers. Only contentType text is supported.
    shared_day_note: Optional[ItemBody] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DayNote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DayNote
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DayNote()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .item_body import ItemBody

        from .change_tracked_entity import ChangeTrackedEntity
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "dayNoteDate": lambda n : setattr(self, 'day_note_date', n.get_date_value()),
            "draftDayNote": lambda n : setattr(self, 'draft_day_note', n.get_object_value(ItemBody)),
            "sharedDayNote": lambda n : setattr(self, 'shared_day_note', n.get_object_value(ItemBody)),
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
        writer.write_date_value("dayNoteDate", self.day_note_date)
        writer.write_object_value("draftDayNote", self.draft_day_note)
        writer.write_object_value("sharedDayNote", self.shared_day_note)
    

