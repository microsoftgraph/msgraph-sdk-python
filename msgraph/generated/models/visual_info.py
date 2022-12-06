from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

image_info = lazy_import('msgraph.generated.models.image_info')
json = lazy_import('msgraph.generated.models.json')

class VisualInfo(AdditionalDataHolder, Parsable):
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
    def attribution(self,) -> Optional[image_info.ImageInfo]:
        """
        Gets the attribution property value. Optional. JSON object used to represent an icon which represents the application used to generate the activity
        Returns: Optional[image_info.ImageInfo]
        """
        return self._attribution
    
    @attribution.setter
    def attribution(self,value: Optional[image_info.ImageInfo] = None) -> None:
        """
        Sets the attribution property value. Optional. JSON object used to represent an icon which represents the application used to generate the activity
        Args:
            value: Value to set for the attribution property.
        """
        self._attribution = value
    
    @property
    def background_color(self,) -> Optional[str]:
        """
        Gets the backgroundColor property value. Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color
        Returns: Optional[str]
        """
        return self._background_color
    
    @background_color.setter
    def background_color(self,value: Optional[str] = None) -> None:
        """
        Sets the backgroundColor property value. Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color
        Args:
            value: Value to set for the backgroundColor property.
        """
        self._background_color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new visualInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional. JSON object used to represent an icon which represents the application used to generate the activity
        self._attribution: Optional[image_info.ImageInfo] = None
        # Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color
        self._background_color: Optional[str] = None
        # Optional. Custom piece of data - JSON object used to provide custom content to render the activity in the Windows Shell UI
        self._content: Optional[json.Json] = None
        # Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)
        self._description: Optional[str] = None
        # Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)
        self._display_text: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[json.Json]:
        """
        Gets the content property value. Optional. Custom piece of data - JSON object used to provide custom content to render the activity in the Windows Shell UI
        Returns: Optional[json.Json]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the content property value. Optional. Custom piece of data - JSON object used to provide custom content to render the activity in the Windows Shell UI
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VisualInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VisualInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VisualInfo()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_text(self,) -> Optional[str]:
        """
        Gets the displayText property value. Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)
        Returns: Optional[str]
        """
        return self._display_text
    
    @display_text.setter
    def display_text(self,value: Optional[str] = None) -> None:
        """
        Sets the displayText property value. Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)
        Args:
            value: Value to set for the displayText property.
        """
        self._display_text = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attribution": lambda n : setattr(self, 'attribution', n.get_object_value(image_info.ImageInfo)),
            "background_color": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_object_value(json.Json)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_text": lambda n : setattr(self, 'display_text', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
        writer.write_object_value("attribution", self.attribution)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_object_value("content", self.content)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayText", self.display_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

