from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
    from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
    from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
    from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
    from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

@dataclass
class CrossTenantAccessPolicyConfigurationPartner(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Determines the partner-specific configuration for automatic user consent settings. Unless specifically configured, the inboundAllowed and outboundAllowed properties are null and inherit from the default settings, which is always false.
    automatic_user_consent_settings: Optional[InboundOutboundPolicyConfiguration] = None
    # Defines your partner-specific configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration.
    b2b_collaboration_inbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration.
    b2b_collaboration_outbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
    b2b_direct_connect_inbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect.
    b2b_direct_connect_outbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another.
    identity_synchronization: Optional[CrossTenantIdentitySyncPolicyPartner] = None
    # Determines the partner-specific configuration for trusting other Conditional Access claims from external Microsoft Entra organizations.
    inbound_trust: Optional[CrossTenantAccessPolicyInboundTrust] = None
    # Identifies whether a tenant is a member of a multitenant organization.
    is_in_multi_tenant_organization: Optional[bool] = None
    # Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
    is_service_provider: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tenant identifier for the partner Microsoft Entra organization. Read-only. Key.
    tenant_id: Optional[str] = None
    # Defines the partner-specific tenant restrictions configuration for users in your organization who access a partner organization using partner supplied identities on your network or devices.
    tenant_restrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccessPolicyConfigurationPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyConfigurationPartner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "automaticUserConsentSettings": lambda n : setattr(self, 'automatic_user_consent_settings', n.get_object_value(InboundOutboundPolicyConfiguration)),
            "b2bCollaborationInbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bCollaborationOutbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectInbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectOutbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "identitySynchronization": lambda n : setattr(self, 'identity_synchronization', n.get_object_value(CrossTenantIdentitySyncPolicyPartner)),
            "inboundTrust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(CrossTenantAccessPolicyInboundTrust)),
            "isInMultiTenantOrganization": lambda n : setattr(self, 'is_in_multi_tenant_organization', n.get_bool_value()),
            "isServiceProvider": lambda n : setattr(self, 'is_service_provider', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tenantRestrictions": lambda n : setattr(self, 'tenant_restrictions', n.get_object_value(CrossTenantAccessPolicyTenantRestrictions)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("automaticUserConsentSettings", self.automatic_user_consent_settings)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("identitySynchronization", self.identity_synchronization)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_bool_value("isInMultiTenantOrganization", self.is_in_multi_tenant_organization)
        writer.write_bool_value("isServiceProvider", self.is_service_provider)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("tenantRestrictions", self.tenant_restrictions)
        writer.write_additional_data_value(self.additional_data)
    

