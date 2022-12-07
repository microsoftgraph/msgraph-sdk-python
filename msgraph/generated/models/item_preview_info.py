from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ItemPreviewInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new itemPreviewInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The getUrl property
        self._get_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The postParameters property
        self._post_parameters: Optional[str] = None
        # The postUrl property
        self._post_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemPreviewInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemPreviewInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemPreviewInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "get_url": lambda n : setattr(self, 'get_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "post_parameters": lambda n : setattr(self, 'post_parameters', n.get_str_value()),
            "post_url": lambda n : setattr(self, 'post_url', n.get_str_value()),
        }
        return fields
    
    @property
    def get_url(self,) -> Optional[str]:
        """
        Gets the getUrl property value. The getUrl property
        Returns: Optional[str]
        """
        return self._get_url
    
    @get_url.setter
    def get_url(self,value: Optional[str] = None) -> None:
        """
        Sets the getUrl property value. The getUrl property
        Args:
            value: Value to set for the getUrl property.
        """
        self._get_url = value
    
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
    def post_parameters(self,) -> Optional[str]:
        """
        Gets the postParameters property value. The postParameters property
        Returns: Optional[str]
        """
        return self._post_parameters
    
    @post_parameters.setter
    def post_parameters(self,value: Optional[str] = None) -> None:
        """
        Sets the postParameters property value. The postParameters property
        Args:
            value: Value to set for the postParameters property.
        """
        self._post_parameters = value
    
    @property
    def post_url(self,) -> Optional[str]:
        """
        Gets the postUrl property value. The postUrl property
        Returns: Optional[str]
        """
        return self._post_url
    
    @post_url.setter
    def post_url(self,value: Optional[str] = None) -> None:
        """
        Sets the postUrl property value. The postUrl property
        Args:
            value: Value to set for the postUrl property.
        """
        self._post_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("getUrl", self.get_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("postParameters", self.post_parameters)
        writer.write_str_value("postUrl", self.post_url)
        writer.write_additional_data_value(self.additional_data)
    

