from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
defender_av_status = lazy_import('msgraph.generated.models.security.defender_av_status')
device_health_status = lazy_import('msgraph.generated.models.security.device_health_status')
device_risk_score = lazy_import('msgraph.generated.models.security.device_risk_score')
logged_on_user = lazy_import('msgraph.generated.models.security.logged_on_user')
onboarding_status = lazy_import('msgraph.generated.models.security.onboarding_status')
vm_metadata = lazy_import('msgraph.generated.models.security.vm_metadata')

class DeviceEvidence(alert_evidence.AlertEvidence):
    @property
    def azure_ad_device_id(self,) -> Optional[str]:
        """
        Gets the azureAdDeviceId property value. A unique identifier assigned to a device by Azure Active Directory (Azure AD) when device is Azure AD-joined.
        Returns: Optional[str]
        """
        return self._azure_ad_device_id
    
    @azure_ad_device_id.setter
    def azure_ad_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdDeviceId property value. A unique identifier assigned to a device by Azure Active Directory (Azure AD) when device is Azure AD-joined.
        Args:
            value: Value to set for the azureAdDeviceId property.
        """
        self._azure_ad_device_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEvidence and sets the default values.
        """
        super().__init__()
        # A unique identifier assigned to a device by Azure Active Directory (Azure AD) when device is Azure AD-joined.
        self._azure_ad_device_id: Optional[str] = None
        # State of the Defender AntiMalware engine. The possible values are: notReporting, disabled, notUpdated, updated, unknown, notSupported, unknownFutureValue.
        self._defender_av_status: Optional[defender_av_status.DefenderAvStatus] = None
        # The fully qualified domain name (FQDN) for the device.
        self._device_dns_name: Optional[str] = None
        # The date and time when the device was first seen.
        self._first_seen_date_time: Optional[datetime] = None
        # The health state of the device.The possible values are: active, inactive, impairedCommunication, noSensorData, noSensorDataImpairedCommunication, unknown, unknownFutureValue.
        self._health_status: Optional[device_health_status.DeviceHealthStatus] = None
        # Users that were logged on the machine during the time of the alert.
        self._logged_on_users: Optional[List[logged_on_user.LoggedOnUser]] = None
        # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        self._mde_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status of the machine onboarding to Microsoft Defender for Endpoint.The possible values are: insufficientInfo, onboarded, canBeOnboarded, unsupported, unknownFutureValue.
        self._onboarding_status: Optional[onboarding_status.OnboardingStatus] = None
        # The build version for the operating system the device is running.
        self._os_build: Optional[int] = None
        # The operating system platform the device is running.
        self._os_platform: Optional[str] = None
        # The ID of the role-based access control (RBAC) device group.
        self._rbac_group_id: Optional[int] = None
        # The name of the RBAC device group.
        self._rbac_group_name: Optional[str] = None
        # Risk score as evaluated by Microsoft Defender for Endpoint. The possible values are: none, informational, low, medium, high, unknownFutureValue.
        self._risk_score: Optional[device_risk_score.DeviceRiskScore] = None
        # The version of the operating system platform.
        self._version: Optional[str] = None
        # Metadata of the virtual machine (VM) on which Microsoft Defender for Endpoint is running.
        self._vm_metadata: Optional[vm_metadata.VmMetadata] = None
    
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
    
    @property
    def defender_av_status(self,) -> Optional[defender_av_status.DefenderAvStatus]:
        """
        Gets the defenderAvStatus property value. State of the Defender AntiMalware engine. The possible values are: notReporting, disabled, notUpdated, updated, unknown, notSupported, unknownFutureValue.
        Returns: Optional[defender_av_status.DefenderAvStatus]
        """
        return self._defender_av_status
    
    @defender_av_status.setter
    def defender_av_status(self,value: Optional[defender_av_status.DefenderAvStatus] = None) -> None:
        """
        Sets the defenderAvStatus property value. State of the Defender AntiMalware engine. The possible values are: notReporting, disabled, notUpdated, updated, unknown, notSupported, unknownFutureValue.
        Args:
            value: Value to set for the defenderAvStatus property.
        """
        self._defender_av_status = value
    
    @property
    def device_dns_name(self,) -> Optional[str]:
        """
        Gets the deviceDnsName property value. The fully qualified domain name (FQDN) for the device.
        Returns: Optional[str]
        """
        return self._device_dns_name
    
    @device_dns_name.setter
    def device_dns_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDnsName property value. The fully qualified domain name (FQDN) for the device.
        Args:
            value: Value to set for the deviceDnsName property.
        """
        self._device_dns_name = value
    
    @property
    def first_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstSeenDateTime property value. The date and time when the device was first seen.
        Returns: Optional[datetime]
        """
        return self._first_seen_date_time
    
    @first_seen_date_time.setter
    def first_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstSeenDateTime property value. The date and time when the device was first seen.
        Args:
            value: Value to set for the firstSeenDateTime property.
        """
        self._first_seen_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_ad_device_id": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "defender_av_status": lambda n : setattr(self, 'defender_av_status', n.get_enum_value(defender_av_status.DefenderAvStatus)),
            "device_dns_name": lambda n : setattr(self, 'device_dns_name', n.get_str_value()),
            "first_seen_date_time": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(device_health_status.DeviceHealthStatus)),
            "logged_on_users": lambda n : setattr(self, 'logged_on_users', n.get_collection_of_object_values(logged_on_user.LoggedOnUser)),
            "mde_device_id": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(onboarding_status.OnboardingStatus)),
            "os_build": lambda n : setattr(self, 'os_build', n.get_int_value()),
            "os_platform": lambda n : setattr(self, 'os_platform', n.get_str_value()),
            "rbac_group_id": lambda n : setattr(self, 'rbac_group_id', n.get_int_value()),
            "rbac_group_name": lambda n : setattr(self, 'rbac_group_name', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_enum_value(device_risk_score.DeviceRiskScore)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "vm_metadata": lambda n : setattr(self, 'vm_metadata', n.get_object_value(vm_metadata.VmMetadata)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_status(self,) -> Optional[device_health_status.DeviceHealthStatus]:
        """
        Gets the healthStatus property value. The health state of the device.The possible values are: active, inactive, impairedCommunication, noSensorData, noSensorDataImpairedCommunication, unknown, unknownFutureValue.
        Returns: Optional[device_health_status.DeviceHealthStatus]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[device_health_status.DeviceHealthStatus] = None) -> None:
        """
        Sets the healthStatus property value. The health state of the device.The possible values are: active, inactive, impairedCommunication, noSensorData, noSensorDataImpairedCommunication, unknown, unknownFutureValue.
        Args:
            value: Value to set for the healthStatus property.
        """
        self._health_status = value
    
    @property
    def logged_on_users(self,) -> Optional[List[logged_on_user.LoggedOnUser]]:
        """
        Gets the loggedOnUsers property value. Users that were logged on the machine during the time of the alert.
        Returns: Optional[List[logged_on_user.LoggedOnUser]]
        """
        return self._logged_on_users
    
    @logged_on_users.setter
    def logged_on_users(self,value: Optional[List[logged_on_user.LoggedOnUser]] = None) -> None:
        """
        Sets the loggedOnUsers property value. Users that were logged on the machine during the time of the alert.
        Args:
            value: Value to set for the loggedOnUsers property.
        """
        self._logged_on_users = value
    
    @property
    def mde_device_id(self,) -> Optional[str]:
        """
        Gets the mdeDeviceId property value. A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        Returns: Optional[str]
        """
        return self._mde_device_id
    
    @mde_device_id.setter
    def mde_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the mdeDeviceId property value. A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        Args:
            value: Value to set for the mdeDeviceId property.
        """
        self._mde_device_id = value
    
    @property
    def onboarding_status(self,) -> Optional[onboarding_status.OnboardingStatus]:
        """
        Gets the onboardingStatus property value. The status of the machine onboarding to Microsoft Defender for Endpoint.The possible values are: insufficientInfo, onboarded, canBeOnboarded, unsupported, unknownFutureValue.
        Returns: Optional[onboarding_status.OnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[onboarding_status.OnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The status of the machine onboarding to Microsoft Defender for Endpoint.The possible values are: insufficientInfo, onboarded, canBeOnboarded, unsupported, unknownFutureValue.
        Args:
            value: Value to set for the onboardingStatus property.
        """
        self._onboarding_status = value
    
    @property
    def os_build(self,) -> Optional[int]:
        """
        Gets the osBuild property value. The build version for the operating system the device is running.
        Returns: Optional[int]
        """
        return self._os_build
    
    @os_build.setter
    def os_build(self,value: Optional[int] = None) -> None:
        """
        Sets the osBuild property value. The build version for the operating system the device is running.
        Args:
            value: Value to set for the osBuild property.
        """
        self._os_build = value
    
    @property
    def os_platform(self,) -> Optional[str]:
        """
        Gets the osPlatform property value. The operating system platform the device is running.
        Returns: Optional[str]
        """
        return self._os_platform
    
    @os_platform.setter
    def os_platform(self,value: Optional[str] = None) -> None:
        """
        Sets the osPlatform property value. The operating system platform the device is running.
        Args:
            value: Value to set for the osPlatform property.
        """
        self._os_platform = value
    
    @property
    def rbac_group_id(self,) -> Optional[int]:
        """
        Gets the rbacGroupId property value. The ID of the role-based access control (RBAC) device group.
        Returns: Optional[int]
        """
        return self._rbac_group_id
    
    @rbac_group_id.setter
    def rbac_group_id(self,value: Optional[int] = None) -> None:
        """
        Sets the rbacGroupId property value. The ID of the role-based access control (RBAC) device group.
        Args:
            value: Value to set for the rbacGroupId property.
        """
        self._rbac_group_id = value
    
    @property
    def rbac_group_name(self,) -> Optional[str]:
        """
        Gets the rbacGroupName property value. The name of the RBAC device group.
        Returns: Optional[str]
        """
        return self._rbac_group_name
    
    @rbac_group_name.setter
    def rbac_group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the rbacGroupName property value. The name of the RBAC device group.
        Args:
            value: Value to set for the rbacGroupName property.
        """
        self._rbac_group_name = value
    
    @property
    def risk_score(self,) -> Optional[device_risk_score.DeviceRiskScore]:
        """
        Gets the riskScore property value. Risk score as evaluated by Microsoft Defender for Endpoint. The possible values are: none, informational, low, medium, high, unknownFutureValue.
        Returns: Optional[device_risk_score.DeviceRiskScore]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[device_risk_score.DeviceRiskScore] = None) -> None:
        """
        Sets the riskScore property value. Risk score as evaluated by Microsoft Defender for Endpoint. The possible values are: none, informational, low, medium, high, unknownFutureValue.
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
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
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the operating system platform.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the operating system platform.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    
    @property
    def vm_metadata(self,) -> Optional[vm_metadata.VmMetadata]:
        """
        Gets the vmMetadata property value. Metadata of the virtual machine (VM) on which Microsoft Defender for Endpoint is running.
        Returns: Optional[vm_metadata.VmMetadata]
        """
        return self._vm_metadata
    
    @vm_metadata.setter
    def vm_metadata(self,value: Optional[vm_metadata.VmMetadata] = None) -> None:
        """
        Sets the vmMetadata property value. Metadata of the virtual machine (VM) on which Microsoft Defender for Endpoint is running.
        Args:
            value: Value to set for the vmMetadata property.
        """
        self._vm_metadata = value
    

