from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceExchangeAccessStateSummary(AdditionalDataHolder, Parsable):
    """
    Device Exchange Access State summary
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
    
    @property
    def allowed_device_count(self,) -> Optional[int]:
        """
        Gets the allowedDeviceCount property value. Total count of devices with Exchange Access State: Allowed.
        Returns: Optional[int]
        """
        return self._allowed_device_count
    
    @allowed_device_count.setter
    def allowed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the allowedDeviceCount property value. Total count of devices with Exchange Access State: Allowed.
        Args:
            value: Value to set for the allowedDeviceCount property.
        """
        self._allowed_device_count = value
    
    @property
    def blocked_device_count(self,) -> Optional[int]:
        """
        Gets the blockedDeviceCount property value. Total count of devices with Exchange Access State: Blocked.
        Returns: Optional[int]
        """
        return self._blocked_device_count
    
    @blocked_device_count.setter
    def blocked_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the blockedDeviceCount property value. Total count of devices with Exchange Access State: Blocked.
        Args:
            value: Value to set for the blockedDeviceCount property.
        """
        self._blocked_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceExchangeAccessStateSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Total count of devices with Exchange Access State: Allowed.
        self._allowed_device_count: Optional[int] = None
        # Total count of devices with Exchange Access State: Blocked.
        self._blocked_device_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total count of devices with Exchange Access State: Quarantined.
        self._quarantined_device_count: Optional[int] = None
        # Total count of devices for which no Exchange Access State could be found.
        self._unavailable_device_count: Optional[int] = None
        # Total count of devices with Exchange Access State: Unknown.
        self._unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceExchangeAccessStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceExchangeAccessStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceExchangeAccessStateSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_device_count": lambda n : setattr(self, 'allowed_device_count', n.get_int_value()),
            "blocked_device_count": lambda n : setattr(self, 'blocked_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quarantined_device_count": lambda n : setattr(self, 'quarantined_device_count', n.get_int_value()),
            "unavailable_device_count": lambda n : setattr(self, 'unavailable_device_count', n.get_int_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
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
    def quarantined_device_count(self,) -> Optional[int]:
        """
        Gets the quarantinedDeviceCount property value. Total count of devices with Exchange Access State: Quarantined.
        Returns: Optional[int]
        """
        return self._quarantined_device_count
    
    @quarantined_device_count.setter
    def quarantined_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the quarantinedDeviceCount property value. Total count of devices with Exchange Access State: Quarantined.
        Args:
            value: Value to set for the quarantinedDeviceCount property.
        """
        self._quarantined_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("allowedDeviceCount", self.allowed_device_count)
        writer.write_int_value("blockedDeviceCount", self.blocked_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("quarantinedDeviceCount", self.quarantined_device_count)
        writer.write_int_value("unavailableDeviceCount", self.unavailable_device_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def unavailable_device_count(self,) -> Optional[int]:
        """
        Gets the unavailableDeviceCount property value. Total count of devices for which no Exchange Access State could be found.
        Returns: Optional[int]
        """
        return self._unavailable_device_count
    
    @unavailable_device_count.setter
    def unavailable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unavailableDeviceCount property value. Total count of devices for which no Exchange Access State could be found.
        Args:
            value: Value to set for the unavailableDeviceCount property.
        """
        self._unavailable_device_count = value
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Total count of devices with Exchange Access State: Unknown.
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Total count of devices with Exchange Access State: Unknown.
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value
    

