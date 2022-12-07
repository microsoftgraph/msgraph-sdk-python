from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cross_tenant_access_policy_b2_b_setting = lazy_import('msgraph.generated.models.cross_tenant_access_policy_b2_b_setting')
cross_tenant_access_policy_inbound_trust = lazy_import('msgraph.generated.models.cross_tenant_access_policy_inbound_trust')

class CrossTenantAccessPolicyConfigurationPartner(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def b2b_collaboration_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationInbound property value. Defines your partner-specific configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_inbound
    
    @b2b_collaboration_inbound.setter
    def b2b_collaboration_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationInbound property value. Defines your partner-specific configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2bCollaborationInbound property.
        """
        self._b2b_collaboration_inbound = value
    
    @property
    def b2b_collaboration_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bCollaborationOutbound property value. Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_collaboration_outbound
    
    @b2b_collaboration_outbound.setter
    def b2b_collaboration_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bCollaborationOutbound property value. Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        Args:
            value: Value to set for the b2bCollaborationOutbound property.
        """
        self._b2b_collaboration_outbound = value
    
    @property
    def b2b_direct_connect_inbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectInbound property value. Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_inbound
    
    @b2b_direct_connect_inbound.setter
    def b2b_direct_connect_inbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectInbound property value. Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
        Args:
            value: Value to set for the b2bDirectConnectInbound property.
        """
        self._b2b_direct_connect_inbound = value
    
    @property
    def b2b_direct_connect_outbound(self,) -> Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]:
        """
        Gets the b2bDirectConnectOutbound property value. Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Returns: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting]
        """
        return self._b2b_direct_connect_outbound
    
    @b2b_direct_connect_outbound.setter
    def b2b_direct_connect_outbound(self,value: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None) -> None:
        """
        Sets the b2bDirectConnectOutbound property value. Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        Args:
            value: Value to set for the b2bDirectConnectOutbound property.
        """
        self._b2b_direct_connect_outbound = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyConfigurationPartner and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines your partner-specific configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        self._b2b_collaboration_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        self._b2b_collaboration_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
        self._b2b_direct_connect_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        self._b2b_direct_connect_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Determines the partner-specific configuration for trusting other Conditional Access claims from external Azure AD organizations.
        self._inbound_trust: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None
        # Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
        self._is_service_provider: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tenant identifier for the partner Azure AD organization. Read-only. Key.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyConfigurationPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationPartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantAccessPolicyConfigurationPartner()
    
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
            "is_service_provider": lambda n : setattr(self, 'is_service_provider', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    @property
    def inbound_trust(self,) -> Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]:
        """
        Gets the inboundTrust property value. Determines the partner-specific configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Returns: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust]
        """
        return self._inbound_trust
    
    @inbound_trust.setter
    def inbound_trust(self,value: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None) -> None:
        """
        Sets the inboundTrust property value. Determines the partner-specific configuration for trusting other Conditional Access claims from external Azure AD organizations.
        Args:
            value: Value to set for the inboundTrust property.
        """
        self._inbound_trust = value
    
    @property
    def is_service_provider(self,) -> Optional[bool]:
        """
        Gets the isServiceProvider property value. Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
        Returns: Optional[bool]
        """
        return self._is_service_provider
    
    @is_service_provider.setter
    def is_service_provider(self,value: Optional[bool] = None) -> None:
        """
        Sets the isServiceProvider property value. Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
        Args:
            value: Value to set for the isServiceProvider property.
        """
        self._is_service_provider = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_bool_value("isServiceProvider", self.is_service_provider)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenant identifier for the partner Azure AD organization. Read-only. Key.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenant identifier for the partner Azure AD organization. Read-only. Key.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

