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
class RemoteTenantGroup(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.remoteTenantGroup"
    # Display name of the group in the remote tenant.
    remote_group_display_name: Optional[str] = None
    # Unique identifier of the group in the remote tenant.
    remote_group_id: Optional[UUID] = None
    # Display name of the remote tenant.
    remote_tenant_display_name: Optional[str] = None
    # Unique identifier of the remote tenant.
    remote_tenant_id: Optional[UUID] = None
    # Primary domain name of the remote tenant.
    remote_tenant_primary_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemoteTenantGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteTenantGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemoteTenantGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "remoteGroupDisplayName": lambda n : setattr(self, 'remote_group_display_name', n.get_str_value()),
            "remoteGroupId": lambda n : setattr(self, 'remote_group_id', n.get_uuid_value()),
            "remoteTenantDisplayName": lambda n : setattr(self, 'remote_tenant_display_name', n.get_str_value()),
            "remoteTenantId": lambda n : setattr(self, 'remote_tenant_id', n.get_uuid_value()),
            "remoteTenantPrimaryDomain": lambda n : setattr(self, 'remote_tenant_primary_domain', n.get_str_value()),
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
        writer.write_str_value("remoteGroupDisplayName", self.remote_group_display_name)
        writer.write_uuid_value("remoteGroupId", self.remote_group_id)
        writer.write_str_value("remoteTenantDisplayName", self.remote_tenant_display_name)
        writer.write_uuid_value("remoteTenantId", self.remote_tenant_id)
        writer.write_str_value("remoteTenantPrimaryDomain", self.remote_tenant_primary_domain)
    

