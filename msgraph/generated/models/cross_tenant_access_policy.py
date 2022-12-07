from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_configuration_default = lazy_import('msgraph.generated.models.cross_tenant_access_policy_configuration_default')
cross_tenant_access_policy_configuration_partner = lazy_import('msgraph.generated.models.cross_tenant_access_policy_configuration_partner')
policy_base = lazy_import('msgraph.generated.models.policy_base')

class CrossTenantAccessPolicy(policy_base.PolicyBase):
    @property
    def allowed_cloud_endpoints(self,) -> Optional[List[str]]:
        """
        Gets the allowedCloudEndpoints property value. The allowedCloudEndpoints property
        Returns: Optional[List[str]]
        """
        return self._allowed_cloud_endpoints
    
    @allowed_cloud_endpoints.setter
    def allowed_cloud_endpoints(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the allowedCloudEndpoints property value. The allowedCloudEndpoints property
        Args:
            value: Value to set for the allowedCloudEndpoints property.
        """
        self._allowed_cloud_endpoints = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CrossTenantAccessPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.crossTenantAccessPolicy"
        # The allowedCloudEndpoints property
        self._allowed_cloud_endpoints: Optional[List[str]] = None
        # Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
        self._default: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault] = None
        # Defines partner-specific configurations for external Azure Active Directory organizations.
        self._partners: Optional[List[cross_tenant_access_policy_configuration_partner.CrossTenantAccessPolicyConfigurationPartner]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicy()
    
    @property
    def default(self,) -> Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]:
        """
        Gets the default property value. Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
        Returns: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]
        """
        return self._default
    
    @default.setter
    def default(self,value: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault] = None) -> None:
        """
        Sets the default property value. Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
        Args:
            value: Value to set for the default property.
        """
        self._default = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_cloud_endpoints": lambda n : setattr(self, 'allowed_cloud_endpoints', n.get_collection_of_primitive_values(str)),
            "default": lambda n : setattr(self, 'default', n.get_object_value(cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault)),
            "partners": lambda n : setattr(self, 'partners', n.get_collection_of_object_values(cross_tenant_access_policy_configuration_partner.CrossTenantAccessPolicyConfigurationPartner)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def partners(self,) -> Optional[List[cross_tenant_access_policy_configuration_partner.CrossTenantAccessPolicyConfigurationPartner]]:
        """
        Gets the partners property value. Defines partner-specific configurations for external Azure Active Directory organizations.
        Returns: Optional[List[cross_tenant_access_policy_configuration_partner.CrossTenantAccessPolicyConfigurationPartner]]
        """
        return self._partners
    
    @partners.setter
    def partners(self,value: Optional[List[cross_tenant_access_policy_configuration_partner.CrossTenantAccessPolicyConfigurationPartner]] = None) -> None:
        """
        Sets the partners property value. Defines partner-specific configurations for external Azure Active Directory organizations.
        Args:
            value: Value to set for the partners property.
        """
        self._partners = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("allowedCloudEndpoints", self.allowed_cloud_endpoints)
        writer.write_object_value("default", self.default)
        writer.write_collection_of_object_values("partners", self.partners)
    

