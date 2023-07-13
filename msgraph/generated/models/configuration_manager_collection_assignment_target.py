from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

@dataclass
class ConfigurationManagerCollectionAssignmentTarget(DeviceAndAppManagementAssignmentTarget):
    """
    Represents an assignment to a Configuration Manager Collection.
    """
    odata_type = "#microsoft.graph.configurationManagerCollectionAssignmentTarget"
    # The collection Id that is the target of the assignment.
    collection_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerCollectionAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerCollectionAssignmentTarget
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagerCollectionAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "collectionId": lambda n : setattr(self, 'collection_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("collectionId", self.collection_id)
    

