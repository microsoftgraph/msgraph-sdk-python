from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_target

from . import device_and_app_management_assignment_target

class ConfigurationManagerCollectionAssignmentTarget(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget):
    def __init__(self,) -> None:
        """
        Instantiates a new ConfigurationManagerCollectionAssignmentTarget and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.configurationManagerCollectionAssignmentTarget"
        # The collection Id that is the target of the assignment.
        self._collection_id: Optional[str] = None
    
    @property
    def collection_id(self,) -> Optional[str]:
        """
        Gets the collectionId property value. The collection Id that is the target of the assignment.
        Returns: Optional[str]
        """
        return self._collection_id
    
    @collection_id.setter
    def collection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the collectionId property value. The collection Id that is the target of the assignment.
        Args:
            value: Value to set for the collection_id property.
        """
        self._collection_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigurationManagerCollectionAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerCollectionAssignmentTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigurationManagerCollectionAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_target

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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("collectionId", self.collection_id)
    

