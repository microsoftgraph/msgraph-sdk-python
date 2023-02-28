from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_answer_choice = lazy_import('msgraph.generated.models.access_package_answer_choice')
access_package_question = lazy_import('msgraph.generated.models.access_package_question')

class AccessPackageMultipleChoiceQuestion(access_package_question.AccessPackageQuestion):
    @property
    def choices(self,) -> Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]]:
        """
        Gets the choices property value. List of answer choices.
        Returns: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]]
        """
        return self._choices
    
    @choices.setter
    def choices(self,value: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None) -> None:
        """
        Sets the choices property value. List of answer choices.
        Args:
            value: Value to set for the choices property.
        """
        self._choices = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageMultipleChoiceQuestion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageMultipleChoiceQuestion"
        # List of answer choices.
        self._choices: Optional[List[access_package_answer_choice.AccessPackageAnswerChoice]] = None
        # Indicates whether requestor can select multiple choices as their answer.
        self._is_multiple_selection_allowed: Optional[bool] = None
    
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
        fields = {
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_object_values(access_package_answer_choice.AccessPackageAnswerChoice)),
            "isMultipleSelectionAllowed": lambda n : setattr(self, 'is_multiple_selection_allowed', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_multiple_selection_allowed(self,) -> Optional[bool]:
        """
        Gets the isMultipleSelectionAllowed property value. Indicates whether requestor can select multiple choices as their answer.
        Returns: Optional[bool]
        """
        return self._is_multiple_selection_allowed
    
    @is_multiple_selection_allowed.setter
    def is_multiple_selection_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMultipleSelectionAllowed property value. Indicates whether requestor can select multiple choices as their answer.
        Args:
            value: Value to set for the is_multiple_selection_allowed property.
        """
        self._is_multiple_selection_allowed = value
    
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
    

