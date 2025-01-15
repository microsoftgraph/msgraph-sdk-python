from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .open_shift_item import OpenShiftItem

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class OpenShift(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.openShift"
    # Draft changes in the openShift are only visible to managers until they're shared.
    draft_open_shift: Optional[OpenShiftItem] = None
    # The openShift is marked for deletion, a process that is finalized when the schedule is shared.
    is_staged_for_deletion: Optional[bool] = None
    # The ID of the schedulingGroup that contains the openShift.
    scheduling_group_id: Optional[str] = None
    # The shared version of this openShift that is viewable by both employees and managers.
    shared_open_shift: Optional[OpenShiftItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenShift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenShift
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenShift()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .open_shift_item import OpenShiftItem

        from .change_tracked_entity import ChangeTrackedEntity
        from .open_shift_item import OpenShiftItem

        fields: dict[str, Callable[[Any], None]] = {
            "draftOpenShift": lambda n : setattr(self, 'draft_open_shift', n.get_object_value(OpenShiftItem)),
            "isStagedForDeletion": lambda n : setattr(self, 'is_staged_for_deletion', n.get_bool_value()),
            "schedulingGroupId": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "sharedOpenShift": lambda n : setattr(self, 'shared_open_shift', n.get_object_value(OpenShiftItem)),
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
        writer.write_object_value("draftOpenShift", self.draft_open_shift)
        writer.write_bool_value("isStagedForDeletion", self.is_staged_for_deletion)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedOpenShift", self.shared_open_shift)
    

