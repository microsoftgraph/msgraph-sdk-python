from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

state_management_setting = lazy_import('msgraph.generated.models.state_management_setting')

class WindowsFirewallNetworkProfile(AdditionalDataHolder, Parsable):
    """
    Windows Firewall Profile Policies.
    """
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
    def authorized_application_rules_from_group_policy_merged(self,) -> Optional[bool]:
        """
        Gets the authorizedApplicationRulesFromGroupPolicyMerged property value. Configures the firewall to merge authorized application rules from group policy with those from local store instead of ignoring the local store rules. When AuthorizedApplicationRulesFromGroupPolicyNotMerged and AuthorizedApplicationRulesFromGroupPolicyMerged are both true, AuthorizedApplicationRulesFromGroupPolicyMerged takes priority.
        Returns: Optional[bool]
        """
        return self._authorized_application_rules_from_group_policy_merged
    
    @authorized_application_rules_from_group_policy_merged.setter
    def authorized_application_rules_from_group_policy_merged(self,value: Optional[bool] = None) -> None:
        """
        Sets the authorizedApplicationRulesFromGroupPolicyMerged property value. Configures the firewall to merge authorized application rules from group policy with those from local store instead of ignoring the local store rules. When AuthorizedApplicationRulesFromGroupPolicyNotMerged and AuthorizedApplicationRulesFromGroupPolicyMerged are both true, AuthorizedApplicationRulesFromGroupPolicyMerged takes priority.
        Args:
            value: Value to set for the authorizedApplicationRulesFromGroupPolicyMerged property.
        """
        self._authorized_application_rules_from_group_policy_merged = value
    
    @property
    def connection_security_rules_from_group_policy_merged(self,) -> Optional[bool]:
        """
        Gets the connectionSecurityRulesFromGroupPolicyMerged property value. Configures the firewall to merge connection security rules from group policy with those from local store instead of ignoring the local store rules. When ConnectionSecurityRulesFromGroupPolicyNotMerged and ConnectionSecurityRulesFromGroupPolicyMerged are both true, ConnectionSecurityRulesFromGroupPolicyMerged takes priority.
        Returns: Optional[bool]
        """
        return self._connection_security_rules_from_group_policy_merged
    
    @connection_security_rules_from_group_policy_merged.setter
    def connection_security_rules_from_group_policy_merged(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectionSecurityRulesFromGroupPolicyMerged property value. Configures the firewall to merge connection security rules from group policy with those from local store instead of ignoring the local store rules. When ConnectionSecurityRulesFromGroupPolicyNotMerged and ConnectionSecurityRulesFromGroupPolicyMerged are both true, ConnectionSecurityRulesFromGroupPolicyMerged takes priority.
        Args:
            value: Value to set for the connectionSecurityRulesFromGroupPolicyMerged property.
        """
        self._connection_security_rules_from_group_policy_merged = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsFirewallNetworkProfile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Configures the firewall to merge authorized application rules from group policy with those from local store instead of ignoring the local store rules. When AuthorizedApplicationRulesFromGroupPolicyNotMerged and AuthorizedApplicationRulesFromGroupPolicyMerged are both true, AuthorizedApplicationRulesFromGroupPolicyMerged takes priority.
        self._authorized_application_rules_from_group_policy_merged: Optional[bool] = None
        # Configures the firewall to merge connection security rules from group policy with those from local store instead of ignoring the local store rules. When ConnectionSecurityRulesFromGroupPolicyNotMerged and ConnectionSecurityRulesFromGroupPolicyMerged are both true, ConnectionSecurityRulesFromGroupPolicyMerged takes priority.
        self._connection_security_rules_from_group_policy_merged: Optional[bool] = None
        # State Management Setting.
        self._firewall_enabled: Optional[state_management_setting.StateManagementSetting] = None
        # Configures the firewall to merge global port rules from group policy with those from local store instead of ignoring the local store rules. When GlobalPortRulesFromGroupPolicyNotMerged and GlobalPortRulesFromGroupPolicyMerged are both true, GlobalPortRulesFromGroupPolicyMerged takes priority.
        self._global_port_rules_from_group_policy_merged: Optional[bool] = None
        # Configures the firewall to block all incoming connections by default. When InboundConnectionsRequired and InboundConnectionsBlocked are both true, InboundConnectionsBlocked takes priority.
        self._inbound_connections_blocked: Optional[bool] = None
        # Prevents the firewall from displaying notifications when an application is blocked from listening on a port. When InboundNotificationsRequired and InboundNotificationsBlocked are both true, InboundNotificationsBlocked takes priority.
        self._inbound_notifications_blocked: Optional[bool] = None
        # Configures the firewall to block all incoming traffic regardless of other policy settings. When IncomingTrafficRequired and IncomingTrafficBlocked are both true, IncomingTrafficBlocked takes priority.
        self._incoming_traffic_blocked: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Configures the firewall to block all outgoing connections by default. When OutboundConnectionsRequired and OutboundConnectionsBlocked are both true, OutboundConnectionsBlocked takes priority. This setting will get applied to Windows releases version 1809 and above.
        self._outbound_connections_blocked: Optional[bool] = None
        # Configures the firewall to merge Firewall Rule policies from group policy with those from local store instead of ignoring the local store rules. When PolicyRulesFromGroupPolicyNotMerged and PolicyRulesFromGroupPolicyMerged are both true, PolicyRulesFromGroupPolicyMerged takes priority.
        self._policy_rules_from_group_policy_merged: Optional[bool] = None
        # Configures the firewall to allow the host computer to respond to unsolicited network traffic of that traffic is secured by IPSec even when stealthModeBlocked is set to true. When SecuredPacketExemptionBlocked and SecuredPacketExemptionAllowed are both true, SecuredPacketExemptionAllowed takes priority.
        self._secured_packet_exemption_allowed: Optional[bool] = None
        # Prevent the server from operating in stealth mode. When StealthModeRequired and StealthModeBlocked are both true, StealthModeBlocked takes priority.
        self._stealth_mode_blocked: Optional[bool] = None
        # Configures the firewall to block unicast responses to multicast broadcast traffic. When UnicastResponsesToMulticastBroadcastsRequired and UnicastResponsesToMulticastBroadcastsBlocked are both true, UnicastResponsesToMulticastBroadcastsBlocked takes priority.
        self._unicast_responses_to_multicast_broadcasts_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsFirewallNetworkProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFirewallNetworkProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsFirewallNetworkProfile()
    
    @property
    def firewall_enabled(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the firewallEnabled property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._firewall_enabled
    
    @firewall_enabled.setter
    def firewall_enabled(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the firewallEnabled property value. State Management Setting.
        Args:
            value: Value to set for the firewallEnabled property.
        """
        self._firewall_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authorized_application_rules_from_group_policy_merged": lambda n : setattr(self, 'authorized_application_rules_from_group_policy_merged', n.get_bool_value()),
            "connection_security_rules_from_group_policy_merged": lambda n : setattr(self, 'connection_security_rules_from_group_policy_merged', n.get_bool_value()),
            "firewall_enabled": lambda n : setattr(self, 'firewall_enabled', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "global_port_rules_from_group_policy_merged": lambda n : setattr(self, 'global_port_rules_from_group_policy_merged', n.get_bool_value()),
            "inbound_connections_blocked": lambda n : setattr(self, 'inbound_connections_blocked', n.get_bool_value()),
            "inbound_notifications_blocked": lambda n : setattr(self, 'inbound_notifications_blocked', n.get_bool_value()),
            "incoming_traffic_blocked": lambda n : setattr(self, 'incoming_traffic_blocked', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outbound_connections_blocked": lambda n : setattr(self, 'outbound_connections_blocked', n.get_bool_value()),
            "policy_rules_from_group_policy_merged": lambda n : setattr(self, 'policy_rules_from_group_policy_merged', n.get_bool_value()),
            "secured_packet_exemption_allowed": lambda n : setattr(self, 'secured_packet_exemption_allowed', n.get_bool_value()),
            "stealth_mode_blocked": lambda n : setattr(self, 'stealth_mode_blocked', n.get_bool_value()),
            "unicast_responses_to_multicast_broadcasts_blocked": lambda n : setattr(self, 'unicast_responses_to_multicast_broadcasts_blocked', n.get_bool_value()),
        }
        return fields
    
    @property
    def global_port_rules_from_group_policy_merged(self,) -> Optional[bool]:
        """
        Gets the globalPortRulesFromGroupPolicyMerged property value. Configures the firewall to merge global port rules from group policy with those from local store instead of ignoring the local store rules. When GlobalPortRulesFromGroupPolicyNotMerged and GlobalPortRulesFromGroupPolicyMerged are both true, GlobalPortRulesFromGroupPolicyMerged takes priority.
        Returns: Optional[bool]
        """
        return self._global_port_rules_from_group_policy_merged
    
    @global_port_rules_from_group_policy_merged.setter
    def global_port_rules_from_group_policy_merged(self,value: Optional[bool] = None) -> None:
        """
        Sets the globalPortRulesFromGroupPolicyMerged property value. Configures the firewall to merge global port rules from group policy with those from local store instead of ignoring the local store rules. When GlobalPortRulesFromGroupPolicyNotMerged and GlobalPortRulesFromGroupPolicyMerged are both true, GlobalPortRulesFromGroupPolicyMerged takes priority.
        Args:
            value: Value to set for the globalPortRulesFromGroupPolicyMerged property.
        """
        self._global_port_rules_from_group_policy_merged = value
    
    @property
    def inbound_connections_blocked(self,) -> Optional[bool]:
        """
        Gets the inboundConnectionsBlocked property value. Configures the firewall to block all incoming connections by default. When InboundConnectionsRequired and InboundConnectionsBlocked are both true, InboundConnectionsBlocked takes priority.
        Returns: Optional[bool]
        """
        return self._inbound_connections_blocked
    
    @inbound_connections_blocked.setter
    def inbound_connections_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the inboundConnectionsBlocked property value. Configures the firewall to block all incoming connections by default. When InboundConnectionsRequired and InboundConnectionsBlocked are both true, InboundConnectionsBlocked takes priority.
        Args:
            value: Value to set for the inboundConnectionsBlocked property.
        """
        self._inbound_connections_blocked = value
    
    @property
    def inbound_notifications_blocked(self,) -> Optional[bool]:
        """
        Gets the inboundNotificationsBlocked property value. Prevents the firewall from displaying notifications when an application is blocked from listening on a port. When InboundNotificationsRequired and InboundNotificationsBlocked are both true, InboundNotificationsBlocked takes priority.
        Returns: Optional[bool]
        """
        return self._inbound_notifications_blocked
    
    @inbound_notifications_blocked.setter
    def inbound_notifications_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the inboundNotificationsBlocked property value. Prevents the firewall from displaying notifications when an application is blocked from listening on a port. When InboundNotificationsRequired and InboundNotificationsBlocked are both true, InboundNotificationsBlocked takes priority.
        Args:
            value: Value to set for the inboundNotificationsBlocked property.
        """
        self._inbound_notifications_blocked = value
    
    @property
    def incoming_traffic_blocked(self,) -> Optional[bool]:
        """
        Gets the incomingTrafficBlocked property value. Configures the firewall to block all incoming traffic regardless of other policy settings. When IncomingTrafficRequired and IncomingTrafficBlocked are both true, IncomingTrafficBlocked takes priority.
        Returns: Optional[bool]
        """
        return self._incoming_traffic_blocked
    
    @incoming_traffic_blocked.setter
    def incoming_traffic_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the incomingTrafficBlocked property value. Configures the firewall to block all incoming traffic regardless of other policy settings. When IncomingTrafficRequired and IncomingTrafficBlocked are both true, IncomingTrafficBlocked takes priority.
        Args:
            value: Value to set for the incomingTrafficBlocked property.
        """
        self._incoming_traffic_blocked = value
    
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
    
    @property
    def outbound_connections_blocked(self,) -> Optional[bool]:
        """
        Gets the outboundConnectionsBlocked property value. Configures the firewall to block all outgoing connections by default. When OutboundConnectionsRequired and OutboundConnectionsBlocked are both true, OutboundConnectionsBlocked takes priority. This setting will get applied to Windows releases version 1809 and above.
        Returns: Optional[bool]
        """
        return self._outbound_connections_blocked
    
    @outbound_connections_blocked.setter
    def outbound_connections_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the outboundConnectionsBlocked property value. Configures the firewall to block all outgoing connections by default. When OutboundConnectionsRequired and OutboundConnectionsBlocked are both true, OutboundConnectionsBlocked takes priority. This setting will get applied to Windows releases version 1809 and above.
        Args:
            value: Value to set for the outboundConnectionsBlocked property.
        """
        self._outbound_connections_blocked = value
    
    @property
    def policy_rules_from_group_policy_merged(self,) -> Optional[bool]:
        """
        Gets the policyRulesFromGroupPolicyMerged property value. Configures the firewall to merge Firewall Rule policies from group policy with those from local store instead of ignoring the local store rules. When PolicyRulesFromGroupPolicyNotMerged and PolicyRulesFromGroupPolicyMerged are both true, PolicyRulesFromGroupPolicyMerged takes priority.
        Returns: Optional[bool]
        """
        return self._policy_rules_from_group_policy_merged
    
    @policy_rules_from_group_policy_merged.setter
    def policy_rules_from_group_policy_merged(self,value: Optional[bool] = None) -> None:
        """
        Sets the policyRulesFromGroupPolicyMerged property value. Configures the firewall to merge Firewall Rule policies from group policy with those from local store instead of ignoring the local store rules. When PolicyRulesFromGroupPolicyNotMerged and PolicyRulesFromGroupPolicyMerged are both true, PolicyRulesFromGroupPolicyMerged takes priority.
        Args:
            value: Value to set for the policyRulesFromGroupPolicyMerged property.
        """
        self._policy_rules_from_group_policy_merged = value
    
    @property
    def secured_packet_exemption_allowed(self,) -> Optional[bool]:
        """
        Gets the securedPacketExemptionAllowed property value. Configures the firewall to allow the host computer to respond to unsolicited network traffic of that traffic is secured by IPSec even when stealthModeBlocked is set to true. When SecuredPacketExemptionBlocked and SecuredPacketExemptionAllowed are both true, SecuredPacketExemptionAllowed takes priority.
        Returns: Optional[bool]
        """
        return self._secured_packet_exemption_allowed
    
    @secured_packet_exemption_allowed.setter
    def secured_packet_exemption_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the securedPacketExemptionAllowed property value. Configures the firewall to allow the host computer to respond to unsolicited network traffic of that traffic is secured by IPSec even when stealthModeBlocked is set to true. When SecuredPacketExemptionBlocked and SecuredPacketExemptionAllowed are both true, SecuredPacketExemptionAllowed takes priority.
        Args:
            value: Value to set for the securedPacketExemptionAllowed property.
        """
        self._secured_packet_exemption_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def stealth_mode_blocked(self,) -> Optional[bool]:
        """
        Gets the stealthModeBlocked property value. Prevent the server from operating in stealth mode. When StealthModeRequired and StealthModeBlocked are both true, StealthModeBlocked takes priority.
        Returns: Optional[bool]
        """
        return self._stealth_mode_blocked
    
    @stealth_mode_blocked.setter
    def stealth_mode_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the stealthModeBlocked property value. Prevent the server from operating in stealth mode. When StealthModeRequired and StealthModeBlocked are both true, StealthModeBlocked takes priority.
        Args:
            value: Value to set for the stealthModeBlocked property.
        """
        self._stealth_mode_blocked = value
    
    @property
    def unicast_responses_to_multicast_broadcasts_blocked(self,) -> Optional[bool]:
        """
        Gets the unicastResponsesToMulticastBroadcastsBlocked property value. Configures the firewall to block unicast responses to multicast broadcast traffic. When UnicastResponsesToMulticastBroadcastsRequired and UnicastResponsesToMulticastBroadcastsBlocked are both true, UnicastResponsesToMulticastBroadcastsBlocked takes priority.
        Returns: Optional[bool]
        """
        return self._unicast_responses_to_multicast_broadcasts_blocked
    
    @unicast_responses_to_multicast_broadcasts_blocked.setter
    def unicast_responses_to_multicast_broadcasts_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the unicastResponsesToMulticastBroadcastsBlocked property value. Configures the firewall to block unicast responses to multicast broadcast traffic. When UnicastResponsesToMulticastBroadcastsRequired and UnicastResponsesToMulticastBroadcastsBlocked are both true, UnicastResponsesToMulticastBroadcastsBlocked takes priority.
        Args:
            value: Value to set for the unicastResponsesToMulticastBroadcastsBlocked property.
        """
        self._unicast_responses_to_multicast_broadcasts_blocked = value
    

