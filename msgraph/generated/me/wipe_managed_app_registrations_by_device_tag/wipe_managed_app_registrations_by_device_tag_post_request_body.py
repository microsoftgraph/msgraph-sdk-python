from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class WipeManagedAppRegistrationsByDeviceTagPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the wipeManagedAppRegistrationsByDeviceTag method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new wipeManagedAppRegistrationsByDeviceTagPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceTag property
        self._device_tag: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WipeManagedAppRegistrationsByDeviceTagPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WipeManagedAppRegistrationsByDeviceTagPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WipeManagedAppRegistrationsByDeviceTagPostRequestBody()
    
    @property
    def device_tag(self,) -> Optional[str]:
        """
        Gets the deviceTag property value. The deviceTag property
        Returns: Optional[str]
        """
        return self._device_tag
    
    @device_tag.setter
    def device_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceTag property value. The deviceTag property
        Args:
            value: Value to set for the deviceTag property.
        """
        self._device_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_tag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
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
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_additional_data_value(self.additional_data)
    

