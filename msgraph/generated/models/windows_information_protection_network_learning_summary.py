from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsInformationProtectionNetworkLearningSummary(entity.Entity):
    """
    Windows Information Protection Network learning Summary entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionNetworkLearningSummary and sets the default values.
        """
        super().__init__()
        # Device Count
        self._device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Website url
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionNetworkLearningSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionNetworkLearningSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionNetworkLearningSummary()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. Device Count
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. Device Count
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("url", self.url)
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. Website url
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. Website url
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

