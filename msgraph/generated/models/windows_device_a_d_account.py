from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_device_account = lazy_import('msgraph.generated.models.windows_device_account')

class WindowsDeviceADAccount(windows_device_account.WindowsDeviceAccount):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDeviceADAccount and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsDeviceADAccount"
        # Not yet documented
        self._domain_name: Optional[str] = None
        # Not yet documented
        self._user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDeviceADAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDeviceADAccount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDeviceADAccount()
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. Not yet documented
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. Not yet documented
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. Not yet documented
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. Not yet documented
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

