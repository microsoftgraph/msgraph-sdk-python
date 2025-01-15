from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .calendar import Calendar
    from .entity import Entity

from .entity import Entity

@dataclass
class CalendarGroup(Entity, Parsable):
    # The calendars in the calendar group. Navigation property. Read-only. Nullable.
    calendars: Optional[list[Calendar]] = None
    # Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
    change_key: Optional[str] = None
    # The class identifier. Read-only.
    class_id: Optional[UUID] = None
    # The group name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalendarGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalendarGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalendarGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .calendar import Calendar
        from .entity import Entity

        from .calendar import Calendar
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "calendars": lambda n : setattr(self, 'calendars', n.get_collection_of_object_values(Calendar)),
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "classId": lambda n : setattr(self, 'class_id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_collection_of_object_values("calendars", self.calendars)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_uuid_value("classId", self.class_id)
        writer.write_str_value("name", self.name)
    

