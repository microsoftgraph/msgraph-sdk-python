from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import filter_operand

class FilterClause(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new filterClause and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operatorName property
        self._operator_name: Optional[str] = None
        # The sourceOperandName property
        self._source_operand_name: Optional[str] = None
        # The targetOperand property
        self._target_operand: Optional[filter_operand.FilterOperand] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FilterClause
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FilterClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import filter_operand

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatorName": lambda n : setattr(self, 'operator_name', n.get_str_value()),
            "sourceOperandName": lambda n : setattr(self, 'source_operand_name', n.get_str_value()),
            "targetOperand": lambda n : setattr(self, 'target_operand', n.get_object_value(filter_operand.FilterOperand)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def operator_name(self,) -> Optional[str]:
        """
        Gets the operatorName property value. The operatorName property
        Returns: Optional[str]
        """
        return self._operator_name
    
    @operator_name.setter
    def operator_name(self,value: Optional[str] = None) -> None:
        """
        Sets the operatorName property value. The operatorName property
        Args:
            value: Value to set for the operator_name property.
        """
        self._operator_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatorName", self.operator_name)
        writer.write_str_value("sourceOperandName", self.source_operand_name)
        writer.write_object_value("targetOperand", self.target_operand)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_operand_name(self,) -> Optional[str]:
        """
        Gets the sourceOperandName property value. The sourceOperandName property
        Returns: Optional[str]
        """
        return self._source_operand_name
    
    @source_operand_name.setter
    def source_operand_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceOperandName property value. The sourceOperandName property
        Args:
            value: Value to set for the source_operand_name property.
        """
        self._source_operand_name = value
    
    @property
    def target_operand(self,) -> Optional[filter_operand.FilterOperand]:
        """
        Gets the targetOperand property value. The targetOperand property
        Returns: Optional[filter_operand.FilterOperand]
        """
        return self._target_operand
    
    @target_operand.setter
    def target_operand(self,value: Optional[filter_operand.FilterOperand] = None) -> None:
        """
        Sets the targetOperand property value. The targetOperand property
        Args:
            value: Value to set for the target_operand property.
        """
        self._target_operand = value
    

