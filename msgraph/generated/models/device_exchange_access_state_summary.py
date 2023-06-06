from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceExchangeAccessStateSummary(AdditionalDataHolder, Parsable):
    """
    Device Exchange Access State summary
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Total count of devices with Exchange Access State: Allowed.
    allowed_device_count: Optional[int] = None
    # Total count of devices with Exchange Access State: Blocked.
    blocked_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total count of devices with Exchange Access State: Quarantined.
    quarantined_device_count: Optional[int] = None
    # Total count of devices for which no Exchange Access State could be found.
    unavailable_device_count: Optional[int] = None
    # Total count of devices with Exchange Access State: Unknown.
    unknown_device_count: Optional[int] = None
    
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
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedDeviceCount": lambda n : setattr(self, 'allowed_device_count', n.get_int_value()),
            "blockedDeviceCount": lambda n : setattr(self, 'blocked_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quarantinedDeviceCount": lambda n : setattr(self, 'quarantined_device_count', n.get_int_value()),
            "unavailableDeviceCount": lambda n : setattr(self, 'unavailable_device_count', n.get_int_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
        }
        return fields
    
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
    

