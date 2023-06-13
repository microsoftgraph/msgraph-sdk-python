from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_answer_choice, access_package_question

from . import access_package_question

@dataclass
class AccessPackageMultipleChoiceQuestion(access_package_question.AccessPackageQuestion):
    odata_type = "#microsoft.graph.accessPackageMultipleChoiceQuestion"
    # List of answer choices.
    choices: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None
    # Indicates whether requestor can select multiple choices as their answer.
    is_multiple_selection_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageMultipleChoiceQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageMultipleChoiceQuestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageMultipleChoiceQuestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_answer_choice, access_package_question

        fields: Dict[str, Callable[[Any], None]] = {
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_object_values(access_package_answer_choice.AccessPackageAnswerChoice)),
            "isMultipleSelectionAllowed": lambda n : setattr(self, 'is_multiple_selection_allowed', n.get_bool_value()),
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
        writer.write_collection_of_object_values("choices", self.choices)
        writer.write_bool_value("isMultipleSelectionAllowed", self.is_multiple_selection_allowed)
    

