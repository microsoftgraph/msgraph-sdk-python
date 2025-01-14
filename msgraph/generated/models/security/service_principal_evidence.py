from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .service_principal_type import ServicePrincipalType

from .alert_evidence import AlertEvidence

@dataclass
class ServicePrincipalEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.servicePrincipalEvidence"
    # The appId property
    app_id: Optional[str] = None
    # The appOwnerTenantId property
    app_owner_tenant_id: Optional[str] = None
    # The servicePrincipalName property
    service_principal_name: Optional[str] = None
    # The servicePrincipalObjectId property
    service_principal_object_id: Optional[str] = None
    # The servicePrincipalType property
    service_principal_type: Optional[ServicePrincipalType] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .service_principal_type import ServicePrincipalType

        from .alert_evidence import AlertEvidence
        from .service_principal_type import ServicePrincipalType

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appOwnerTenantId": lambda n : setattr(self, 'app_owner_tenant_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "servicePrincipalObjectId": lambda n : setattr(self, 'service_principal_object_id', n.get_str_value()),
            "servicePrincipalType": lambda n : setattr(self, 'service_principal_type', n.get_enum_value(ServicePrincipalType)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appOwnerTenantId", self.app_owner_tenant_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_str_value("servicePrincipalObjectId", self.service_principal_object_id)
        writer.write_enum_value("servicePrincipalType", self.service_principal_type)
        writer.write_str_value("tenantId", self.tenant_id)
    

