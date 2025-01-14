from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_source import IdentitySource

from .identity_source import IdentitySource

@dataclass
class CrossCloudAzureActiveDirectoryTenant(IdentitySource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.crossCloudAzureActiveDirectoryTenant"
    # The ID of the cloud where the tenant is located, one of microsoftonline.com, microsoftonline.us or partner.microsoftonline.cn. Read only.
    cloud_instance: Optional[str] = None
    # The name of the Microsoft Entra tenant. Read only.
    display_name: Optional[str] = None
    # The ID of the Microsoft Entra tenant. Read only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossCloudAzureActiveDirectoryTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossCloudAzureActiveDirectoryTenant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossCloudAzureActiveDirectoryTenant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_source import IdentitySource

        from .identity_source import IdentitySource

        fields: dict[str, Callable[[Any], None]] = {
            "cloudInstance": lambda n : setattr(self, 'cloud_instance', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("cloudInstance", self.cloud_instance)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    

