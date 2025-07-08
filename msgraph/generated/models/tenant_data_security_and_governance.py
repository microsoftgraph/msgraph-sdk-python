from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_security_and_governance import DataSecurityAndGovernance
    from .tenant_protection_scope_container import TenantProtectionScopeContainer

from .data_security_and_governance import DataSecurityAndGovernance

@dataclass
class TenantDataSecurityAndGovernance(DataSecurityAndGovernance, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.tenantDataSecurityAndGovernance"
    # The protectionScopes property
    protection_scopes: Optional[TenantProtectionScopeContainer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantDataSecurityAndGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantDataSecurityAndGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantDataSecurityAndGovernance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_security_and_governance import DataSecurityAndGovernance
        from .tenant_protection_scope_container import TenantProtectionScopeContainer

        from .data_security_and_governance import DataSecurityAndGovernance
        from .tenant_protection_scope_container import TenantProtectionScopeContainer

        fields: dict[str, Callable[[Any], None]] = {
            "protectionScopes": lambda n : setattr(self, 'protection_scopes', n.get_object_value(TenantProtectionScopeContainer)),
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
        writer.write_object_value("protectionScopes", self.protection_scopes)
    

