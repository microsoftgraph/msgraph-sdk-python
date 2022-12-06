from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teleconference_device_quality = lazy_import('msgraph.generated.models.teleconference_device_quality')

class LogTeleconferenceDeviceQualityPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the logTeleconferenceDeviceQuality method.
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
        Instantiates a new logTeleconferenceDeviceQualityPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The quality property
        self._quality: Optional[teleconference_device_quality.TeleconferenceDeviceQuality] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LogTeleconferenceDeviceQualityPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LogTeleconferenceDeviceQualityPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LogTeleconferenceDeviceQualityPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "quality": lambda n : setattr(self, 'quality', n.get_object_value(teleconference_device_quality.TeleconferenceDeviceQuality)),
        }
        return fields
    
    @property
    def quality(self,) -> Optional[teleconference_device_quality.TeleconferenceDeviceQuality]:
        """
        Gets the quality property value. The quality property
        Returns: Optional[teleconference_device_quality.TeleconferenceDeviceQuality]
        """
        return self._quality
    
    @quality.setter
    def quality(self,value: Optional[teleconference_device_quality.TeleconferenceDeviceQuality] = None) -> None:
        """
        Sets the quality property value. The quality property
        Args:
            value: Value to set for the quality property.
        """
        self._quality = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("quality", self.quality)
        writer.write_additional_data_value(self.additional_data)
    

