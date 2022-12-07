from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

answer_input_type = lazy_import('msgraph.generated.models.answer_input_type')
entity = lazy_import('msgraph.generated.models.entity')

class BookingCustomQuestion(entity.Entity):
    """
    Represents a custom question of the business.
    """
    @property
    def answer_input_type(self,) -> Optional[answer_input_type.AnswerInputType]:
        """
        Gets the answerInputType property value. The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        Returns: Optional[answer_input_type.AnswerInputType]
        """
        return self._answer_input_type
    
    @answer_input_type.setter
    def answer_input_type(self,value: Optional[answer_input_type.AnswerInputType] = None) -> None:
        """
        Sets the answerInputType property value. The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        Args:
            value: Value to set for the answerInputType property.
        """
        self._answer_input_type = value
    
    @property
    def answer_options(self,) -> Optional[List[str]]:
        """
        Gets the answerOptions property value. List of possible answer values.
        Returns: Optional[List[str]]
        """
        return self._answer_options
    
    @answer_options.setter
    def answer_options(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the answerOptions property value. List of possible answer values.
        Args:
            value: Value to set for the answerOptions property.
        """
        self._answer_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingCustomQuestion and sets the default values.
        """
        super().__init__()
        # The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
        self._answer_input_type: Optional[answer_input_type.AnswerInputType] = None
        # List of possible answer values.
        self._answer_options: Optional[List[str]] = None
        # The question.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingCustomQuestion()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The question.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The question.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "answer_input_type": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(answer_input_type.AnswerInputType)),
            "answer_options": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_str_value("displayName", self.display_name)
    

