from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType
    from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

@dataclass
class VirtualEventRegistrationCustomQuestion(VirtualEventRegistrationQuestionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventRegistrationCustomQuestion"
    # Answer choices when answerInputType is singleChoice or multiChoice.
    answer_choices: Optional[list[str]] = None
    # Input type of the registration question answer. Possible values are text, multilineText, singleChoice, multiChoice, boolean, and unknownFutureValue.
    answer_input_type: Optional[VirtualEventRegistrationQuestionAnswerInputType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventRegistrationCustomQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationCustomQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistrationCustomQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

        from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

        fields: dict[str, Callable[[Any], None]] = {
            "answerChoices": lambda n : setattr(self, 'answer_choices', n.get_collection_of_primitive_values(str)),
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(VirtualEventRegistrationQuestionAnswerInputType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("answerChoices", self.answer_choices)
        writer.write_enum_value("answerInputType", self.answer_input_type)
    

