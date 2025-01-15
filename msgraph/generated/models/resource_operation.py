from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ResourceOperation(Entity, Parsable):
    """
    Describes the resourceOperation resource (entity) of the Microsoft Graph API (REST), which supports Intune workflows related to role-based access control (RBAC).
    """
    # Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
    action_name: Optional[str] = None
    # Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the Resource this operation is performed on.
    resource_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourceOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("resourceName", self.resource_name)
    

