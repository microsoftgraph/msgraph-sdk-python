from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping_source, public_error

class ParseExpressionResponse(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new parseExpressionResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The error property
        self._error: Optional[public_error.PublicError] = None
        # The evaluationResult property
        self._evaluation_result: Optional[List[str]] = None
        # The evaluationSucceeded property
        self._evaluation_succeeded: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The parsedExpression property
        self._parsed_expression: Optional[attribute_mapping_source.AttributeMappingSource] = None
        # The parsingSucceeded property
        self._parsing_succeeded: Optional[bool] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParseExpressionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParseExpressionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParseExpressionResponse()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. The error property
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    @property
    def evaluation_result(self,) -> Optional[List[str]]:
        """
        Gets the evaluationResult property value. The evaluationResult property
        Returns: Optional[List[str]]
        """
        return self._evaluation_result
    
    @evaluation_result.setter
    def evaluation_result(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the evaluationResult property value. The evaluationResult property
        Args:
            value: Value to set for the evaluation_result property.
        """
        self._evaluation_result = value
    
    @property
    def evaluation_succeeded(self,) -> Optional[bool]:
        """
        Gets the evaluationSucceeded property value. The evaluationSucceeded property
        Returns: Optional[bool]
        """
        return self._evaluation_succeeded
    
    @evaluation_succeeded.setter
    def evaluation_succeeded(self,value: Optional[bool] = None) -> None:
        """
        Sets the evaluationSucceeded property value. The evaluationSucceeded property
        Args:
            value: Value to set for the evaluation_succeeded property.
        """
        self._evaluation_succeeded = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping_source, public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "evaluationResult": lambda n : setattr(self, 'evaluation_result', n.get_collection_of_primitive_values(str)),
            "evaluationSucceeded": lambda n : setattr(self, 'evaluation_succeeded', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parsedExpression": lambda n : setattr(self, 'parsed_expression', n.get_object_value(attribute_mapping_source.AttributeMappingSource)),
            "parsingSucceeded": lambda n : setattr(self, 'parsing_succeeded', n.get_bool_value()),
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
    def parsed_expression(self,) -> Optional[attribute_mapping_source.AttributeMappingSource]:
        """
        Gets the parsedExpression property value. The parsedExpression property
        Returns: Optional[attribute_mapping_source.AttributeMappingSource]
        """
        return self._parsed_expression
    
    @parsed_expression.setter
    def parsed_expression(self,value: Optional[attribute_mapping_source.AttributeMappingSource] = None) -> None:
        """
        Sets the parsedExpression property value. The parsedExpression property
        Args:
            value: Value to set for the parsed_expression property.
        """
        self._parsed_expression = value
    
    @property
    def parsing_succeeded(self,) -> Optional[bool]:
        """
        Gets the parsingSucceeded property value. The parsingSucceeded property
        Returns: Optional[bool]
        """
        return self._parsing_succeeded
    
    @parsing_succeeded.setter
    def parsing_succeeded(self,value: Optional[bool] = None) -> None:
        """
        Sets the parsingSucceeded property value. The parsingSucceeded property
        Args:
            value: Value to set for the parsing_succeeded property.
        """
        self._parsing_succeeded = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("error", self.error)
        writer.write_collection_of_primitive_values("evaluationResult", self.evaluation_result)
        writer.write_bool_value("evaluationSucceeded", self.evaluation_succeeded)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parsedExpression", self.parsed_expression)
        writer.write_bool_value("parsingSucceeded", self.parsing_succeeded)
        writer.write_additional_data_value(self.additional_data)
    

