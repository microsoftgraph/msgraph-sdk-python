from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class NumberColumn(AdditionalDataHolder, Parsable):
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
        Instantiates a new numberColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # How many decimal places to display. See below for information about the possible values.
        self._decimal_places: Optional[str] = None
        # How the value should be presented in the UX. Must be one of number or percentage. If unspecified, treated as number.
        self._display_as: Optional[str] = None
        # The maximum permitted value.
        self._maximum: Optional[float] = None
        # The minimum permitted value.
        self._minimum: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NumberColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NumberColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NumberColumn()
    
    @property
    def decimal_places(self,) -> Optional[str]:
        """
        Gets the decimalPlaces property value. How many decimal places to display. See below for information about the possible values.
        Returns: Optional[str]
        """
        return self._decimal_places
    
    @decimal_places.setter
    def decimal_places(self,value: Optional[str] = None) -> None:
        """
        Sets the decimalPlaces property value. How many decimal places to display. See below for information about the possible values.
        Args:
            value: Value to set for the decimalPlaces property.
        """
        self._decimal_places = value
    
    @property
    def display_as(self,) -> Optional[str]:
        """
        Gets the displayAs property value. How the value should be presented in the UX. Must be one of number or percentage. If unspecified, treated as number.
        Returns: Optional[str]
        """
        return self._display_as
    
    @display_as.setter
    def display_as(self,value: Optional[str] = None) -> None:
        """
        Sets the displayAs property value. How the value should be presented in the UX. Must be one of number or percentage. If unspecified, treated as number.
        Args:
            value: Value to set for the displayAs property.
        """
        self._display_as = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "decimal_places": lambda n : setattr(self, 'decimal_places', n.get_str_value()),
            "display_as": lambda n : setattr(self, 'display_as', n.get_str_value()),
            "maximum": lambda n : setattr(self, 'maximum', n.get_float_value()),
            "minimum": lambda n : setattr(self, 'minimum', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def maximum(self,) -> Optional[float]:
        """
        Gets the maximum property value. The maximum permitted value.
        Returns: Optional[float]
        """
        return self._maximum
    
    @maximum.setter
    def maximum(self,value: Optional[float] = None) -> None:
        """
        Sets the maximum property value. The maximum permitted value.
        Args:
            value: Value to set for the maximum property.
        """
        self._maximum = value
    
    @property
    def minimum(self,) -> Optional[float]:
        """
        Gets the minimum property value. The minimum permitted value.
        Returns: Optional[float]
        """
        return self._minimum
    
    @minimum.setter
    def minimum(self,value: Optional[float] = None) -> None:
        """
        Sets the minimum property value. The minimum permitted value.
        Args:
            value: Value to set for the minimum property.
        """
        self._minimum = value
    
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
        writer.write_str_value("decimalPlaces", self.decimal_places)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_float_value("maximum", self.maximum)
        writer.write_float_value("minimum", self.minimum)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

