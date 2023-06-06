from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UnifiedRolePermission(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Set of tasks that can be performed on a resource. Required.
    allowed_resource_actions: Optional[List[str]] = None
    # Optional constraints that must be met for the permission to be effective. Not supported for custom roles.
    condition: Optional[str] = None
    # Set of tasks that may not be performed on a resource. Not yet supported.
    excluded_resource_actions: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRolePermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRolePermission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRolePermission()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedResourceActions": lambda n : setattr(self, 'allowed_resource_actions', n.get_collection_of_primitive_values(str)),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "excludedResourceActions": lambda n : setattr(self, 'excluded_resource_actions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("allowedResourceActions", self.allowed_resource_actions)
        writer.write_str_value("condition", self.condition)
        writer.write_collection_of_primitive_values("excludedResourceActions", self.excluded_resource_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

