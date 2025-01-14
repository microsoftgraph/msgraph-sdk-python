from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason
    from .device_enrollment_type import DeviceEnrollmentType
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

@dataclass
class EnrollmentTroubleshootingEvent(DeviceManagementTroubleshootingEvent, Parsable):
    """
    Event representing an enrollment failure.
    """
    # Azure AD device identifier.
    device_id: Optional[str] = None
    # Possible ways of adding a mobile device to management.
    enrollment_type: Optional[DeviceEnrollmentType] = None
    # Top level failure categories for enrollment.
    failure_category: Optional[DeviceEnrollmentFailureReason] = None
    # Detailed failure reason.
    failure_reason: Optional[str] = None
    # Device identifier created or collected by Intune.
    managed_device_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Operating System.
    operating_system: Optional[str] = None
    # OS Version.
    os_version: Optional[str] = None
    # Identifier for the user that tried to enroll the device.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnrollmentTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentTroubleshootingEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnrollmentTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason
        from .device_enrollment_type import DeviceEnrollmentType
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

        from .device_enrollment_failure_reason import DeviceEnrollmentFailureReason
        from .device_enrollment_type import DeviceEnrollmentType
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "enrollmentType": lambda n : setattr(self, 'enrollment_type', n.get_enum_value(DeviceEnrollmentType)),
            "failureCategory": lambda n : setattr(self, 'failure_category', n.get_enum_value(DeviceEnrollmentFailureReason)),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "managedDeviceIdentifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_enum_value("enrollmentType", self.enrollment_type)
        writer.write_enum_value("failureCategory", self.failure_category)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userId", self.user_id)
    

