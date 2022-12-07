from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
entity = lazy_import('msgraph.generated.models.entity')
ios_updates_install_status = lazy_import('msgraph.generated.models.ios_updates_install_status')

class IosUpdateDeviceStatus(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def compliance_grace_period_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Returns: Optional[datetime]
        """
        return self._compliance_grace_period_expiration_date_time
    
    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Args:
            value: Value to set for the complianceGracePeriodExpirationDateTime property.
        """
        self._compliance_grace_period_expiration_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosUpdateDeviceStatus and sets the default values.
        """
        super().__init__()
        # The DateTime when device compliance grace period expires
        self._compliance_grace_period_expiration_date_time: Optional[datetime] = None
        # Device name of the DevicePolicyStatus.
        self._device_display_name: Optional[str] = None
        # The device id that is being reported.
        self._device_id: Optional[str] = None
        # The device model that is being reported
        self._device_model: Optional[str] = None
        # The installStatus property
        self._install_status: Optional[ios_updates_install_status.IosUpdatesInstallStatus] = None
        # Last modified date time of the policy report.
        self._last_reported_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The device version that is being reported.
        self._os_version: Optional[str] = None
        # The status property
        self._status: Optional[compliance_status.ComplianceStatus] = None
        # The User id that is being reported.
        self._user_id: Optional[str] = None
        # The User Name that is being reported
        self._user_name: Optional[str] = None
        # UserPrincipalName.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateDeviceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateDeviceStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosUpdateDeviceStatus()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Device name of the DevicePolicyStatus.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Device name of the DevicePolicyStatus.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The device id that is being reported.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The device id that is being reported.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The device model that is being reported
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The device model that is being reported
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_grace_period_expiration_date_time": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "install_status": lambda n : setattr(self, 'install_status', n.get_enum_value(ios_updates_install_status.IosUpdatesInstallStatus)),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(compliance_status.ComplianceStatus)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_status(self,) -> Optional[ios_updates_install_status.IosUpdatesInstallStatus]:
        """
        Gets the installStatus property value. The installStatus property
        Returns: Optional[ios_updates_install_status.IosUpdatesInstallStatus]
        """
        return self._install_status
    
    @install_status.setter
    def install_status(self,value: Optional[ios_updates_install_status.IosUpdatesInstallStatus] = None) -> None:
        """
        Sets the installStatus property value. The installStatus property
        Args:
            value: Value to set for the installStatus property.
        """
        self._install_status = value
    
    @property
    def last_reported_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastReportedDateTime property value. Last modified date time of the policy report.
        Returns: Optional[datetime]
        """
        return self._last_reported_date_time
    
    @last_reported_date_time.setter
    def last_reported_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastReportedDateTime property value. Last modified date time of the policy report.
        Args:
            value: Value to set for the lastReportedDateTime property.
        """
        self._last_reported_date_time = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. The device version that is being reported.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. The device version that is being reported.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("complianceGracePeriodExpirationDateTime", self.compliance_grace_period_expiration_date_time)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("installStatus", self.install_status)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def status(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The User id that is being reported.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The User id that is being reported.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The User Name that is being reported
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The User Name that is being reported
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. UserPrincipalName.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. UserPrincipalName.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

