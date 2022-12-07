from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceEnrollmentPlatformRestriction(AdditionalDataHolder, Parsable):
    """
    Platform specific enrollment restrictions
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceEnrollmentPlatformRestriction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Max OS version supported
        self._os_maximum_version: Optional[str] = None
        # Min OS version supported
        self._os_minimum_version: Optional[str] = None
        # Block personally owned devices from enrolling
        self._personal_device_enrollment_blocked: Optional[bool] = None
        # Block the platform from enrolling
        self._platform_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentPlatformRestriction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestriction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentPlatformRestriction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "personal_device_enrollment_blocked": lambda n : setattr(self, 'personal_device_enrollment_blocked', n.get_bool_value()),
            "platform_blocked": lambda n : setattr(self, 'platform_blocked', n.get_bool_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Max OS version supported
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Max OS version supported
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Min OS version supported
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Min OS version supported
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def personal_device_enrollment_blocked(self,) -> Optional[bool]:
        """
        Gets the personalDeviceEnrollmentBlocked property value. Block personally owned devices from enrolling
        Returns: Optional[bool]
        """
        return self._personal_device_enrollment_blocked
    
    @personal_device_enrollment_blocked.setter
    def personal_device_enrollment_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the personalDeviceEnrollmentBlocked property value. Block personally owned devices from enrolling
        Args:
            value: Value to set for the personalDeviceEnrollmentBlocked property.
        """
        self._personal_device_enrollment_blocked = value
    
    @property
    def platform_blocked(self,) -> Optional[bool]:
        """
        Gets the platformBlocked property value. Block the platform from enrolling
        Returns: Optional[bool]
        """
        return self._platform_blocked
    
    @platform_blocked.setter
    def platform_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the platformBlocked property value. Block the platform from enrolling
        Args:
            value: Value to set for the platformBlocked property.
        """
        self._platform_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("personalDeviceEnrollmentBlocked", self.personal_device_enrollment_blocked)
        writer.write_bool_value("platformBlocked", self.platform_blocked)
        writer.write_additional_data_value(self.additional_data)
    

