from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object

from . import directory_object

@dataclass
class ResourceSpecificPermissionGrant(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.resourceSpecificPermissionGrant"
    # ID of the service principal of the Azure AD app that has been granted access. Read-only.
    client_app_id: Optional[str] = None
    # ID of the Azure AD app that has been granted access. Read-only.
    client_id: Optional[str] = None
    # The name of the resource-specific permission. Read-only.
    permission: Optional[str] = None
    # The type of permission. Possible values are: Application, Delegated. Read-only.
    permission_type: Optional[str] = None
    # ID of the Azure AD app that is hosting the resource. Read-only.
    resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceSpecificPermissionGrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceSpecificPermissionGrant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceSpecificPermissionGrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object

        fields: Dict[str, Callable[[Any], None]] = {
            "clientAppId": lambda n : setattr(self, 'client_app_id', n.get_str_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_str_value()),
            "resourceAppId": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
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
        writer.write_str_value("clientAppId", self.client_app_id)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("permission", self.permission)
        writer.write_str_value("permissionType", self.permission_type)
        writer.write_str_value("resourceAppId", self.resource_app_id)
    

