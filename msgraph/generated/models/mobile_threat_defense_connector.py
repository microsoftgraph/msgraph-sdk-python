from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, mobile_threat_partner_tenant_state

from . import entity

class MobileThreatDefenseConnector(entity.Entity):
    """
    Entity which represents a connection to Mobile Threat Defense partner.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileThreatDefenseConnector and sets the default values.
        """
        super().__init__()
        # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about installed applications from Intune for IOS devices. Default value is FALSE.
        self._allow_partner_to_collect_i_o_s_application_metadata: Optional[bool] = None
        # When TRUE, indicates the Mobile Threat Defense partner may collect metadata about personally installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about personally installed applications from Intune for IOS devices. Default value is FALSE.
        self._allow_partner_to_collect_i_o_s_personal_application_metadata: Optional[bool] = None
        # For Android, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        self._android_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For Android, set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        self._android_enabled: Optional[bool] = None
        # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for Android devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for Android devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        self._android_mobile_application_management_enabled: Optional[bool] = None
        # For IOS, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        self._ios_device_blocked_on_missing_partner_data: Optional[bool] = None
        # For IOS, get or set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        self._ios_enabled: Optional[bool] = None
        # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for IOS devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for IOS devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        self._ios_mobile_application_management_enabled: Optional[bool] = None
        # DateTime of last Heartbeat recieved from the Mobile Threat Defense partner
        self._last_heartbeat_date_time: Optional[datetime] = None
        # When TRUE, inidicates that configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, inidicates that configuration profile management via Microsoft Defender for Endpoint is disabled. Default value is FALSE.
        self._microsoft_defender_for_endpoint_attach_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Partner state of this tenant.
        self._partner_state: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState] = None
        # Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        self._partner_unresponsiveness_threshold_in_days: Optional[int] = None
        # Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner
        self._partner_unsupported_os_version_blocked: Optional[bool] = None
        # When TRUE, inidicates that Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant for Windows. When FALSE, inidicates that Intune may make a device compliant without receiving data from the Mobile Threat Defense partner for Windows. Default value is FALSE.
        self._windows_device_blocked_on_missing_partner_data: Optional[bool] = None
        # When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during compliance evaluations for Windows. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during compliance evaluations for Windows. Default value is FALSE.
        self._windows_enabled: Optional[bool] = None
    
    @property
    def allow_partner_to_collect_i_o_s_application_metadata(self,) -> Optional[bool]:
        """
        Gets the allowPartnerToCollectIOSApplicationMetadata property value. When TRUE, indicates the Mobile Threat Defense partner may collect metadata about installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about installed applications from Intune for IOS devices. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._allow_partner_to_collect_i_o_s_application_metadata
    
    @allow_partner_to_collect_i_o_s_application_metadata.setter
    def allow_partner_to_collect_i_o_s_application_metadata(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPartnerToCollectIOSApplicationMetadata property value. When TRUE, indicates the Mobile Threat Defense partner may collect metadata about installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about installed applications from Intune for IOS devices. Default value is FALSE.
        Args:
            value: Value to set for the allow_partner_to_collect_i_o_s_application_metadata property.
        """
        self._allow_partner_to_collect_i_o_s_application_metadata = value
    
    @property
    def allow_partner_to_collect_i_o_s_personal_application_metadata(self,) -> Optional[bool]:
        """
        Gets the allowPartnerToCollectIOSPersonalApplicationMetadata property value. When TRUE, indicates the Mobile Threat Defense partner may collect metadata about personally installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about personally installed applications from Intune for IOS devices. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._allow_partner_to_collect_i_o_s_personal_application_metadata
    
    @allow_partner_to_collect_i_o_s_personal_application_metadata.setter
    def allow_partner_to_collect_i_o_s_personal_application_metadata(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPartnerToCollectIOSPersonalApplicationMetadata property value. When TRUE, indicates the Mobile Threat Defense partner may collect metadata about personally installed applications from Intune for IOS devices. When FALSE, indicates the Mobile Threat Defense partner may not collect metadata about personally installed applications from Intune for IOS devices. Default value is FALSE.
        Args:
            value: Value to set for the allow_partner_to_collect_i_o_s_personal_application_metadata property.
        """
        self._allow_partner_to_collect_i_o_s_personal_application_metadata = value
    
    @property
    def android_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the androidDeviceBlockedOnMissingPartnerData property value. For Android, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._android_device_blocked_on_missing_partner_data
    
    @android_device_blocked_on_missing_partner_data.setter
    def android_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidDeviceBlockedOnMissingPartnerData property value. For Android, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        Args:
            value: Value to set for the android_device_blocked_on_missing_partner_data property.
        """
        self._android_device_blocked_on_missing_partner_data = value
    
    @property
    def android_enabled(self,) -> Optional[bool]:
        """
        Gets the androidEnabled property value. For Android, set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._android_enabled
    
    @android_enabled.setter
    def android_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidEnabled property value. For Android, set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        Args:
            value: Value to set for the android_enabled property.
        """
        self._android_enabled = value
    
    @property
    def android_mobile_application_management_enabled(self,) -> Optional[bool]:
        """
        Gets the androidMobileApplicationManagementEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for Android devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for Android devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._android_mobile_application_management_enabled
    
    @android_mobile_application_management_enabled.setter
    def android_mobile_application_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the androidMobileApplicationManagementEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for Android devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for Android devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        Args:
            value: Value to set for the android_mobile_application_management_enabled property.
        """
        self._android_mobile_application_management_enabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileThreatDefenseConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileThreatDefenseConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileThreatDefenseConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, mobile_threat_partner_tenant_state

        fields: Dict[str, Callable[[Any], None]] = {
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
            "partnerState": lambda n : setattr(self, 'partner_state', n.get_enum_value(mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState)),
            "partnerUnresponsivenessThresholdInDays": lambda n : setattr(self, 'partner_unresponsiveness_threshold_in_days', n.get_int_value()),
            "partnerUnsupportedOsVersionBlocked": lambda n : setattr(self, 'partner_unsupported_os_version_blocked', n.get_bool_value()),
            "windowsDeviceBlockedOnMissingPartnerData": lambda n : setattr(self, 'windows_device_blocked_on_missing_partner_data', n.get_bool_value()),
            "windowsEnabled": lambda n : setattr(self, 'windows_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the iosDeviceBlockedOnMissingPartnerData property value. For IOS, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        Returns: Optional[bool]
        """
        return self._ios_device_blocked_on_missing_partner_data
    
    @ios_device_blocked_on_missing_partner_data.setter
    def ios_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosDeviceBlockedOnMissingPartnerData property value. For IOS, set whether Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant
        Args:
            value: Value to set for the ios_device_blocked_on_missing_partner_data property.
        """
        self._ios_device_blocked_on_missing_partner_data = value
    
    @property
    def ios_enabled(self,) -> Optional[bool]:
        """
        Gets the iosEnabled property value. For IOS, get or set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        Returns: Optional[bool]
        """
        return self._ios_enabled
    
    @ios_enabled.setter
    def ios_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosEnabled property value. For IOS, get or set whether data from the Mobile Threat Defense partner should be used during compliance evaluations
        Args:
            value: Value to set for the ios_enabled property.
        """
        self._ios_enabled = value
    
    @property
    def ios_mobile_application_management_enabled(self,) -> Optional[bool]:
        """
        Gets the iosMobileApplicationManagementEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for IOS devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for IOS devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._ios_mobile_application_management_enabled
    
    @ios_mobile_application_management_enabled.setter
    def ios_mobile_application_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the iosMobileApplicationManagementEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during Mobile Application Management (MAM) evaluations for IOS devices. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during Mobile Application Management (MAM) evaluations for IOS devices. Only one partner per platform may be enabled for Mobile Application Management (MAM) evaluation. Default value is FALSE.
        Args:
            value: Value to set for the ios_mobile_application_management_enabled property.
        """
        self._ios_mobile_application_management_enabled = value
    
    @property
    def last_heartbeat_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastHeartbeatDateTime property value. DateTime of last Heartbeat recieved from the Mobile Threat Defense partner
        Returns: Optional[datetime]
        """
        return self._last_heartbeat_date_time
    
    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastHeartbeatDateTime property value. DateTime of last Heartbeat recieved from the Mobile Threat Defense partner
        Args:
            value: Value to set for the last_heartbeat_date_time property.
        """
        self._last_heartbeat_date_time = value
    
    @property
    def microsoft_defender_for_endpoint_attach_enabled(self,) -> Optional[bool]:
        """
        Gets the microsoftDefenderForEndpointAttachEnabled property value. When TRUE, inidicates that configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, inidicates that configuration profile management via Microsoft Defender for Endpoint is disabled. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._microsoft_defender_for_endpoint_attach_enabled
    
    @microsoft_defender_for_endpoint_attach_enabled.setter
    def microsoft_defender_for_endpoint_attach_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftDefenderForEndpointAttachEnabled property value. When TRUE, inidicates that configuration profile management via Microsoft Defender for Endpoint is enabled. When FALSE, inidicates that configuration profile management via Microsoft Defender for Endpoint is disabled. Default value is FALSE.
        Args:
            value: Value to set for the microsoft_defender_for_endpoint_attach_enabled property.
        """
        self._microsoft_defender_for_endpoint_attach_enabled = value
    
    @property
    def partner_state(self,) -> Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState]:
        """
        Gets the partnerState property value. Partner state of this tenant.
        Returns: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState]
        """
        return self._partner_state
    
    @partner_state.setter
    def partner_state(self,value: Optional[mobile_threat_partner_tenant_state.MobileThreatPartnerTenantState] = None) -> None:
        """
        Sets the partnerState property value. Partner state of this tenant.
        Args:
            value: Value to set for the partner_state property.
        """
        self._partner_state = value
    
    @property
    def partner_unresponsiveness_threshold_in_days(self,) -> Optional[int]:
        """
        Gets the partnerUnresponsivenessThresholdInDays property value. Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        Returns: Optional[int]
        """
        return self._partner_unresponsiveness_threshold_in_days
    
    @partner_unresponsiveness_threshold_in_days.setter
    def partner_unresponsiveness_threshold_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the partnerUnresponsivenessThresholdInDays property value. Get or Set days the per tenant tolerance to unresponsiveness for this partner integration
        Args:
            value: Value to set for the partner_unresponsiveness_threshold_in_days property.
        """
        self._partner_unresponsiveness_threshold_in_days = value
    
    @property
    def partner_unsupported_os_version_blocked(self,) -> Optional[bool]:
        """
        Gets the partnerUnsupportedOsVersionBlocked property value. Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner
        Returns: Optional[bool]
        """
        return self._partner_unsupported_os_version_blocked
    
    @partner_unsupported_os_version_blocked.setter
    def partner_unsupported_os_version_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the partnerUnsupportedOsVersionBlocked property value. Get or set whether to block devices on the enabled platforms that do not meet the minimum version requirements of the Mobile Threat Defense partner
        Args:
            value: Value to set for the partner_unsupported_os_version_blocked property.
        """
        self._partner_unsupported_os_version_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def windows_device_blocked_on_missing_partner_data(self,) -> Optional[bool]:
        """
        Gets the windowsDeviceBlockedOnMissingPartnerData property value. When TRUE, inidicates that Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant for Windows. When FALSE, inidicates that Intune may make a device compliant without receiving data from the Mobile Threat Defense partner for Windows. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._windows_device_blocked_on_missing_partner_data
    
    @windows_device_blocked_on_missing_partner_data.setter
    def windows_device_blocked_on_missing_partner_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsDeviceBlockedOnMissingPartnerData property value. When TRUE, inidicates that Intune must receive data from the Mobile Threat Defense partner prior to marking a device compliant for Windows. When FALSE, inidicates that Intune may make a device compliant without receiving data from the Mobile Threat Defense partner for Windows. Default value is FALSE.
        Args:
            value: Value to set for the windows_device_blocked_on_missing_partner_data property.
        """
        self._windows_device_blocked_on_missing_partner_data = value
    
    @property
    def windows_enabled(self,) -> Optional[bool]:
        """
        Gets the windowsEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during compliance evaluations for Windows. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during compliance evaluations for Windows. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._windows_enabled
    
    @windows_enabled.setter
    def windows_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsEnabled property value. When TRUE, inidicates that data from the Mobile Threat Defense partner can be used during compliance evaluations for Windows. When FALSE, inidicates that data from the Mobile Threat Defense partner should not be used during compliance evaluations for Windows. Default value is FALSE.
        Args:
            value: Value to set for the windows_enabled property.
        """
        self._windows_enabled = value
    

