from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
    from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class CrossTenantAccessPolicy(PolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.crossTenantAccessPolicy"
    # Used to specify which Microsoft clouds an organization would like to collaborate with. By default, this value is empty. Supported values for this field are: microsoftonline.com, microsoftonline.us, and partner.microsoftonline.cn.
    allowed_cloud_endpoints: Optional[List[str]] = None
    # Defines the default configuration for how your organization interacts with external Microsoft Entra organizations.
    default: Optional[CrossTenantAccessPolicyConfigurationDefault] = None
    # Defines partner-specific configurations for external Microsoft Entra organizations.
    partners: Optional[List[CrossTenantAccessPolicyConfigurationPartner]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .policy_base import PolicyBase

        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .policy_base import PolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedCloudEndpoints": lambda n : setattr(self, 'allowed_cloud_endpoints', n.get_collection_of_primitive_values(str)),
            "default": lambda n : setattr(self, 'default', n.get_object_value(CrossTenantAccessPolicyConfigurationDefault)),
            "partners": lambda n : setattr(self, 'partners', n.get_collection_of_object_values(CrossTenantAccessPolicyConfigurationPartner)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("allowedCloudEndpoints", self.allowed_cloud_endpoints)
        writer.write_object_value("default", self.default)
        writer.write_collection_of_object_values("partners", self.partners)
    

