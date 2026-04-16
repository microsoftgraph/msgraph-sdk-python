from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_app_service_connect_setting import CrossTenantAccessPolicyAppServiceConnectSetting
    from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
    from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
    from .cross_tenant_access_policy_m365_collaboration_inbound_setting import CrossTenantAccessPolicyM365CollaborationInboundSetting
    from .cross_tenant_access_policy_m365_collaboration_outbound_setting import CrossTenantAccessPolicyM365CollaborationOutboundSetting
    from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
    from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
    from .entity import Entity
    from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

from .entity import Entity

@dataclass
class CrossTenantAccessPolicyConfigurationDefault(Entity, Parsable):
    # Defines your default configuration for inbound app service connect settings that control which applications can connect across tenant boundaries.
    app_service_connect_inbound: Optional[CrossTenantAccessPolicyAppServiceConnectSetting] = None
    # Determines the default configuration for automatic user consent settings. The inboundAllowed and outboundAllowed properties are always false and can't be updated in the default configuration. Read-only.
    automatic_user_consent_settings: Optional[InboundOutboundPolicyConfiguration] = None
    # Defines your default configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration.
    b2b_collaboration_inbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your default configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration.
    b2b_collaboration_outbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your default configuration for users from other organizations accessing your resources via Microsoft Entra B2B direct connect.
    b2b_direct_connect_inbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Defines your default configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect.
    b2b_direct_connect_outbound: Optional[CrossTenantAccessPolicyB2BSetting] = None
    # Determines the default configuration for trusting other Conditional Access claims from external Microsoft Entra organizations.
    inbound_trust: Optional[CrossTenantAccessPolicyInboundTrust] = None
    # Defines the priority order based on which an identity provider is selected during invitation redemption for a guest user.
    invitation_redemption_identity_provider_configuration: Optional[DefaultInvitationRedemptionIdentityProviderConfiguration] = None
    # If true, the default configuration is set to the system default configuration. If false, the default settings are customized.
    is_service_default: Optional[bool] = None
    # Defines your default configuration for inbound Microsoft 365 collaboration settings that determine which users from other organizations can collaborate with your organization using Microsoft 365 apps.
    m365_collaboration_inbound: Optional[CrossTenantAccessPolicyM365CollaborationInboundSetting] = None
    # Defines your default configuration for outbound Microsoft 365 collaboration settings that determine which users in your organization can collaborate with other organizations using Microsoft 365 apps.
    m365_collaboration_outbound: Optional[CrossTenantAccessPolicyM365CollaborationOutboundSetting] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the default tenant restrictions configuration for users in your organization who access an external organization on your network or devices.
    tenant_restrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccessPolicyConfigurationDefault:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationDefault
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyConfigurationDefault()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_app_service_connect_setting import CrossTenantAccessPolicyAppServiceConnectSetting
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .cross_tenant_access_policy_m365_collaboration_inbound_setting import CrossTenantAccessPolicyM365CollaborationInboundSetting
        from .cross_tenant_access_policy_m365_collaboration_outbound_setting import CrossTenantAccessPolicyM365CollaborationOutboundSetting
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
        from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
        from .entity import Entity
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        from .cross_tenant_access_policy_app_service_connect_setting import CrossTenantAccessPolicyAppServiceConnectSetting
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .cross_tenant_access_policy_m365_collaboration_inbound_setting import CrossTenantAccessPolicyM365CollaborationInboundSetting
        from .cross_tenant_access_policy_m365_collaboration_outbound_setting import CrossTenantAccessPolicyM365CollaborationOutboundSetting
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
        from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
        from .entity import Entity
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "appServiceConnectInbound": lambda n : setattr(self, 'app_service_connect_inbound', n.get_object_value(CrossTenantAccessPolicyAppServiceConnectSetting)),
            "automaticUserConsentSettings": lambda n : setattr(self, 'automatic_user_consent_settings', n.get_object_value(InboundOutboundPolicyConfiguration)),
            "b2bCollaborationInbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bCollaborationOutbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectInbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectOutbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "inboundTrust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(CrossTenantAccessPolicyInboundTrust)),
            "invitationRedemptionIdentityProviderConfiguration": lambda n : setattr(self, 'invitation_redemption_identity_provider_configuration', n.get_object_value(DefaultInvitationRedemptionIdentityProviderConfiguration)),
            "isServiceDefault": lambda n : setattr(self, 'is_service_default', n.get_bool_value()),
            "m365CollaborationInbound": lambda n : setattr(self, 'm365_collaboration_inbound', n.get_object_value(CrossTenantAccessPolicyM365CollaborationInboundSetting)),
            "m365CollaborationOutbound": lambda n : setattr(self, 'm365_collaboration_outbound', n.get_object_value(CrossTenantAccessPolicyM365CollaborationOutboundSetting)),
            "tenantRestrictions": lambda n : setattr(self, 'tenant_restrictions', n.get_object_value(CrossTenantAccessPolicyTenantRestrictions)),
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
        writer.write_object_value("appServiceConnectInbound", self.app_service_connect_inbound)
        writer.write_object_value("automaticUserConsentSettings", self.automatic_user_consent_settings)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_object_value("invitationRedemptionIdentityProviderConfiguration", self.invitation_redemption_identity_provider_configuration)
        writer.write_bool_value("isServiceDefault", self.is_service_default)
        writer.write_object_value("m365CollaborationInbound", self.m365_collaboration_inbound)
        writer.write_object_value("m365CollaborationOutbound", self.m365_collaboration_outbound)
        writer.write_object_value("tenantRestrictions", self.tenant_restrictions)
    

