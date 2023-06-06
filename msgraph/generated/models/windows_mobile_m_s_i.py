from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_lob_app

from . import mobile_lob_app

@dataclass
class WindowsMobileMSI(mobile_lob_app.MobileLobApp):
    odata_type = "#microsoft.graph.windowsMobileMSI"
    # The command line.
    command_line: Optional[str] = None
    # A boolean to control whether the app's version will be used to detect the app after it is installed on a device. Set this to true for Windows Mobile MSI Line of Business (LoB) apps that use a self update feature.
    ignore_version_detection: Optional[bool] = None
    # The product code.
    product_code: Optional[str] = None
    # The product version of Windows Mobile MSI Line of Business (LoB) app.
    product_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsMobileMSI:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMobileMSI
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsMobileMSI()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_lob_app

        fields: Dict[str, Callable[[Any], None]] = {
            "commandLine": lambda n : setattr(self, 'command_line', n.get_str_value()),
            "ignoreVersionDetection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("commandLine", self.command_line)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
    

