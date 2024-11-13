from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_device_account import WindowsDeviceAccount

from .windows_device_account import WindowsDeviceAccount

@dataclass
class WindowsDeviceADAccount(WindowsDeviceAccount, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsDeviceADAccount"
    # Not yet documented
    domain_name: Optional[str] = None
    # Not yet documented
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsDeviceADAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDeviceADAccount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsDeviceADAccount()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_device_account import WindowsDeviceAccount

        from .windows_device_account import WindowsDeviceAccount

        fields: Dict[str, Callable[[Any], None]] = {
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        from .windows_device_account import WindowsDeviceAccount

        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("userName", self.user_name)
    

