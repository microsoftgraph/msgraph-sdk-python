from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping_source, public_error

@dataclass
class ParseExpressionResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The error property
    error: Optional[public_error.PublicError] = None
    # The evaluationResult property
    evaluation_result: Optional[List[str]] = None
    # The evaluationSucceeded property
    evaluation_succeeded: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parsedExpression property
    parsed_expression: Optional[attribute_mapping_source.AttributeMappingSource] = None
    # The parsingSucceeded property
    parsing_succeeded: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParseExpressionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParseExpressionResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ParseExpressionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping_source, public_error

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("error", self.error)
        writer.write_collection_of_primitive_values("evaluationResult", self.evaluation_result)
        writer.write_bool_value("evaluationSucceeded", self.evaluation_succeeded)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parsedExpression", self.parsed_expression)
        writer.write_bool_value("parsingSucceeded", self.parsing_succeeded)
        writer.write_additional_data_value(self.additional_data)
    

