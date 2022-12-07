from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
entity = lazy_import('msgraph.generated.models.entity')

class ManagedDeviceMobileAppConfigurationUserStatus(entity.Entity):
    """
    Contains properties, inherited properties and actions for an MDM mobile app configuration status for a user.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceMobileAppConfigurationUserStatus and sets the default values.
        """
        super().__init__()
        # Devices count for that user.
        self._devices_count: Optional[int] = None
        # Last modified date time of the policy report.
        self._last_reported_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[compliance_status.ComplianceStatus] = None
        # User name of the DevicePolicyStatus.
        self._user_display_name: Optional[str] = None
        # UserPrincipalName.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceMobileAppConfigurationUserStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceMobileAppConfigurationUserStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceMobileAppConfigurationUserStatus()
    
    @property
    def devices_count(self,) -> Optional[int]:
        """
        Gets the devicesCount property value. Devices count for that user.
        Returns: Optional[int]
        """
        return self._devices_count
    
    @devices_count.setter
    def devices_count(self,value: Optional[int] = None) -> None:
        """
        Sets the devicesCount property value. Devices count for that user.
        Args:
            value: Value to set for the devicesCount property.
        """
        self._devices_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "devices_count": lambda n : setattr(self, 'devices_count', n.get_int_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(compliance_status.ComplianceStatus)),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("devicesCount", self.devices_count)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userDisplayName", self.user_display_name)
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
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. User name of the DevicePolicyStatus.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. User name of the DevicePolicyStatus.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
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
    

