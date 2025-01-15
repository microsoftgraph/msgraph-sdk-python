from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

@dataclass
class ConfigurationManagerCollectionAssignmentTarget(DeviceAndAppManagementAssignmentTarget, Parsable):
    """
    Represents an assignment to a Configuration Manager Collection.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.configurationManagerCollectionAssignmentTarget"
    # The collection Id that is the target of the assignment.
    collection_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationManagerCollectionAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerCollectionAssignmentTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagerCollectionAssignmentTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

        fields: dict[str, Callable[[Any], None]] = {
            "collectionId": lambda n : setattr(self, 'collection_id', n.get_str_value()),
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
        writer.write_str_value("collectionId", self.collection_id)
    

