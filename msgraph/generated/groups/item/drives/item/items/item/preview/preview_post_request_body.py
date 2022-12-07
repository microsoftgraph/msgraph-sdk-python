from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PreviewPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the preview method.
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
        Instantiates a new previewPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The page property
        self._page: Optional[str] = None
        # The zoom property
        self._zoom: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PreviewPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PreviewPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PreviewPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "page": lambda n : setattr(self, 'page', n.get_str_value()),
            "zoom": lambda n : setattr(self, 'zoom', n.get_float_value()),
        }
        return fields
    
    @property
    def page(self,) -> Optional[str]:
        """
        Gets the page property value. The page property
        Returns: Optional[str]
        """
        return self._page
    
    @page.setter
    def page(self,value: Optional[str] = None) -> None:
        """
        Sets the page property value. The page property
        Args:
            value: Value to set for the page property.
        """
        self._page = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("page", self.page)
        writer.write_float_value("zoom", self.zoom)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def zoom(self,) -> Optional[float]:
        """
        Gets the zoom property value. The zoom property
        Returns: Optional[float]
        """
        return self._zoom
    
    @zoom.setter
    def zoom(self,value: Optional[float] = None) -> None:
        """
        Sets the zoom property value. The zoom property
        Args:
            value: Value to set for the zoom property.
        """
        self._zoom = value
    

