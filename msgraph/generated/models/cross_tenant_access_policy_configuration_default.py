from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_b2_b_setting = lazy_import('msgraph.generated.models.cross_tenant_access_policy_b2_b_setting')
cross_tenant_access_policy_inbound_trust = lazy_import('msgraph.generated.models.cross_tenant_access_policy_inbound_trust')
entity = lazy_import('msgraph.generated.models.entity')

class CrossTenantAccessPolicyConfigurationDefault(entity.Entity):
    @property
    def b2b_collaboration_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_inbound
    
    @b2b_collaboration_inbound.setter
    def b2b_collaboration_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2bCollaborationInbound property.
        """
        self._b2b_collaboration_inbound = value
    
    @property
    def b2b_collaboration_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_outbound
    
    @b2b_collaboration_outbound.setter
    def b2b_collaboration_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2bCollaborationOutbound property.
        """
        self._b2b_collaboration_outbound = value
    
    @property
    def b2b_direct_connect_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_inbound
    
    @b2b_direct_connect_inbound.setter
    def b2b_direct_connect_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectInbound property value. Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        Args:
            value: Value to set for the b2bDirectConnectInbound property.
        """
        self._b2b_direct_connect_inbound = value
    
    @property
    def b2b_direct_connect_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_outbound
    
    @b2b_direct_connect_outbound.setter
    def b2b_direct_connect_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectOutbound property value. Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Args:
            value: Value to set for the b2bDirectConnectOutbound property.
        """
        self._b2b_direct_connect_outbound = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyConfigurationDefault and sets the default values.
        """
        super().__init__()
        # Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        self._b2b_collaboration_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        self._b2b_collaboration_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users from other organizations accessing your resources via Azure AD B2B direct connect.
        self._b2b_direct_connect_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your default configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        self._b2b_direct_connect_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        self._inbound_trust: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None
        # If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        self._is_service_default: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyConfigurationDefault:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationDefault
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyConfigurationDefault()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "b2b_collaboration_inbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2b_collaboration_outbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2b_direct_connect_inbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2b_direct_connect_outbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "inbound_trust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust)),
            "is_service_default": lambda n : setattr(self, 'is_service_default', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inbound_trust(self,) -> Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]:
        """
        Gets the inboundTrust property value. Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Returns: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]
        """
        return self._inbound_trust
    
    @inbound_trust.setter
    def inbound_trust(self,value: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None) -> None:
        """
        Sets the inboundTrust property value. Determines the default configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Args:
            value: Value to set for the inboundTrust property.
        """
        self._inbound_trust = value
    
    @property
    def is_service_default(self,) -> Optional[bool]:
        """
        Gets the isServiceDefault property value. If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        Returns: Optional[bool]
        """
        return self._is_service_default
    
    @is_service_default.setter
    def is_service_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isServiceDefault property value. If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
        Args:
            value: Value to set for the isServiceDefault property.
        """
        self._is_service_default = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_bool_value("isServiceDefault", self.is_service_default)
    

