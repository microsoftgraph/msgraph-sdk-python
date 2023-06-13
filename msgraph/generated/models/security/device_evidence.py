from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence, defender_av_status, device_health_status, device_risk_score, logged_on_user, onboarding_status, vm_metadata

from . import alert_evidence

@dataclass
class DeviceEvidence(alert_evidence.AlertEvidence):
    # A unique identifier assigned to a device by Azure Active Directory (Azure AD) when device is Azure AD-joined.
    azure_ad_device_id: Optional[str] = None
    # State of the Defender AntiMalware engine. The possible values are: notReporting, disabled, notUpdated, updated, unknown, notSupported, unknownFutureValue.
    defender_av_status: Optional[defender_av_status.DefenderAvStatus] = None
    # The fully qualified domain name (FQDN) for the device.
    device_dns_name: Optional[str] = None
    # The date and time when the device was first seen.
    first_seen_date_time: Optional[datetime] = None
    # The health state of the device.The possible values are: active, inactive, impairedCommunication, noSensorData, noSensorDataImpairedCommunication, unknown, unknownFutureValue.
    health_status: Optional[device_health_status.DeviceHealthStatus] = None
    # The ipInterfaces property
    ip_interfaces: Optional[List[str]] = None
    # Users that were logged on the machine during the time of the alert.
    logged_on_users: Optional[List[logged_on_user.LoggedOnUser]] = None
    # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
    mde_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the machine onboarding to Microsoft Defender for Endpoint.The possible values are: insufficientInfo, onboarded, canBeOnboarded, unsupported, unknownFutureValue.
    onboarding_status: Optional[onboarding_status.OnboardingStatus] = None
    # The build version for the operating system the device is running.
    os_build: Optional[int] = None
    # The operating system platform the device is running.
    os_platform: Optional[str] = None
    # The ID of the role-based access control (RBAC) device group.
    rbac_group_id: Optional[int] = None
    # The name of the RBAC device group.
    rbac_group_name: Optional[str] = None
    # Risk score as evaluated by Microsoft Defender for Endpoint. The possible values are: none, informational, low, medium, high, unknownFutureValue.
    risk_score: Optional[device_risk_score.DeviceRiskScore] = None
    # The version of the operating system platform.
    version: Optional[str] = None
    # Metadata of the virtual machine (VM) on which Microsoft Defender for Endpoint is running.
    vm_metadata: Optional[vm_metadata.VmMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence, defender_av_status, device_health_status, device_risk_score, logged_on_user, onboarding_status, vm_metadata

        fields: Dict[str, Callable[[Any], None]] = {
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "defenderAvStatus": lambda n : setattr(self, 'defender_av_status', n.get_enum_value(defender_av_status.DefenderAvStatus)),
            "deviceDnsName": lambda n : setattr(self, 'device_dns_name', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(device_health_status.DeviceHealthStatus)),
            "ipInterfaces": lambda n : setattr(self, 'ip_interfaces', n.get_collection_of_primitive_values(str)),
            "loggedOnUsers": lambda n : setattr(self, 'logged_on_users', n.get_collection_of_object_values(logged_on_user.LoggedOnUser)),
            "mdeDeviceId": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(onboarding_status.OnboardingStatus)),
            "osBuild": lambda n : setattr(self, 'os_build', n.get_int_value()),
            "osPlatform": lambda n : setattr(self, 'os_platform', n.get_str_value()),
            "rbacGroupId": lambda n : setattr(self, 'rbac_group_id', n.get_int_value()),
            "rbacGroupName": lambda n : setattr(self, 'rbac_group_name', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_enum_value(device_risk_score.DeviceRiskScore)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "vmMetadata": lambda n : setattr(self, 'vm_metadata', n.get_object_value(vm_metadata.VmMetadata)),
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
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_enum_value("defenderAvStatus", self.defender_av_status)
        writer.write_str_value("deviceDnsName", self.device_dns_name)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_collection_of_primitive_values("ipInterfaces", self.ip_interfaces)
        writer.write_collection_of_object_values("loggedOnUsers", self.logged_on_users)
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_int_value("osBuild", self.os_build)
        writer.write_str_value("osPlatform", self.os_platform)
        writer.write_int_value("rbacGroupId", self.rbac_group_id)
        writer.write_str_value("rbacGroupName", self.rbac_group_name)
        writer.write_enum_value("riskScore", self.risk_score)
        writer.write_str_value("version", self.version)
        writer.write_object_value("vmMetadata", self.vm_metadata)
    

