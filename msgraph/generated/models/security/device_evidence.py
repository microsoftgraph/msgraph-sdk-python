from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .defender_av_status import DefenderAvStatus
    from .device_health_status import DeviceHealthStatus
    from .device_risk_score import DeviceRiskScore
    from .logged_on_user import LoggedOnUser
    from .onboarding_status import OnboardingStatus
    from .resource_access_event import ResourceAccessEvent
    from .vm_metadata import VmMetadata

from .alert_evidence import AlertEvidence

@dataclass
class DeviceEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.deviceEvidence"
    # A unique identifier assigned to a device by Microsoft Entra ID when device is Microsoft Entra joined.
    azure_ad_device_id: Optional[str] = None
    # State of the Defender anti-malware engine. The possible values are: notReporting, disabled, notUpdated, updated, unknown, notSupported, unknownFutureValue.
    defender_av_status: Optional[DefenderAvStatus] = None
    # The fully qualified domain name (FQDN) for the device.
    device_dns_name: Optional[str] = None
    # The DNS domain that this computer belongs to. A sequence of labels separated by dots.
    dns_domain: Optional[str] = None
    # The date and time when the device was first seen.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The health state of the device. The possible values are: active, inactive, impairedCommunication, noSensorData, noSensorDataImpairedCommunication, unknown, unknownFutureValue.
    health_status: Optional[DeviceHealthStatus] = None
    # The hostname without the domain suffix.
    host_name: Optional[str] = None
    # Ip interfaces of the device during the time of the alert.
    ip_interfaces: Optional[list[str]] = None
    # The lastExternalIpAddress property
    last_external_ip_address: Optional[str] = None
    # The lastIpAddress property
    last_ip_address: Optional[str] = None
    # Users that were logged on the machine during the time of the alert.
    logged_on_users: Optional[list[LoggedOnUser]] = None
    # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
    mde_device_id: Optional[str] = None
    # A logical grouping of computers within a Microsoft Windows network.
    nt_domain: Optional[str] = None
    # The status of the machine onboarding to Microsoft Defender for Endpoint. The possible values are: insufficientInfo, onboarded, canBeOnboarded, unsupported, unknownFutureValue.
    onboarding_status: Optional[OnboardingStatus] = None
    # The build version for the operating system the device is running.
    os_build: Optional[int] = None
    # The operating system platform the device is running.
    os_platform: Optional[str] = None
    # The ID of the role-based access control (RBAC) device group.
    rbac_group_id: Optional[int] = None
    # The name of the RBAC device group.
    rbac_group_name: Optional[str] = None
    # Information on resource access attempts made by the user account.
    resource_access_events: Optional[list[ResourceAccessEvent]] = None
    # Risk score as evaluated by Microsoft Defender for Endpoint. The possible values are: none, informational, low, medium, high, unknownFutureValue.
    risk_score: Optional[DeviceRiskScore] = None
    # The version of the operating system platform.
    version: Optional[str] = None
    # Metadata of the virtual machine (VM) on which Microsoft Defender for Endpoint is running.
    vm_metadata: Optional[VmMetadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .defender_av_status import DefenderAvStatus
        from .device_health_status import DeviceHealthStatus
        from .device_risk_score import DeviceRiskScore
        from .logged_on_user import LoggedOnUser
        from .onboarding_status import OnboardingStatus
        from .resource_access_event import ResourceAccessEvent
        from .vm_metadata import VmMetadata

        from .alert_evidence import AlertEvidence
        from .defender_av_status import DefenderAvStatus
        from .device_health_status import DeviceHealthStatus
        from .device_risk_score import DeviceRiskScore
        from .logged_on_user import LoggedOnUser
        from .onboarding_status import OnboardingStatus
        from .resource_access_event import ResourceAccessEvent
        from .vm_metadata import VmMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "defenderAvStatus": lambda n : setattr(self, 'defender_av_status', n.get_enum_value(DefenderAvStatus)),
            "deviceDnsName": lambda n : setattr(self, 'device_dns_name', n.get_str_value()),
            "dnsDomain": lambda n : setattr(self, 'dns_domain', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(DeviceHealthStatus)),
            "hostName": lambda n : setattr(self, 'host_name', n.get_str_value()),
            "ipInterfaces": lambda n : setattr(self, 'ip_interfaces', n.get_collection_of_primitive_values(str)),
            "lastExternalIpAddress": lambda n : setattr(self, 'last_external_ip_address', n.get_str_value()),
            "lastIpAddress": lambda n : setattr(self, 'last_ip_address', n.get_str_value()),
            "loggedOnUsers": lambda n : setattr(self, 'logged_on_users', n.get_collection_of_object_values(LoggedOnUser)),
            "mdeDeviceId": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "ntDomain": lambda n : setattr(self, 'nt_domain', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(OnboardingStatus)),
            "osBuild": lambda n : setattr(self, 'os_build', n.get_int_value()),
            "osPlatform": lambda n : setattr(self, 'os_platform', n.get_str_value()),
            "rbacGroupId": lambda n : setattr(self, 'rbac_group_id', n.get_int_value()),
            "rbacGroupName": lambda n : setattr(self, 'rbac_group_name', n.get_str_value()),
            "resourceAccessEvents": lambda n : setattr(self, 'resource_access_events', n.get_collection_of_object_values(ResourceAccessEvent)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_enum_value(DeviceRiskScore)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "vmMetadata": lambda n : setattr(self, 'vm_metadata', n.get_object_value(VmMetadata)),
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
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_enum_value("defenderAvStatus", self.defender_av_status)
        writer.write_str_value("deviceDnsName", self.device_dns_name)
        writer.write_str_value("dnsDomain", self.dns_domain)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("hostName", self.host_name)
        writer.write_collection_of_primitive_values("ipInterfaces", self.ip_interfaces)
        writer.write_str_value("lastExternalIpAddress", self.last_external_ip_address)
        writer.write_str_value("lastIpAddress", self.last_ip_address)
        writer.write_collection_of_object_values("loggedOnUsers", self.logged_on_users)
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
        writer.write_str_value("ntDomain", self.nt_domain)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_int_value("osBuild", self.os_build)
        writer.write_str_value("osPlatform", self.os_platform)
        writer.write_int_value("rbacGroupId", self.rbac_group_id)
        writer.write_str_value("rbacGroupName", self.rbac_group_name)
        writer.write_collection_of_object_values("resourceAccessEvents", self.resource_access_events)
        writer.write_enum_value("riskScore", self.risk_score)
        writer.write_str_value("version", self.version)
        writer.write_object_value("vmMetadata", self.vm_metadata)
    

