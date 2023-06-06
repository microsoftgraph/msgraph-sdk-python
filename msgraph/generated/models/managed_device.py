from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_state, configuration_manager_client_enabled_features, device_action_result, device_category, device_compliance_policy_state, device_configuration_state, device_enrollment_type, device_health_attestation_state, device_management_exchange_access_state, device_management_exchange_access_state_reason, device_registration_state, entity, managed_device_owner_type, managed_device_partner_reported_health_state, management_agent_type, user

from . import entity

@dataclass
class ManagedDevice(entity.Entity):
    """
    Devices that are managed or pre-enrolled through Intune
    """
    # The code that allows the Activation Lock on managed device to be bypassed. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity in LIST call. Individual GET call with select query options is needed to retrieve actual values. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    activation_lock_bypass_code: Optional[str] = None
    # Android security patch level. This property is read-only.
    android_security_patch_level: Optional[str] = None
    # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
    azure_a_d_device_id: Optional[str] = None
    # Whether the device is Azure Active Directory registered. This property is read-only.
    azure_a_d_registered: Optional[bool] = None
    # The DateTime when device compliance grace period expires. This property is read-only.
    compliance_grace_period_expiration_date_time: Optional[datetime] = None
    # Compliance state.
    compliance_state: Optional[compliance_state.ComplianceState] = None
    # ConfigrMgr client enabled features. This property is read-only.
    configuration_manager_client_enabled_features: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures] = None
    # List of ComplexType deviceActionResult objects. This property is read-only.
    device_action_results: Optional[List[device_action_result.DeviceActionResult]] = None
    # Device category
    device_category: Optional[device_category.DeviceCategory] = None
    # Device category display name. This property is read-only.
    device_category_display_name: Optional[str] = None
    # Device compliance policy states for this device.
    device_compliance_policy_states: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]] = None
    # Device configuration states for this device.
    device_configuration_states: Optional[List[device_configuration_state.DeviceConfigurationState]] = None
    # Possible ways of adding a mobile device to management.
    device_enrollment_type: Optional[device_enrollment_type.DeviceEnrollmentType] = None
    # The device health attestation state. This property is read-only.
    device_health_attestation_state: Optional[device_health_attestation_state.DeviceHealthAttestationState] = None
    # Name of the device. This property is read-only.
    device_name: Optional[str] = None
    # Device registration status.
    device_registration_state: Optional[device_registration_state.DeviceRegistrationState] = None
    # Whether the device is Exchange ActiveSync activated. This property is read-only.
    eas_activated: Optional[bool] = None
    # Exchange ActivationSync activation time of the device. This property is read-only.
    eas_activation_date_time: Optional[datetime] = None
    # Exchange ActiveSync Id of the device. This property is read-only.
    eas_device_id: Optional[str] = None
    # Email(s) for the user associated with the device. This property is read-only.
    email_address: Optional[str] = None
    # Enrollment time of the device. This property is read-only.
    enrolled_date_time: Optional[datetime] = None
    # Indicates Ethernet MAC Address of the device. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity. Individual get call with select query options is needed to retrieve actual values. Example: deviceManagement/managedDevices({managedDeviceId})?$select=ethernetMacAddress Supports: $select. $Search is not supported. Read-only. This property is read-only.
    ethernet_mac_address: Optional[str] = None
    # Device Exchange Access State.
    exchange_access_state: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState] = None
    # Device Exchange Access State Reason.
    exchange_access_state_reason: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason] = None
    # Last time the device contacted Exchange. This property is read-only.
    exchange_last_successful_sync_date_time: Optional[datetime] = None
    # Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
    free_storage_space_in_bytes: Optional[int] = None
    # Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    iccid: Optional[str] = None
    # IMEI. This property is read-only.
    imei: Optional[str] = None
    # Device encryption status. This property is read-only.
    is_encrypted: Optional[bool] = None
    # Device supervised status. This property is read-only.
    is_supervised: Optional[bool] = None
    # whether the device is jail broken or rooted. This property is read-only.
    jail_broken: Optional[str] = None
    # The date and time that the device last completed a successful sync with Intune. This property is read-only.
    last_sync_date_time: Optional[datetime] = None
    # Automatically generated name to identify a device. Can be overwritten to a user friendly name.
    managed_device_name: Optional[str] = None
    # Owner type of device.
    managed_device_owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
    # The managementAgent property
    management_agent: Optional[management_agent_type.ManagementAgentType] = None
    # Reports device management certificate expiration date. This property is read-only.
    management_certificate_expiration_date: Optional[datetime] = None
    # Manufacturer of the device. This property is read-only.
    manufacturer: Optional[str] = None
    # MEID. This property is read-only.
    meid: Optional[str] = None
    # Model of the device. This property is read-only.
    model: Optional[str] = None
    # Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating system of the device. Windows, iOS, etc. This property is read-only.
    operating_system: Optional[str] = None
    # Operating system version of the device. This property is read-only.
    os_version: Optional[str] = None
    # Available health states for the Device Health API
    partner_reported_threat_state: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState] = None
    # Phone number of the device. This property is read-only.
    phone_number: Optional[str] = None
    # Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
    physical_memory_in_bytes: Optional[int] = None
    # An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
    remote_assistance_session_error_details: Optional[str] = None
    # Url that allows a Remote Assistance session to be established with the device. This property is read-only.
    remote_assistance_session_url: Optional[str] = None
    # Reports if the managed iOS device is user approval enrollment. This property is read-only.
    require_user_enrollment_approval: Optional[bool] = None
    # SerialNumber. This property is read-only.
    serial_number: Optional[str] = None
    # Subscriber Carrier. This property is read-only.
    subscriber_carrier: Optional[str] = None
    # Total Storage in Bytes. This property is read-only.
    total_storage_space_in_bytes: Optional[int] = None
    # Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
    udid: Optional[str] = None
    # User display name. This property is read-only.
    user_display_name: Optional[str] = None
    # Unique Identifier for the user associated with the device. This property is read-only.
    user_id: Optional[str] = None
    # Device user principal name. This property is read-only.
    user_principal_name: Optional[str] = None
    # The primary users associated with the managed device.
    users: Optional[List[user.User]] = None
    # Wi-Fi MAC. This property is read-only.
    wi_fi_mac_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_state, configuration_manager_client_enabled_features, device_action_result, device_category, device_compliance_policy_state, device_configuration_state, device_enrollment_type, device_health_attestation_state, device_management_exchange_access_state, device_management_exchange_access_state_reason, device_registration_state, entity, managed_device_owner_type, managed_device_partner_reported_health_state, management_agent_type, user

        fields: Dict[str, Callable[[Any], None]] = {
            "activationLockBypassCode": lambda n : setattr(self, 'activation_lock_bypass_code', n.get_str_value()),
            "androidSecurityPatchLevel": lambda n : setattr(self, 'android_security_patch_level', n.get_str_value()),
            "azureADDeviceId": lambda n : setattr(self, 'azure_a_d_device_id', n.get_str_value()),
            "azureADRegistered": lambda n : setattr(self, 'azure_a_d_registered', n.get_bool_value()),
            "complianceGracePeriodExpirationDateTime": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(compliance_state.ComplianceState)),
            "configurationManagerClientEnabledFeatures": lambda n : setattr(self, 'configuration_manager_client_enabled_features', n.get_object_value(configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures)),
            "deviceActionResults": lambda n : setattr(self, 'device_action_results', n.get_collection_of_object_values(device_action_result.DeviceActionResult)),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_object_value(device_category.DeviceCategory)),
            "deviceCategoryDisplayName": lambda n : setattr(self, 'device_category_display_name', n.get_str_value()),
            "deviceCompliancePolicyStates": lambda n : setattr(self, 'device_compliance_policy_states', n.get_collection_of_object_values(device_compliance_policy_state.DeviceCompliancePolicyState)),
            "deviceConfigurationStates": lambda n : setattr(self, 'device_configuration_states', n.get_collection_of_object_values(device_configuration_state.DeviceConfigurationState)),
            "deviceEnrollmentType": lambda n : setattr(self, 'device_enrollment_type', n.get_enum_value(device_enrollment_type.DeviceEnrollmentType)),
            "deviceHealthAttestationState": lambda n : setattr(self, 'device_health_attestation_state', n.get_object_value(device_health_attestation_state.DeviceHealthAttestationState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceRegistrationState": lambda n : setattr(self, 'device_registration_state', n.get_enum_value(device_registration_state.DeviceRegistrationState)),
            "easActivated": lambda n : setattr(self, 'eas_activated', n.get_bool_value()),
            "easActivationDateTime": lambda n : setattr(self, 'eas_activation_date_time', n.get_datetime_value()),
            "easDeviceId": lambda n : setattr(self, 'eas_device_id', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "ethernetMacAddress": lambda n : setattr(self, 'ethernet_mac_address', n.get_str_value()),
            "exchangeAccessState": lambda n : setattr(self, 'exchange_access_state', n.get_enum_value(device_management_exchange_access_state.DeviceManagementExchangeAccessState)),
            "exchangeAccessStateReason": lambda n : setattr(self, 'exchange_access_state_reason', n.get_enum_value(device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason)),
            "exchangeLastSuccessfulSyncDateTime": lambda n : setattr(self, 'exchange_last_successful_sync_date_time', n.get_datetime_value()),
            "freeStorageSpaceInBytes": lambda n : setattr(self, 'free_storage_space_in_bytes', n.get_int_value()),
            "iccid": lambda n : setattr(self, 'iccid', n.get_str_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "isSupervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "jailBroken": lambda n : setattr(self, 'jail_broken', n.get_str_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managedDeviceOwnerType": lambda n : setattr(self, 'managed_device_owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
            "managementAgent": lambda n : setattr(self, 'management_agent', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "managementCertificateExpirationDate": lambda n : setattr(self, 'management_certificate_expiration_date', n.get_datetime_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "partnerReportedThreatState": lambda n : setattr(self, 'partner_reported_threat_state', n.get_enum_value(managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "physicalMemoryInBytes": lambda n : setattr(self, 'physical_memory_in_bytes', n.get_int_value()),
            "remoteAssistanceSessionErrorDetails": lambda n : setattr(self, 'remote_assistance_session_error_details', n.get_str_value()),
            "remoteAssistanceSessionUrl": lambda n : setattr(self, 'remote_assistance_session_url', n.get_str_value()),
            "requireUserEnrollmentApproval": lambda n : setattr(self, 'require_user_enrollment_approval', n.get_bool_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "subscriberCarrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "totalStorageSpaceInBytes": lambda n : setattr(self, 'total_storage_space_in_bytes', n.get_int_value()),
            "udid": lambda n : setattr(self, 'udid', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(user.User)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "wiFiMacAddress": lambda n : setattr(self, 'wi_fi_mac_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_object_value("deviceCategory", self.device_category)
        writer.write_collection_of_object_values("deviceCompliancePolicyStates", self.device_compliance_policy_states)
        writer.write_collection_of_object_values("deviceConfigurationStates", self.device_configuration_states)
        writer.write_enum_value("deviceEnrollmentType", self.device_enrollment_type)
        writer.write_enum_value("deviceRegistrationState", self.device_registration_state)
        writer.write_enum_value("exchangeAccessState", self.exchange_access_state)
        writer.write_enum_value("exchangeAccessStateReason", self.exchange_access_state_reason)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_enum_value("managedDeviceOwnerType", self.managed_device_owner_type)
        writer.write_enum_value("managementAgent", self.management_agent)
        writer.write_str_value("notes", self.notes)
        writer.write_enum_value("partnerReportedThreatState", self.partner_reported_threat_state)
        writer.write_collection_of_object_values("users", self.users)
    

