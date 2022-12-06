from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_tracked_entity = lazy_import('msgraph.generated.models.change_tracked_entity')

class SchedulingGroup(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new SchedulingGroup and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.schedulingGroup"
        # The display name for the schedulingGroup. Required.
        self._display_name: Optional[str] = None
        # Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.
        self._is_active: Optional[bool] = None
        # The list of user IDs that are a member of the schedulingGroup. Required.
        self._user_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SchedulingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SchedulingGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SchedulingGroup()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the schedulingGroup. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the schedulingGroup. Required.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "user_ids": lambda n : setattr(self, 'user_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("userIds", self.user_ids)
    
    @property
    def user_ids(self,) -> Optional[List[str]]:
        """
        Gets the userIds property value. The list of user IDs that are a member of the schedulingGroup. Required.
        Returns: Optional[List[str]]
        """
        return self._user_ids
    
    @user_ids.setter
    def user_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the userIds property value. The list of user IDs that are a member of the schedulingGroup. Required.
        Args:
            value: Value to set for the userIds property.
        """
        self._user_ids = value
    

