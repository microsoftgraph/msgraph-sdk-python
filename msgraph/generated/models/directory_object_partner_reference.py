from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class DirectoryObjectPartnerReference(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.directoryObjectPartnerReference"
    # Description of the object returned. Read-only.
    description: Optional[str] = None
    # Name of directory object being returned, like group or application. Read-only.
    display_name: Optional[str] = None
    # The tenant identifier for the partner tenant. Read-only.
    external_partner_tenant_id: Optional[UUID] = None
    # The type of the referenced object in the partner tenant. Read-only.
    object_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryObjectPartnerReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryObjectPartnerReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectoryObjectPartnerReference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalPartnerTenantId": lambda n : setattr(self, 'external_partner_tenant_id', n.get_uuid_value()),
            "objectType": lambda n : setattr(self, 'object_type', n.get_str_value()),
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
        writer.write_uuid_value("externalPartnerTenantId", self.external_partner_tenant_id)
        writer.write_str_value("objectType", self.object_type)
    

