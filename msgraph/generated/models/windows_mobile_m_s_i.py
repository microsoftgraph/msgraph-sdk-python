from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class WindowsMobileMSI(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Windows Mobile MSI Line Of Business apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsMobileMSI"
    # The command line.
    command_line: Optional[str] = None
    # A boolean to control whether the app's version will be used to detect the app after it is installed on a device. Set this to true for Windows Mobile MSI Line of Business (LoB) apps that use a self update feature.
    ignore_version_detection: Optional[bool] = None
    # The product code.
    product_code: Optional[str] = None
    # The product version of Windows Mobile MSI Line of Business (LoB) app.
    product_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsMobileMSI:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMobileMSI
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsMobileMSI()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_lob_app import MobileLobApp

        from .mobile_lob_app import MobileLobApp

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("commandLine", self.command_line)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
    

