from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_failure_reason = lazy_import('msgraph.generated.models.device_enrollment_failure_reason')
device_enrollment_type = lazy_import('msgraph.generated.models.device_enrollment_type')
device_management_troubleshooting_event = lazy_import('msgraph.generated.models.device_management_troubleshooting_event')

class EnrollmentTroubleshootingEvent(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent):
    def __init__(self,) -> None:
        """
        Instantiates a new EnrollmentTroubleshootingEvent and sets the default values.
        """
        super().__init__()
        # Azure AD device identifier.
        self._device_id: Optional[str] = None
        # Possible ways of adding a mobile device to management.
        self._enrollment_type: Optional[device_enrollment_type.DeviceEnrollmentType] = None
        # Top level failure categories for enrollment.
        self._failure_category: Optional[device_enrollment_failure_reason.DeviceEnrollmentFailureReason] = None
        # Detailed failure reason.
        self._failure_reason: Optional[str] = None
        # Device identifier created or collected by Intune.
        self._managed_device_identifier: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Operating System.
        self._operating_system: Optional[str] = None
        # OS Version.
        self._os_version: Optional[str] = None
        # Identifier for the user that tried to enroll the device.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnrollmentTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentTroubleshootingEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EnrollmentTroubleshootingEvent()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Azure AD device identifier.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Azure AD device identifier.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def enrollment_type(self,) -> Optional[device_enrollment_type.DeviceEnrollmentType]:
        """
        Gets the enrollmentType property value. Possible ways of adding a mobile device to management.
        Returns: Optional[device_enrollment_type.DeviceEnrollmentType]
        """
        return self._enrollment_type
    
    @enrollment_type.setter
    def enrollment_type(self,value: Optional[device_enrollment_type.DeviceEnrollmentType] = None) -> None:
        """
        Sets the enrollmentType property value. Possible ways of adding a mobile device to management.
        Args:
            value: Value to set for the enrollmentType property.
        """
        self._enrollment_type = value
    
    @property
    def failure_category(self,) -> Optional[device_enrollment_failure_reason.DeviceEnrollmentFailureReason]:
        """
        Gets the failureCategory property value. Top level failure categories for enrollment.
        Returns: Optional[device_enrollment_failure_reason.DeviceEnrollmentFailureReason]
        """
        return self._failure_category
    
    @failure_category.setter
    def failure_category(self,value: Optional[device_enrollment_failure_reason.DeviceEnrollmentFailureReason] = None) -> None:
        """
        Sets the failureCategory property value. Top level failure categories for enrollment.
        Args:
            value: Value to set for the failureCategory property.
        """
        self._failure_category = value
    
    @property
    def failure_reason(self,) -> Optional[str]:
        """
        Gets the failureReason property value. Detailed failure reason.
        Returns: Optional[str]
        """
        return self._failure_reason
    
    @failure_reason.setter
    def failure_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the failureReason property value. Detailed failure reason.
        Args:
            value: Value to set for the failureReason property.
        """
        self._failure_reason = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "enrollment_type": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(device_enrollment_type.DeviceEnrollmentType)),
            "failure_category": lambda n : setattr(self, 'failure_category', n.get_enum_value(device_enrollment_failure_reason.DeviceEnrollmentFailureReason)),
            "failure_reason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "managed_device_identifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_identifier(self,) -> Optional[str]:
        """
        Gets the managedDeviceIdentifier property value. Device identifier created or collected by Intune.
        Returns: Optional[str]
        """
        return self._managed_device_identifier
    
    @managed_device_identifier.setter
    def managed_device_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceIdentifier property value. Device identifier created or collected by Intune.
        Args:
            value: Value to set for the managedDeviceIdentifier property.
        """
        self._managed_device_identifier = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. Operating System.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. Operating System.
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. OS Version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. OS Version.
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_enum_value("failureCategory", self.failure_category)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Identifier for the user that tried to enroll the device.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Identifier for the user that tried to enroll the device.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

