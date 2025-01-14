from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceScope(Entity, Parsable):
    # The description of the scope.
    description: Optional[str] = None
    # The display name of the scope.
    display_name: Optional[str] = None
    # True if the scopes are arranged in a hierarchy and this is the top or root scope of the resource.
    is_root_scope: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the scope in the resource as defined in the origin system.
    origin_id: Optional[str] = None
    # The origin system for the scope.
    origin_system: Optional[str] = None
    # The resource property
    resource: Optional[AccessPackageResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRootScope": lambda n : setattr(self, 'is_root_scope', n.get_bool_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AccessPackageResource)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRootScope", self.is_root_scope)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_object_value("resource", self.resource)
    

