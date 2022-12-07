from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RgbColor(AdditionalDataHolder, Parsable):
    """
    Color in RGB.
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
    
    @property
    def b(self,) -> Optional[int]:
        """
        Gets the b property value. Blue value
        Returns: Optional[int]
        """
        return self._b
    
    @b.setter
    def b(self,value: Optional[int] = None) -> None:
        """
        Sets the b property value. Blue value
        Args:
            value: Value to set for the b property.
        """
        self._b = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new rgbColor and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Blue value
        self._b: Optional[int] = None
        # Green value
        self._g: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Red value
        self._r: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RgbColor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RgbColor
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RgbColor()
    
    @property
    def g(self,) -> Optional[int]:
        """
        Gets the g property value. Green value
        Returns: Optional[int]
        """
        return self._g
    
    @g.setter
    def g(self,value: Optional[int] = None) -> None:
        """
        Sets the g property value. Green value
        Args:
            value: Value to set for the g property.
        """
        self._g = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "b": lambda n : setattr(self, 'b', n.get_int_value()),
            "g": lambda n : setattr(self, 'g', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "r": lambda n : setattr(self, 'r', n.get_int_value()),
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
    def r(self,) -> Optional[int]:
        """
        Gets the r property value. Red value
        Returns: Optional[int]
        """
        return self._r
    
    @r.setter
    def r(self,value: Optional[int] = None) -> None:
        """
        Sets the r property value. Red value
        Args:
            value: Value to set for the r property.
        """
        self._r = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("b", self.b)
        writer.write_int_value("g", self.g)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("r", self.r)
        writer.write_additional_data_value(self.additional_data)
    

