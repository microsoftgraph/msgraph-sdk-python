from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DelegatedAdminServiceManagementDetail(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL of the management portal for the managed service. Read-only.
    service_management_url: Optional[str] = None
    # The name of a managed service. Read-only.
    service_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminServiceManagementDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminServiceManagementDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminServiceManagementDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "serviceManagementUrl": lambda n : setattr(self, 'service_management_url', n.get_str_value()),
            "serviceName": lambda n : setattr(self, 'service_name', n.get_str_value()),
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
        writer.write_str_value("serviceManagementUrl", self.service_management_url)
        writer.write_str_value("serviceName", self.service_name)
    

