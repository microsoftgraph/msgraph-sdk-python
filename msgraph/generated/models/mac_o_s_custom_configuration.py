from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSCustomConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the macOSCustomConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSCustomConfiguration"
    # Payload. (UTF8 encoded byte array)
    payload: Optional[bytes] = None
    # Payload file name (.mobileconfig
    payload_file_name: Optional[str] = None
    # Name that is displayed to the user.
    payload_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSCustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCustomConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSCustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "payload": lambda n : setattr(self, 'payload', n.get_bytes_value()),
            "payloadFileName": lambda n : setattr(self, 'payload_file_name', n.get_str_value()),
            "payloadName": lambda n : setattr(self, 'payload_name', n.get_str_value()),
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
        from .device_configuration import DeviceConfiguration

        writer.write_bytes_value("payload", self.payload)
        writer.write_str_value("payloadFileName", self.payload_file_name)
        writer.write_str_value("payloadName", self.payload_name)
    

