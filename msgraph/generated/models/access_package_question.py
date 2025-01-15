from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_localized_text import AccessPackageLocalizedText
    from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
    from .access_package_text_input_question import AccessPackageTextInputQuestion
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageQuestion(Entity, Parsable):
    # Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
    is_answer_editable: Optional[bool] = None
    # Whether the requestor is required to supply an answer or not.
    is_required: Optional[bool] = None
    # The text of the question represented in a format for a specific locale.
    localizations: Optional[list[AccessPackageLocalizedText]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Relative position of this question when displaying a list of questions to the requestor.
    sequence: Optional[int] = None
    # The text of the question to show to the requestor.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageMultipleChoiceQuestion".casefold():
            from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion

            return AccessPackageMultipleChoiceQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageTextInputQuestion".casefold():
            from .access_package_text_input_question import AccessPackageTextInputQuestion

            return AccessPackageTextInputQuestion()
        return AccessPackageQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_localized_text import AccessPackageLocalizedText
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_text_input_question import AccessPackageTextInputQuestion
        from .entity import Entity

        from .access_package_localized_text import AccessPackageLocalizedText
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_text_input_question import AccessPackageTextInputQuestion
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "isAnswerEditable": lambda n : setattr(self, 'is_answer_editable', n.get_bool_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(AccessPackageLocalizedText)),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_bool_value("isAnswerEditable", self.is_answer_editable)
        writer.write_bool_value("isRequired", self.is_required)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_int_value("sequence", self.sequence)
        writer.write_str_value("text", self.text)
    

