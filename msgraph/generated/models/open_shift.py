from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
open_shift_item = lazy_import('msgraph.generated.models.open_shift_item')

class OpenShift(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new OpenShift and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.openShift"
        # An unpublished open shift.
        self._draft_open_shift: Optional[open_shift_item.OpenShiftItem] = None
        # ID for the scheduling group that the open shift belongs to.
        self._scheduling_group_id: Optional[str] = None
        # A published open shift.
        self._shared_open_shift: Optional[open_shift_item.OpenShiftItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenShift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenShift
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OpenShift()
    
    @property
    def draft_open_shift(self,) -> Optional[open_shift_item.OpenShiftItem]:
        """
        Gets the draftOpenShift property value. An unpublished open shift.
        Returns: Optional[open_shift_item.OpenShiftItem]
        """
        return self._draft_open_shift
    
    @draft_open_shift.setter
    def draft_open_shift(self,value: Optional[open_shift_item.OpenShiftItem] = None) -> None:
        """
        Sets the draftOpenShift property value. An unpublished open shift.
        Args:
            value: Value to set for the draftOpenShift property.
        """
        self._draft_open_shift = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "draft_open_shift": lambda n : setattr(self, 'draft_open_shift', n.get_object_value(open_shift_item.OpenShiftItem)),
            "scheduling_group_id": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "shared_open_shift": lambda n : setattr(self, 'shared_open_shift', n.get_object_value(open_shift_item.OpenShiftItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scheduling_group_id(self,) -> Optional[str]:
        """
        Gets the schedulingGroupId property value. ID for the scheduling group that the open shift belongs to.
        Returns: Optional[str]
        """
        return self._scheduling_group_id
    
    @scheduling_group_id.setter
    def scheduling_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the schedulingGroupId property value. ID for the scheduling group that the open shift belongs to.
        Args:
            value: Value to set for the schedulingGroupId property.
        """
        self._scheduling_group_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("draftOpenShift", self.draft_open_shift)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedOpenShift", self.shared_open_shift)
    
    @property
    def shared_open_shift(self,) -> Optional[open_shift_item.OpenShiftItem]:
        """
        Gets the sharedOpenShift property value. A published open shift.
        Returns: Optional[open_shift_item.OpenShiftItem]
        """
        return self._shared_open_shift
    
    @shared_open_shift.setter
    def shared_open_shift(self,value: Optional[open_shift_item.OpenShiftItem] = None) -> None:
        """
        Sets the sharedOpenShift property value. A published open shift.
        Args:
            value: Value to set for the sharedOpenShift property.
        """
        self._shared_open_shift = value
    

