from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ResourceVisualization(AdditionalDataHolder, Parsable):
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
        Instantiates a new resourceVisualization and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A string describing where the item is stored. For example, the name of a SharePoint site or the user name identifying the owner of the OneDrive storing the item.
        self._container_display_name: Optional[str] = None
        # Can be used for filtering by the type of container in which the file is stored. Such as Site or OneDriveBusiness.
        self._container_type: Optional[str] = None
        # A path leading to the folder in which the item is stored.
        self._container_web_url: Optional[str] = None
        # The item's media type. Can be used for filtering for a specific type of file based on supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
        self._media_type: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A URL leading to the preview image for the item.
        self._preview_image_url: Optional[str] = None
        # A preview text for the item.
        self._preview_text: Optional[str] = None
        # The item's title text.
        self._title: Optional[str] = None
        # The item's media type. Can be used for filtering for a specific file based on a specific type. See below for supported types.
        self._type: Optional[str] = None
    
    @property
    def container_display_name(self,) -> Optional[str]:
        """
        Gets the containerDisplayName property value. A string describing where the item is stored. For example, the name of a SharePoint site or the user name identifying the owner of the OneDrive storing the item.
        Returns: Optional[str]
        """
        return self._container_display_name
    
    @container_display_name.setter
    def container_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the containerDisplayName property value. A string describing where the item is stored. For example, the name of a SharePoint site or the user name identifying the owner of the OneDrive storing the item.
        Args:
            value: Value to set for the containerDisplayName property.
        """
        self._container_display_name = value
    
    @property
    def container_type(self,) -> Optional[str]:
        """
        Gets the containerType property value. Can be used for filtering by the type of container in which the file is stored. Such as Site or OneDriveBusiness.
        Returns: Optional[str]
        """
        return self._container_type
    
    @container_type.setter
    def container_type(self,value: Optional[str] = None) -> None:
        """
        Sets the containerType property value. Can be used for filtering by the type of container in which the file is stored. Such as Site or OneDriveBusiness.
        Args:
            value: Value to set for the containerType property.
        """
        self._container_type = value
    
    @property
    def container_web_url(self,) -> Optional[str]:
        """
        Gets the containerWebUrl property value. A path leading to the folder in which the item is stored.
        Returns: Optional[str]
        """
        return self._container_web_url
    
    @container_web_url.setter
    def container_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the containerWebUrl property value. A path leading to the folder in which the item is stored.
        Args:
            value: Value to set for the containerWebUrl property.
        """
        self._container_web_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceVisualization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceVisualization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceVisualization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "container_display_name": lambda n : setattr(self, 'container_display_name', n.get_str_value()),
            "container_type": lambda n : setattr(self, 'container_type', n.get_str_value()),
            "container_web_url": lambda n : setattr(self, 'container_web_url', n.get_str_value()),
            "media_type": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "preview_image_url": lambda n : setattr(self, 'preview_image_url', n.get_str_value()),
            "preview_text": lambda n : setattr(self, 'preview_text', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def media_type(self,) -> Optional[str]:
        """
        Gets the mediaType property value. The item's media type. Can be used for filtering for a specific type of file based on supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
        Returns: Optional[str]
        """
        return self._media_type
    
    @media_type.setter
    def media_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaType property value. The item's media type. Can be used for filtering for a specific type of file based on supported IANA Media Mime Types. Note that not all Media Mime Types are supported.
        Args:
            value: Value to set for the mediaType property.
        """
        self._media_type = value
    
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
    
    @property
    def preview_image_url(self,) -> Optional[str]:
        """
        Gets the previewImageUrl property value. A URL leading to the preview image for the item.
        Returns: Optional[str]
        """
        return self._preview_image_url
    
    @preview_image_url.setter
    def preview_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the previewImageUrl property value. A URL leading to the preview image for the item.
        Args:
            value: Value to set for the previewImageUrl property.
        """
        self._preview_image_url = value
    
    @property
    def preview_text(self,) -> Optional[str]:
        """
        Gets the previewText property value. A preview text for the item.
        Returns: Optional[str]
        """
        return self._preview_text
    
    @preview_text.setter
    def preview_text(self,value: Optional[str] = None) -> None:
        """
        Sets the previewText property value. A preview text for the item.
        Args:
            value: Value to set for the previewText property.
        """
        self._preview_text = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("containerDisplayName", self.container_display_name)
        writer.write_str_value("containerType", self.container_type)
        writer.write_str_value("containerWebUrl", self.container_web_url)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previewImageUrl", self.preview_image_url)
        writer.write_str_value("previewText", self.preview_text)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The item's title text.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The item's title text.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The item's media type. Can be used for filtering for a specific file based on a specific type. See below for supported types.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The item's media type. Can be used for filtering for a specific file based on a specific type. See below for supported types.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

