from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
    from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
    from .entity import Entity
    from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

from .entity import Entity

@dataclass
class CrossTenantAccessPolicyConfigurationDefault(Entity):
    # Determines the default configuration for automatic user consent settings. The inboundAllowed and outboundAllowed properties are always false and cannot be updated in the default configuration. Read-only.
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
    # If true, the default configuration is set to the system default configuration. If false, the default settings have been customized.
    is_service_default: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyConfigurationDefault:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyConfigurationDefault
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyConfigurationDefault()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .entity import Entity
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
        from .entity import Entity
        from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticUserConsentSettings": lambda n : setattr(self, 'automatic_user_consent_settings', n.get_object_value(InboundOutboundPolicyConfiguration)),
            "b2bCollaborationInbound": lambda n : setattr(self, 'b2b_collaboration_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bCollaborationOutbound": lambda n : setattr(self, 'b2b_collaboration_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectInbound": lambda n : setattr(self, 'b2b_direct_connect_inbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "b2bDirectConnectOutbound": lambda n : setattr(self, 'b2b_direct_connect_outbound', n.get_object_value(CrossTenantAccessPolicyB2BSetting)),
            "inboundTrust": lambda n : setattr(self, 'inbound_trust', n.get_object_value(CrossTenantAccessPolicyInboundTrust)),
            "isServiceDefault": lambda n : setattr(self, 'is_service_default', n.get_bool_value()),
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
        writer.write_object_value("automaticUserConsentSettings", self.automatic_user_consent_settings)
        writer.write_object_value("b2bCollaborationInbound", self.b2b_collaboration_inbound)
        writer.write_object_value("b2bCollaborationOutbound", self.b2b_collaboration_outbound)
        writer.write_object_value("b2bDirectConnectInbound", self.b2b_direct_connect_inbound)
        writer.write_object_value("b2bDirectConnectOutbound", self.b2b_direct_connect_outbound)
        writer.write_object_value("inboundTrust", self.inbound_trust)
        writer.write_bool_value("isServiceDefault", self.is_service_default)
    

