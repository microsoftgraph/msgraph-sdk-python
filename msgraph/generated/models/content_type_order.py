from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ContentTypeOrder(AdditionalDataHolder, Parsable):
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
        Instantiates a new contentTypeOrder and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether this is the default Content Type
        self._default: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the position in which the Content Type appears in the selection UI.
        self._position: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentTypeOrder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentTypeOrder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentTypeOrder()
    
    @property
    def default(self,) -> Optional[bool]:
        """
        Gets the default property value. Whether this is the default Content Type
        Returns: Optional[bool]
        """
        return self._default
    
    @default.setter
    def default(self,value: Optional[bool] = None) -> None:
        """
        Sets the default property value. Whether this is the default Content Type
        Args:
            value: Value to set for the default property.
        """
        self._default = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default": lambda n : setattr(self, 'default', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
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
    
    @property
    def position(self,) -> Optional[int]:
        """
        Gets the position property value. Specifies the position in which the Content Type appears in the selection UI.
        Returns: Optional[int]
        """
        return self._position
    
    @position.setter
    def position(self,value: Optional[int] = None) -> None:
        """
        Sets the position property value. Specifies the position in which the Content Type appears in the selection UI.
        Args:
            value: Value to set for the position property.
        """
        self._position = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("default", self.default)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("position", self.position)
        writer.write_additional_data_value(self.additional_data)
    

