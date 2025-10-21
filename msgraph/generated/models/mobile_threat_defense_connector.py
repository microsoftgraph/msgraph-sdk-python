from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

from .entity import Entity

@dataclass
class MobileThreatDefenseConnector(Entity, Parsable):
    """
    Entity which represents a connection to Mobile Threat Defense partner.
    """
    # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about installed applications from Intune for iOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about installed applications from Intune for iOS devices. Default value is FALSE.
    allow_partner_to_collect_i_o_s_application_metadata: Optional[bool] = None
    # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about personally installed applications from Intune for iOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about personally installed applications from Intune for iOS devices. Default value is FALSE.
    allow_partner_to_collect_i_o_s_personal_application_metadata: Optional[bool] = None
    # When TRUE, indicates that Intune must receive data from the Mobile Threat Defense partner prior to marking an Android device compliant. When FALSE, indicates that Intune may mark an Android device compliant before receiving data from the Mobile Threat Defense partner.
    android_device_blocked_on_missing_partner_data: Optional[bool] = None
    # When TRUE, indicates that data from the Mobile Threat Defense partner will be used during compliance evaluations for Android devices. When FALSE, indicates that data from the Mobile Threat Defense partner will not be used during compliance evaluations for Android devices. Default value is FALSE.
    android_enabled: Optional[bool] = None
    # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for Android devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for Android devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
    android_mobile_application_management_enabled: Optional[bool] = None
    # When TRUE, indicates that Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant. When FALSE, indicates that Intune may not recieve data from Mobile Threat Defense partner prior to making device compliant. Default value is FALSE.
    ios_device_blocked_on_missing_partner_data: Optional[bool] = None
    # When TRUE, indicates that data from the Mobile Threat Defense partner will be used during compliance evaluations for iOS devices. When FALSE, indicates that data from the Mobile Threat Defense partner will not be used during compliance evaluations for iOS devices. Default value is FALSE.
    ios_enabled: Optional[bool] = None
    # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for iOS devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for iOS devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
    ios_mobile_application_management_enabled: Optional[bool] = None
    # DateTime of last Heartbeat recieved from the Mobile Threat Defense partner
    last_heartbeat_date_time: Optional[datetime.datetime] = None
    # When TRUE, inidicates that configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, inidicates that configuration profile management via Microsoft Defender for Endpoint is disabled. Default value is FALSE.
    microsoft_defender_for_endpoint_attach_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Partner state of this tenant.
    partner_state: Optional[MobileThreatPartnerTenantState] = None
    # Indicates the number of days without receiving a heartbeat from a Mobile Threat Defense partner before the partner is marked as unresponsive. Intune will the ignore the data from this Mobile Threat Defense Partner for next compliance calculation.
    partner_unresponsiveness_threshold_in_days: Optional[int] = None
    # When TRUE, indicates that Intune will mark devices noncompliant on enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner. When FALSE, indicates that Intune will not mark devices noncompliant on enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner. Default value is FALSE.
    partner_unsupported_os_version_blocked: Optional[bool] = None
    # When TRUE, indicates that Intune must receive data from the data sync partner prior to marking a device compliant for Windows. When FALSE, indicates that Intune may mark a device compliant without receiving data from the data sync partner for Windows. Default value is FALSE.
    windows_device_blocked_on_missing_partner_data: Optional[bool] = None
    # When TRUE, indicates that data from the Mobile Threat Defense partner will be used during compliance evaluations for Windows. When FALSE, indicates that data from the Mobile Threat Defense partner will not be used during compliance evaluations for Windows. Default value is FALSE.
    windows_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileThreatDefenseConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileThreatDefenseConnector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileThreatDefenseConnector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

        from .entity import Entity
        from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

        fields: dict[str, Callable[[Any], None]] = {
            "allowPartnerToCollectIOSApplicationMetadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_application_metadata', n.get_bool_value()),
            "allowPartnerToCollectIOSPersonalApplicationMetadata": lambda n : setattr(self, 'allow_partner_to_collect_i_o_s_personal_application_metadata', n.get_bool_value()),
            "androidDeviceBlockedOnMissingPartnerData": lambda n : setattr(self, 'android_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "androidEnabled": lambda n : setattr(self, 'android_enabled', n.get_bool_value()),
            "androidMobileApplicationManagementEnabled": lambda n : setattr(self, 'android_mobile_application_management_enabled', n.get_bool_value()),
            "iosDeviceBlockedOnMissingPartnerData": lambda n : setattr(self, 'ios_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "iosEnabled": lambda n : setattr(self, 'ios_enabled', n.get_bool_value()),
            "iosMobileApplicationManagementEnabled": lambda n : setattr(self, 'ios_mobile_application_management_enabled', n.get_bool_value()),
            "lastHeartbeatDateTime": lambda n : setattr(self, 'last_heartbeat_date_time', n.get_datetime_value()),
            "microsoftDefenderForEndpointAttachEnabled": lambda n : setattr(self, 'microsoft_defender_for_endpoint_attach_enabled', n.get_bool_value()),
            "partnerState": lambda n : setattr(self, 'partner_state', n.get_enum_value(MobileThreatPartnerTenantState)),
            "partnerUnresponsivenessThresholdInDays": lambda n : setattr(self, 'partner_unresponsiveness_threshold_in_days', n.get_int_value()),
            "partnerUnsupportedOsVersionBlocked": lambda n : setattr(self, 'partner_unsupported_os_version_blocked', n.get_bool_value()),
            "windowsDeviceBlockedOnMissingPartnerData": lambda n : setattr(self, 'windows_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "windowsEnabled": lambda n : setattr(self, 'windows_enabled', n.get_bool_value()),
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
        writer.write_bool_value("allowPartnerToCollectIOSApplicationMetadata", self.allow_partner_to_collect_i_o_s_application_metadata)
        writer.write_bool_value("allowPartnerToCollectIOSPersonalApplicationMetadata", self.allow_partner_to_collect_i_o_s_personal_application_metadata)
        writer.write_bool_value("androidDeviceBlockedOnMissingPartnerData", self.android_device_blocked_on_missing_partner_data)
        writer.write_bool_value("androidEnabled", self.android_enabled)
        writer.write_bool_value("androidMobileApplicationManagementEnabled", self.android_mobile_application_management_enabled)
        writer.write_bool_value("iosDeviceBlockedOnMissingPartnerData", self.ios_device_blocked_on_missing_partner_data)
        writer.write_bool_value("iosEnabled", self.ios_enabled)
        writer.write_bool_value("iosMobileApplicationManagementEnabled", self.ios_mobile_application_management_enabled)
        writer.write_datetime_value("lastHeartbeatDateTime", self.last_heartbeat_date_time)
        writer.write_bool_value("microsoftDefenderForEndpointAttachEnabled", self.microsoft_defender_for_endpoint_attach_enabled)
        writer.write_enum_value("partnerState", self.partner_state)
        writer.write_int_value("partnerUnresponsivenessThresholdInDays", self.partner_unresponsiveness_threshold_in_days)
        writer.write_bool_value("partnerUnsupportedOsVersionBlocked", self.partner_unsupported_os_version_blocked)
        writer.write_bool_value("windowsDeviceBlockedOnMissingPartnerData", self.windows_device_blocked_on_missing_partner_data)
        writer.write_bool_value("windowsEnabled", self.windows_enabled)
    

