from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ApplyCustomFilterPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new applyCustomFilterPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The criteria1 property
        self._criteria1: Optional[str] = None
        # The criteria2 property
        self._criteria2: Optional[str] = None
        # The oper property
        self._oper: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyCustomFilterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplyCustomFilterPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplyCustomFilterPostRequestBody()
    
    @property
    def criteria1(self,) -> Optional[str]:
        """
        Gets the criteria1 property value. The criteria1 property
        Returns: Optional[str]
        """
        return self._criteria1
    
    @criteria1.setter
    def criteria1(self,value: Optional[str] = None) -> None:
        """
        Sets the criteria1 property value. The criteria1 property
        Args:
            value: Value to set for the criteria1 property.
        """
        self._criteria1 = value
    
    @property
    def criteria2(self,) -> Optional[str]:
        """
        Gets the criteria2 property value. The criteria2 property
        Returns: Optional[str]
        """
        return self._criteria2
    
    @criteria2.setter
    def criteria2(self,value: Optional[str] = None) -> None:
        """
        Sets the criteria2 property value. The criteria2 property
        Args:
            value: Value to set for the criteria2 property.
        """
        self._criteria2 = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "criteria1": lambda n : setattr(self, 'criteria1', n.get_str_value()),
            "criteria2": lambda n : setattr(self, 'criteria2', n.get_str_value()),
            "oper": lambda n : setattr(self, 'oper', n.get_str_value()),
        }
        return fields
    
    @property
    def oper(self,) -> Optional[str]:
        """
        Gets the oper property value. The oper property
        Returns: Optional[str]
        """
        return self._oper
    
    @oper.setter
    def oper(self,value: Optional[str] = None) -> None:
        """
        Sets the oper property value. The oper property
        Args:
            value: Value to set for the oper property.
        """
        self._oper = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("criteria1", self.criteria1)
        writer.write_str_value("criteria2", self.criteria2)
        writer.write_str_value("oper", self.oper)
        writer.write_additional_data_value(self.additional_data)
    

