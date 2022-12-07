from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')
time_off_item = lazy_import('msgraph.generated.models.time_off_item')

class TimeOff(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new TimeOff and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.timeOff"
        # The draft version of this timeOff that is viewable by managers. Required.
        self._draft_time_off: Optional[time_off_item.TimeOffItem] = None
        # The shared version of this timeOff that is viewable by both employees and managers. Required.
        self._shared_time_off: Optional[time_off_item.TimeOffItem] = None
        # ID of the user assigned to the timeOff. Required.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimeOff:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimeOff
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimeOff()
    
    @property
    def draft_time_off(self,) -> Optional[time_off_item.TimeOffItem]:
        """
        Gets the draftTimeOff property value. The draft version of this timeOff that is viewable by managers. Required.
        Returns: Optional[time_off_item.TimeOffItem]
        """
        return self._draft_time_off
    
    @draft_time_off.setter
    def draft_time_off(self,value: Optional[time_off_item.TimeOffItem] = None) -> None:
        """
        Sets the draftTimeOff property value. The draft version of this timeOff that is viewable by managers. Required.
        Args:
            value: Value to set for the draftTimeOff property.
        """
        self._draft_time_off = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "draft_time_off": lambda n : setattr(self, 'draft_time_off', n.get_object_value(time_off_item.TimeOffItem)),
            "shared_time_off": lambda n : setattr(self, 'shared_time_off', n.get_object_value(time_off_item.TimeOffItem)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("draftTimeOff", self.draft_time_off)
        writer.write_object_value("sharedTimeOff", self.shared_time_off)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def shared_time_off(self,) -> Optional[time_off_item.TimeOffItem]:
        """
        Gets the sharedTimeOff property value. The shared version of this timeOff that is viewable by both employees and managers. Required.
        Returns: Optional[time_off_item.TimeOffItem]
        """
        return self._shared_time_off
    
    @shared_time_off.setter
    def shared_time_off(self,value: Optional[time_off_item.TimeOffItem] = None) -> None:
        """
        Sets the sharedTimeOff property value. The shared version of this timeOff that is viewable by both employees and managers. Required.
        Args:
            value: Value to set for the sharedTimeOff property.
        """
        self._shared_time_off = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. ID of the user assigned to the timeOff. Required.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. ID of the user assigned to the timeOff. Required.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

