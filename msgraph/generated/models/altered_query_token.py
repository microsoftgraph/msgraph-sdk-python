from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AlteredQueryToken(AdditionalDataHolder, Parsable):
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
        Instantiates a new alteredQueryToken and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines the length of a changed segment.
        self._length: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines the offset of a changed segment.
        self._offset: Optional[int] = None
        # Represents the corrected segment string.
        self._suggestion: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlteredQueryToken:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlteredQueryToken
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlteredQueryToken()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "suggestion": lambda n : setattr(self, 'suggestion', n.get_str_value()),
        }
        return fields
    
    @property
    def length(self,) -> Optional[int]:
        """
        Gets the length property value. Defines the length of a changed segment.
        Returns: Optional[int]
        """
        return self._length
    
    @length.setter
    def length(self,value: Optional[int] = None) -> None:
        """
        Sets the length property value. Defines the length of a changed segment.
        Args:
            value: Value to set for the length property.
        """
        self._length = value
    
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
    def offset(self,) -> Optional[int]:
        """
        Gets the offset property value. Defines the offset of a changed segment.
        Returns: Optional[int]
        """
        return self._offset
    
    @offset.setter
    def offset(self,value: Optional[int] = None) -> None:
        """
        Sets the offset property value. Defines the offset of a changed segment.
        Args:
            value: Value to set for the offset property.
        """
        self._offset = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("length", self.length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("offset", self.offset)
        writer.write_str_value("suggestion", self.suggestion)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def suggestion(self,) -> Optional[str]:
        """
        Gets the suggestion property value. Represents the corrected segment string.
        Returns: Optional[str]
        """
        return self._suggestion
    
    @suggestion.setter
    def suggestion(self,value: Optional[str] = None) -> None:
        """
        Sets the suggestion property value. Represents the corrected segment string.
        Args:
            value: Value to set for the suggestion property.
        """
        self._suggestion = value
    

