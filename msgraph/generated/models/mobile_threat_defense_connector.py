from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

from .entity import Entity

@dataclass
class MobileThreatDefenseConnector(Entity):
    """
    Entity which represents a connection to Mobile Threat Defense partner.
    """
    # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about installed applications from Intune for IOS devices. Default value is FALSE.
    allow_partner_to_collect_i_o_s_application_metadata: Optional[bool] = None
    # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about personally installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about personally installed applications from Intune for IOS devices. Default value is FALSE.
    allow_partner_to_collect_i_o_s_personal_application_metadata: Optional[bool] = None
    # For Android, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
    android_device_blocked_on_missing_partner_data: Optional[bool] = None
    # For Android, set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
    android_enabled: Optional[bool] = None
    # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for Android devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for Android devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
    android_mobile_application_management_enabled: Optional[bool] = None
    # For IOS, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
    ios_device_blocked_on_missing_partner_data: Optional[bool] = None
    # For IOS, get or set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
    ios_enabled: Optional[bool] = None
    # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for IOS devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for IOS devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
    ios_mobile_application_management_enabled: Optional[bool] = None
    # DateTime of last Heartbeat recieved from the Mobile Threat Defense partner
    last_heartbeat_date_time: Optional[datetime.datetime] = None
    # When TRUE, inidicates that configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, inidicates that configuration profile management via Microsoft Defender for Endpoint is disabled. Default value is FALSE.
    microsoft_defender_for_endpoint_attach_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Partner state of this tenant.
    partner_state: Optional[MobileThreatPartnerTenantState] = None
    # Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
    partner_unresponsiveness_threshold_in_days: Optional[int] = None
    # Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner
    partner_unsupported_os_version_blocked: Optional[bool] = None
    # When TRUE, inidicates that Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant for Windows. When FALSE, inidicates that Intune may make a device compliant without receiving data from the Mobile Threat Defense partner for Windows. Default value is FALSE.
    windows_device_blocked_on_missing_partner_data: Optional[bool] = None
    # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during compliance evaluations for Windows. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during compliance evaluations for Windows. Default value is FALSE.
    windows_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileThreatDefenseConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileThreatDefenseConnector
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileThreatDefenseConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

        from .entity import Entity
        from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

        fields: Dict[str, Callable[[Any], None]] = {
            "allow_partner_to_collect_i_o_s_application_metadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_application_metadata', n.get_bool_value()),
            "allow_partner_to_collect_i_o_s_personal_application_metadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_personal_application_metadata', n.get_bool_value()),
            "android_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'android_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "android_enabled": lambda n : setattr(self, 'android_enabled', n.get_bool_value()),
            "android_mobile_application_management_enabled": lambda n : setattr(self, 'android_mobile_application_management_enabled', n.get_bool_value()),
            "ios_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'ios_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "ios_enabled": lambda n : setattr(self, 'ios_enabled', n.get_bool_value()),
            "ios_mobile_application_management_enabled": lambda n : setattr(self, 'ios_mobile_application_management_enabled', n.get_bool_value()),
            "last_heartbeat_date_time": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "microsoft_defender_for_endpoint_attach_enabled": lambda n : setattr(self, 'microsoft_defender_for_endpoint_attach_enabled', n.get_bool_value()),
            "partner_state": lambda n : setattr(self, 'partner_state', n.get_enum_value(MobileThreatPartnerTenantState)),
            "partner_unresponsiveness_threshold_in_days": lambda n : setattr(self, 'partner_unresponsiveness_threshold_in_days', n.get_int_value()),
            "partner_unsupported_os_version_blocked": lambda n : setattr(self, 'partner_unsupported_os_version_blocked', n.get_bool_value()),
            "windows_device_blocked_on_missing_partner_data": lambda n : setattr(self, 'windows_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "windows_enabled": lambda n : setattr(self, 'windows_enabled', n.get_bool_value()),
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
        writer.write_bool_value("allow_partner_to_collect_i_o_s_application_metadata", self.allow_partner_to_collect_i_o_s_application_metadata)
        writer.write_bool_value("allow_partner_to_collect_i_o_s_personal_application_metadata", self.allow_partner_to_collect_i_o_s_personal_application_metadata)
        writer.write_bool_value("android_device_blocked_on_missing_partner_data", self.android_device_blocked_on_missing_partner_data)
        writer.write_bool_value("android_enabled", self.android_enabled)
        writer.write_bool_value("android_mobile_application_management_enabled", self.android_mobile_application_management_enabled)
        writer.write_bool_value("ios_device_blocked_on_missing_partner_data", self.ios_device_blocked_on_missing_partner_data)
        writer.write_bool_value("ios_enabled", self.ios_enabled)
        writer.write_bool_value("ios_mobile_application_management_enabled", self.ios_mobile_application_management_enabled)
        writer.write_datetime_value("last_heartbeat_date_time", self.last_heartbeat_date_time)
        writer.write_bool_value("microsoft_defender_for_endpoint_attach_enabled", self.microsoft_defender_for_endpoint_attach_enabled)
        writer.write_enum_value("partner_state", self.partner_state)
        writer.write_int_value("partner_unresponsiveness_threshold_in_days", self.partner_unresponsiveness_threshold_in_days)
        writer.write_bool_value("partner_unsupported_os_version_blocked", self.partner_unsupported_os_version_blocked)
        writer.write_bool_value("windows_device_blocked_on_missing_partner_data", self.windows_device_blocked_on_missing_partner_data)
        writer.write_bool_value("windows_enabled", self.windows_enabled)
    

