from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method, authentication_method_key_strength, device

from . import authentication_method

@dataclass
class WindowsHelloForBusinessAuthenticationMethod(authentication_method.AuthenticationMethod):
    odata_type = "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod"
    # The date and time that this Windows Hello for Business key was registered.
    created_date_time: Optional[datetime] = None
    # The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
    device: Optional[device.Device] = None
    # The name of the device on which Windows Hello for Business is registered
    display_name: Optional[str] = None
    # Key strength of this Windows Hello for Business key. Possible values are: normal, weak, unknown.
    key_strength: Optional[authentication_method_key_strength.AuthenticationMethodKeyStrength] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsHelloForBusinessAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsHelloForBusinessAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsHelloForBusinessAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method, authentication_method_key_strength, device

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(device.Device)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "keyStrength": lambda n : setattr(self, 'key_strength', n.get_enum_value(authentication_method_key_strength.AuthenticationMethodKeyStrength)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("device", self.device)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("keyStrength", self.key_strength)
    

