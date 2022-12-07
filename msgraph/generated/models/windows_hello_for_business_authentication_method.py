from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method = lazy_import('msgraph.generated.models.authentication_method')
authentication_method_key_strength = lazy_import('msgraph.generated.models.authentication_method_key_strength')
device = lazy_import('msgraph.generated.models.device')

class WindowsHelloForBusinessAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsHelloForBusinessAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod"
        # The date and time that this Windows Hello for Business key was registered.
        self._created_date_time: Optional[datetime] = None
        # The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        self._device: Optional[device.Device] = None
        # The name of the device on which Windows Hello for Business is registered
        self._display_name: Optional[str] = None
        # Key strength of this Windows Hello for Business key. Possible values are: normal, weak, unknown.
        self._key_strength: Optional[authentication_method_key_strength.AuthenticationMethodKeyStrength] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time that this Windows Hello for Business key was registered.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time that this Windows Hello for Business key was registered.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def device(self,) -> Optional[device.Device]:
        """
        Gets the device property value. The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        Returns: Optional[device.Device]
        """
        return self._device
    
    @device.setter
    def device(self,value: Optional[device.Device] = None) -> None:
        """
        Sets the device property value. The registered device on which this Windows Hello for Business key resides. Supports $expand. When you get a user's Windows Hello for Business registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/windowsHelloForBusinessMethods/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.
        Args:
            value: Value to set for the device property.
        """
        self._device = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the device on which Windows Hello for Business is registered
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the device on which Windows Hello for Business is registered
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device": lambda n : setattr(self, 'device', n.get_object_value(device.Device)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "key_strength": lambda n : setattr(self, 'key_strength', n.get_enum_value(authentication_method_key_strength.AuthenticationMethodKeyStrength)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_strength(self,) -> Optional[authentication_method_key_strength.AuthenticationMethodKeyStrength]:
        """
        Gets the keyStrength property value. Key strength of this Windows Hello for Business key. Possible values are: normal, weak, unknown.
        Returns: Optional[authentication_method_key_strength.AuthenticationMethodKeyStrength]
        """
        return self._key_strength
    
    @key_strength.setter
    def key_strength(self,value: Optional[authentication_method_key_strength.AuthenticationMethodKeyStrength] = None) -> None:
        """
        Sets the keyStrength property value. Key strength of this Windows Hello for Business key. Possible values are: normal, weak, unknown.
        Args:
            value: Value to set for the keyStrength property.
        """
        self._key_strength = value
    
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
    

