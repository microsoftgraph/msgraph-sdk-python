from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
    from .entity import Entity

from .entity import Entity

@dataclass
class DelegatedAdminCustomer(Entity):
    # The Microsoft Entra ID display name of the customer tenant. Read-only. Supports $orderby.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the management details of a service in the customer tenant that's managed by delegated administration.
    service_management_details: Optional[List[DelegatedAdminServiceManagementDetail]] = None
    # The Microsoft Entra ID-assigned tenant ID of the customer. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminCustomer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminCustomer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .entity import Entity

        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "serviceManagementDetails": lambda n : setattr(self, 'service_management_details', n.get_collection_of_object_values(DelegatedAdminServiceManagementDetail)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("serviceManagementDetails", self.service_management_details)
        writer.write_str_value("tenantId", self.tenant_id)
    

