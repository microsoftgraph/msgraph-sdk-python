from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .answer_input_type import AnswerInputType

@dataclass
class BookingQuestionAnswer(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The answer given by the user in case the answerInputType is text.
    answer: Optional[str] = None
    # The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
    answer_input_type: Optional[AnswerInputType] = None
    # In case the answerInputType is radioButton, this will consists of a list of possible answer values.
    answer_options: Optional[list[str]] = None
    # Indicates whether it is mandatory to answer the custom question.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The question.
    question: Optional[str] = None
    # The ID of the custom question.
    question_id: Optional[str] = None
    # The answers selected by the user.
    selected_options: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingQuestionAnswer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingQuestionAnswer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingQuestionAnswer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .answer_input_type import AnswerInputType

        from .answer_input_type import AnswerInputType

        fields: dict[str, Callable[[Any], None]] = {
            "answer": lambda n : setattr(self, 'answer', n.get_str_value()),
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(AnswerInputType)),
            "answerOptions": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "question": lambda n : setattr(self, 'question', n.get_str_value()),
            "questionId": lambda n : setattr(self, 'question_id', n.get_str_value()),
            "selectedOptions": lambda n : setattr(self, 'selected_options', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("answer", self.answer)
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("question", self.question)
        writer.write_str_value("questionId", self.question_id)
        writer.write_collection_of_primitive_values("selectedOptions", self.selected_options)
        writer.write_additional_data_value(self.additional_data)
    

