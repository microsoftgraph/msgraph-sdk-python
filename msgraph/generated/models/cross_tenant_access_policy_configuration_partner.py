from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_b2_b_setting, cross_tenant_access_policy_inbound_trust, cross_tenant_identity_sync_policy_partner, inbound_outbound_policy_configuration

class CrossTenantAccessPolicyConfigurationPartner(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantAccessPolicyConfigurationPartner and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The automaticUserConsentSettings property
        self._automatic_user_consent_settings: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration] = None
        # Defines your partner-specific configuration for users from other organizations accessing your resources via Azure AD B2B collaboration.
        self._b2b_collaboration_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B collaboration.
        self._b2b_collaboration_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
        self._b2b_direct_connect_inbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Azure AD B2B direct connect.
        self._b2b_direct_connect_outbound: Optional[cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting] = None
        # The identitySynchronization property
        self._identity_synchronization: Optional[cross_tenant_identity_sync_policy_partner.CrossTenantIdentitySyncPolicyPartner] = None
        # Determines the partner-specific configuration for trusting other Conditional Access claims from external Azure AD organizations.
        self._inbound_trust: Optional[cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust] = None
        # Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
        self._is_service_provider: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tenant identifier for the partner Azure AD organization. Read-only. Key.
        self._tenant_id: Optional[str] = None
    
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
    def automatic_user_consent_settings(self,) -> Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration]:
        """
        Gets the automaticUserConsentSettings property value. The automaticUserConsentSettings property
        Returns: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration]
        """
        return self._automatic_user_consent_settings
    
    @automatic_user_consent_settings.setter
    def automatic_user_consent_settings(self,value: Optional[inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration] = None) -> None:
        """
        Sets the automaticUserConsentSettings property value. The automaticUserConsentSettings property
        Args:
            value: Value to set for the automatic_user_consent_settings property.
        """
        self._automatic_user_consent_settings = value
    
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
            value: Value to set for the b2b_collaboration_inbound property.
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
            value: Value to set for the b2b_collaboration_outbound property.
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
            value: Value to set for the b2b_direct_connect_inbound property.
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
            value: Value to set for the b2b_direct_connect_outbound property.
        """
        self._b2b_direct_connect_outbound = value
    
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
        from . import cross_tenant_access_policy_b2_b_setting, cross_tenant_access_policy_inbound_trust, cross_tenant_identity_sync_policy_partner, inbound_outbound_policy_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticUserConsentSettings": lambda n : setattr(self, 'automatic_user_consent_settings', n.get_object_value(inbound_outbound_policy_configuration.InboundOutboundPolicyConfiguration)),
            "b2bCollaborationInbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bCollaborationOutbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectInbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectOutbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(cross_tenant_access_policy_b2_b_setting.CrossTenantAccessPolicyB2BSetting)),
            "identitySynchronization": lambda n : setattr(self, 'identity_synchronization', n.get_object_value(cross_tenant_identity_sync_policy_partner.CrossTenantIdentitySyncPolicyPartner)),
            "inboundTrust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(cross_tenant_access_policy_inbound_trust.CrossTenantAccessPolicyInboundTrust)),
            "isServiceProvider": lambda n : setattr(self, 'is_service_provider', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        return fields
    
    @property
    def identity_synchronization(self,) -> Optional[cross_tenant_identity_sync_policy_partner.CrossTenantIdentitySyncPolicyPartner]:
        """
        Gets the identitySynchronization property value. The identitySynchronization property
        Returns: Optional[cross_tenant_identity_sync_policy_partner.CrossTenantIdentitySyncPolicyPartner]
        """
        return self._identity_synchronization
    
    @identity_synchronization.setter
    def identity_synchronization(self,value: Optional[cross_tenant_identity_sync_policy_partner.CrossTenantIdentitySyncPolicyPartner] = None) -> None:
        """
        Sets the identitySynchronization property value. The identitySynchronization property
        Args:
            value: Value to set for the identity_synchronization property.
        """
        self._identity_synchronization = value
    
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
            value: Value to set for the inbound_trust property.
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
            value: Value to set for the is_service_provider property.
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("automaticUserConsentSettings", self.automatic_user_consent_settings)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("identitySynchronization", self.identity_synchronization)
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
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

