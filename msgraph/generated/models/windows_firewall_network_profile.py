from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .state_management_setting import StateManagementSetting

@dataclass
class WindowsFirewallNetworkProfile(AdditionalDataHolder, BackedModel, Parsable):
    """
    Windows Firewall Profile Policies.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Configures the firewall to merge authorized application rules from group policy with those from local store instead of ignoring the local store rules. When AuthorizedApplicationRulesFromGroupPolicyNotMerged and AuthorizedApplicationRulesFromGroupPolicyMerged are both true, AuthorizedApplicationRulesFromGroupPolicyMerged takes priority.
    authorized_application_rules_from_group_policy_merged: Optional[bool] = None
    # Configures the firewall to merge connection security rules from group policy with those from local store instead of ignoring the local store rules. When ConnectionSecurityRulesFromGroupPolicyNotMerged and ConnectionSecurityRulesFromGroupPolicyMerged are both true, ConnectionSecurityRulesFromGroupPolicyMerged takes priority.
    connection_security_rules_from_group_policy_merged: Optional[bool] = None
    # State Management Setting.
    firewall_enabled: Optional[StateManagementSetting] = None
    # Configures the firewall to merge global port rules from group policy with those from local store instead of ignoring the local store rules. When GlobalPortRulesFromGroupPolicyNotMerged and GlobalPortRulesFromGroupPolicyMerged are both true, GlobalPortRulesFromGroupPolicyMerged takes priority.
    global_port_rules_from_group_policy_merged: Optional[bool] = None
    # Configures the firewall to block all incoming connections by default. When InboundConnectionsRequired and InboundConnectionsBlocked are both true, InboundConnectionsBlocked takes priority.
    inbound_connections_blocked: Optional[bool] = None
    # Prevents the firewall from displaying notifications when an application is blocked from listening on a port. When InboundNotificationsRequired and InboundNotificationsBlocked are both true, InboundNotificationsBlocked takes priority.
    inbound_notifications_blocked: Optional[bool] = None
    # Configures the firewall to block all incoming traffic regardless of other policy settings. When IncomingTrafficRequired and IncomingTrafficBlocked are both true, IncomingTrafficBlocked takes priority.
    incoming_traffic_blocked: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Configures the firewall to block all outgoing connections by default. When OutboundConnectionsRequired and OutboundConnectionsBlocked are both true, OutboundConnectionsBlocked takes priority. This setting will get applied to Windows releases version 1809 and above.
    outbound_connections_blocked: Optional[bool] = None
    # Configures the firewall to merge Firewall Rule policies from group policy with those from local store instead of ignoring the local store rules. When PolicyRulesFromGroupPolicyNotMerged and PolicyRulesFromGroupPolicyMerged are both true, PolicyRulesFromGroupPolicyMerged takes priority.
    policy_rules_from_group_policy_merged: Optional[bool] = None
    # Configures the firewall to allow the host computer to respond to unsolicited network traffic of that traffic is secured by IPSec even when stealthModeBlocked is set to true. When SecuredPacketExemptionBlocked and SecuredPacketExemptionAllowed are both true, SecuredPacketExemptionAllowed takes priority.
    secured_packet_exemption_allowed: Optional[bool] = None
    # Prevent the server from operating in stealth mode. When StealthModeRequired and StealthModeBlocked are both true, StealthModeBlocked takes priority.
    stealth_mode_blocked: Optional[bool] = None
    # Configures the firewall to block unicast responses to multicast broadcast traffic. When UnicastResponsesToMulticastBroadcastsRequired and UnicastResponsesToMulticastBroadcastsBlocked are both true, UnicastResponsesToMulticastBroadcastsBlocked takes priority.
    unicast_responses_to_multicast_broadcasts_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsFirewallNetworkProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFirewallNetworkProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsFirewallNetworkProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .state_management_setting import StateManagementSetting

        from .state_management_setting import StateManagementSetting

        fields: dict[str, Callable[[Any], None]] = {
            "authorizedApplicationRulesFromGroupPolicyMerged": lambda n : setattr(self, 'authorized_application_rules_from_group_policy_merged', n.get_bool_value()),
            "connectionSecurityRulesFromGroupPolicyMerged": lambda n : setattr(self, 'connection_security_rules_from_group_policy_merged', n.get_bool_value()),
            "firewallEnabled": lambda n : setattr(self, 'firewall_enabled', n.get_enum_value(StateManagementSetting)),
            "globalPortRulesFromGroupPolicyMerged": lambda n : setattr(self, 'global_port_rules_from_group_policy_merged', n.get_bool_value()),
            "inboundConnectionsBlocked": lambda n : setattr(self, 'inbound_connections_blocked', n.get_bool_value()),
            "inboundNotificationsBlocked": lambda n : setattr(self, 'inbound_notifications_blocked', n.get_bool_value()),
            "incomingTrafficBlocked": lambda n : setattr(self, 'incoming_traffic_blocked', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outboundConnectionsBlocked": lambda n : setattr(self, 'outbound_connections_blocked', n.get_bool_value()),
            "policyRulesFromGroupPolicyMerged": lambda n : setattr(self, 'policy_rules_from_group_policy_merged', n.get_bool_value()),
            "securedPacketExemptionAllowed": lambda n : setattr(self, 'secured_packet_exemption_allowed', n.get_bool_value()),
            "stealthModeBlocked": lambda n : setattr(self, 'stealth_mode_blocked', n.get_bool_value()),
            "unicastResponsesToMulticastBroadcastsBlocked": lambda n : setattr(self, 'unicast_responses_to_multicast_broadcasts_blocked', n.get_bool_value()),
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
        writer.write_bool_value("authorizedApplicationRulesFromGroupPolicyMerged", self.authorized_application_rules_from_group_policy_merged)
        writer.write_bool_value("connectionSecurityRulesFromGroupPolicyMerged", self.connection_security_rules_from_group_policy_merged)
        writer.write_enum_value("firewallEnabled", self.firewall_enabled)
        writer.write_bool_value("globalPortRulesFromGroupPolicyMerged", self.global_port_rules_from_group_policy_merged)
        writer.write_bool_value("inboundConnectionsBlocked", self.inbound_connections_blocked)
        writer.write_bool_value("inboundNotificationsBlocked", self.inbound_notifications_blocked)
        writer.write_bool_value("incomingTrafficBlocked", self.incoming_traffic_blocked)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("outboundConnectionsBlocked", self.outbound_connections_blocked)
        writer.write_bool_value("policyRulesFromGroupPolicyMerged", self.policy_rules_from_group_policy_merged)
        writer.write_bool_value("securedPacketExemptionAllowed", self.secured_packet_exemption_allowed)
        writer.write_bool_value("stealthModeBlocked", self.stealth_mode_blocked)
        writer.write_bool_value("unicastResponsesToMulticastBroadcastsBlocked", self.unicast_responses_to_multicast_broadcasts_blocked)
        writer.write_additional_data_value(self.additional_data)
    

