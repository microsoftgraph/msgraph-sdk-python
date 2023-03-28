from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AddFormulaLocalPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new addFormulaLocalPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The comment property
        self._comment: Optional[str] = None
        # The formula property
        self._formula: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
    
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
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment property
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment property
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddFormulaLocalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddFormulaLocalPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddFormulaLocalPostRequestBody()
    
    @property
    def formula(self,) -> Optional[str]:
        """
        Gets the formula property value. The formula property
        Returns: Optional[str]
        """
        return self._formula
    
    @formula.setter
    def formula(self,value: Optional[str] = None) -> None:
        """
        Sets the formula property value. The formula property
        Args:
            value: Value to set for the formula property.
        """
        self._formula = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

