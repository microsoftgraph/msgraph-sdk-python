from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import attribute_definition, expression_input_object

class ParseExpressionPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new parseExpressionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expression property
        self._expression: Optional[str] = None
        # The targetAttributeDefinition property
        self._target_attribute_definition: Optional[attribute_definition.AttributeDefinition] = None
        # The testInputObject property
        self._test_input_object: Optional[expression_input_object.ExpressionInputObject] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParseExpressionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParseExpressionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParseExpressionPostRequestBody()
    
    @property
    def expression(self,) -> Optional[str]:
        """
        Gets the expression property value. The expression property
        Returns: Optional[str]
        """
        return self._expression
    
    @expression.setter
    def expression(self,value: Optional[str] = None) -> None:
        """
        Sets the expression property value. The expression property
        Args:
            value: Value to set for the expression property.
        """
        self._expression = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import attribute_definition, expression_input_object

        fields: Dict[str, Callable[[Any], None]] = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "targetAttributeDefinition": lambda n : setattr(self, 'target_attribute_definition', n.get_object_value(attribute_definition.AttributeDefinition)),
            "testInputObject": lambda n : setattr(self, 'test_input_object', n.get_object_value(expression_input_object.ExpressionInputObject)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("expression", self.expression)
        writer.write_object_value("targetAttributeDefinition", self.target_attribute_definition)
        writer.write_object_value("testInputObject", self.test_input_object)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target_attribute_definition(self,) -> Optional[attribute_definition.AttributeDefinition]:
        """
        Gets the targetAttributeDefinition property value. The targetAttributeDefinition property
        Returns: Optional[attribute_definition.AttributeDefinition]
        """
        return self._target_attribute_definition
    
    @target_attribute_definition.setter
    def target_attribute_definition(self,value: Optional[attribute_definition.AttributeDefinition] = None) -> None:
        """
        Sets the targetAttributeDefinition property value. The targetAttributeDefinition property
        Args:
            value: Value to set for the target_attribute_definition property.
        """
        self._target_attribute_definition = value
    
    @property
    def test_input_object(self,) -> Optional[expression_input_object.ExpressionInputObject]:
        """
        Gets the testInputObject property value. The testInputObject property
        Returns: Optional[expression_input_object.ExpressionInputObject]
        """
        return self._test_input_object
    
    @test_input_object.setter
    def test_input_object(self,value: Optional[expression_input_object.ExpressionInputObject] = None) -> None:
        """
        Sets the testInputObject property value. The testInputObject property
        Args:
            value: Value to set for the test_input_object property.
        """
        self._test_input_object = value
    

