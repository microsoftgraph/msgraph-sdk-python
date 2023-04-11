from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class WatermarkProtectionValues(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new watermarkProtectionValues and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether to apply a watermark to any shared content.
        self._is_enabled_for_content_sharing: Optional[bool] = None
        # Indicates whether to apply a watermark to everyone's video feed.
        self._is_enabled_for_video: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WatermarkProtectionValues:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WatermarkProtectionValues
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WatermarkProtectionValues()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabledForContentSharing": lambda n : setattr(self, 'is_enabled_for_content_sharing', n.get_bool_value()),
            "isEnabledForVideo": lambda n : setattr(self, 'is_enabled_for_video', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_enabled_for_content_sharing(self,) -> Optional[bool]:
        """
        Gets the isEnabledForContentSharing property value. Indicates whether to apply a watermark to any shared content.
        Returns: Optional[bool]
        """
        return self._is_enabled_for_content_sharing
    
    @is_enabled_for_content_sharing.setter
    def is_enabled_for_content_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledForContentSharing property value. Indicates whether to apply a watermark to any shared content.
        Args:
            value: Value to set for the is_enabled_for_content_sharing property.
        """
        self._is_enabled_for_content_sharing = value
    
    @property
    def is_enabled_for_video(self,) -> Optional[bool]:
        """
        Gets the isEnabledForVideo property value. Indicates whether to apply a watermark to everyone's video feed.
        Returns: Optional[bool]
        """
        return self._is_enabled_for_video
    
    @is_enabled_for_video.setter
    def is_enabled_for_video(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabledForVideo property value. Indicates whether to apply a watermark to everyone's video feed.
        Args:
            value: Value to set for the is_enabled_for_video property.
        """
        self._is_enabled_for_video = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isEnabledForContentSharing", self.is_enabled_for_content_sharing)
        writer.write_bool_value("isEnabledForVideo", self.is_enabled_for_video)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

