from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .time_off_item import TimeOffItem

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class TimeOff(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.timeOff"
    # The draft version of this timeOff item that is viewable by managers. It must be shared before it's visible to team members. Required.
    draft_time_off: Optional[TimeOffItem] = None
    # The timeOff is marked for deletion, a process that is finalized when the schedule is shared.
    is_staged_for_deletion: Optional[bool] = None
    # The shared version of this timeOff that is viewable by both employees and managers. Updates to the sharedTimeOff property send notifications to users in the Teams client. Required.
    shared_time_off: Optional[TimeOffItem] = None
    # ID of the user assigned to the timeOff. Required.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeOff:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeOff
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeOff()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .time_off_item import TimeOffItem

        from .change_tracked_entity import ChangeTrackedEntity
        from .time_off_item import TimeOffItem

        fields: dict[str, Callable[[Any], None]] = {
            "draftTimeOff": lambda n : setattr(self, 'draft_time_off', n.get_object_value(TimeOffItem)),
            "isStagedForDeletion": lambda n : setattr(self, 'is_staged_for_deletion', n.get_bool_value()),
            "sharedTimeOff": lambda n : setattr(self, 'shared_time_off', n.get_object_value(TimeOffItem)),
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
        writer.write_object_value("draftTimeOff", self.draft_time_off)
        writer.write_bool_value("isStagedForDeletion", self.is_staged_for_deletion)
        writer.write_object_value("sharedTimeOff", self.shared_time_off)
        writer.write_str_value("userId", self.user_id)
    

