from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ImageInfo(AdditionalDataHolder, Parsable):
    @property
    def add_image_query(self,) -> Optional[bool]:
        """
        Gets the addImageQuery property value. Optional; parameter used to indicate the server is able to render image dynamically in response to parameterization. For example – a high contrast image
        Returns: Optional[bool]
        """
        return self._add_image_query
    
    @add_image_query.setter
    def add_image_query(self,value: Optional[bool] = None) -> None:
        """
        Sets the addImageQuery property value. Optional; parameter used to indicate the server is able to render image dynamically in response to parameterization. For example – a high contrast image
        Args:
            value: Value to set for the addImageQuery property.
        """
        self._add_image_query = value
    
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
    
    @property
    def alternate_text(self,) -> Optional[str]:
        """
        Gets the alternateText property value. Optional; alt-text accessible content for the image
        Returns: Optional[str]
        """
        return self._alternate_text
    
    @alternate_text.setter
    def alternate_text(self,value: Optional[str] = None) -> None:
        """
        Sets the alternateText property value. Optional; alt-text accessible content for the image
        Args:
            value: Value to set for the alternateText property.
        """
        self._alternate_text = value
    
    @property
    def alternative_text(self,) -> Optional[str]:
        """
        Gets the alternativeText property value. The alternativeText property
        Returns: Optional[str]
        """
        return self._alternative_text
    
    @alternative_text.setter
    def alternative_text(self,value: Optional[str] = None) -> None:
        """
        Sets the alternativeText property value. The alternativeText property
        Args:
            value: Value to set for the alternativeText property.
        """
        self._alternative_text = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new imageInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional; parameter used to indicate the server is able to render image dynamically in response to parameterization. For example – a high contrast image
        self._add_image_query: Optional[bool] = None
        # Optional; alt-text accessible content for the image
        self._alternate_text: Optional[str] = None
        # The alternativeText property
        self._alternative_text: Optional[str] = None
        # Optional; URI that points to an icon which represents the application used to generate the activity
        self._icon_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImageInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImageInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "add_image_query": lambda n : setattr(self, 'add_image_query', n.get_bool_value()),
            "alternate_text": lambda n : setattr(self, 'alternate_text', n.get_str_value()),
            "alternative_text": lambda n : setattr(self, 'alternative_text', n.get_str_value()),
            "icon_url": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def icon_url(self,) -> Optional[str]:
        """
        Gets the iconUrl property value. Optional; URI that points to an icon which represents the application used to generate the activity
        Returns: Optional[str]
        """
        return self._icon_url
    
    @icon_url.setter
    def icon_url(self,value: Optional[str] = None) -> None:
        """
        Sets the iconUrl property value. Optional; URI that points to an icon which represents the application used to generate the activity
        Args:
            value: Value to set for the iconUrl property.
        """
        self._icon_url = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_bool_value("addImageQuery", self.add_image_query)
        writer.write_str_value("alternateText", self.alternate_text)
        writer.write_str_value("alternativeText", self.alternative_text)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

