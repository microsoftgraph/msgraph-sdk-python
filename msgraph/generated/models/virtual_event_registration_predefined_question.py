from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .virtual_event_registration_predefined_question_label import VirtualEventRegistrationPredefinedQuestionLabel
    from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

@dataclass
class VirtualEventRegistrationPredefinedQuestion(VirtualEventRegistrationQuestionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventRegistrationPredefinedQuestion"
    # Label of the predefined registration question. It accepts a single line of text: street, city, state, postalCode, countryOrRegion, industry, jobTitle, organization, and unknownFutureValue.
    label: Optional[VirtualEventRegistrationPredefinedQuestionLabel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventRegistrationPredefinedQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationPredefinedQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistrationPredefinedQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .virtual_event_registration_predefined_question_label import VirtualEventRegistrationPredefinedQuestionLabel
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

        from .virtual_event_registration_predefined_question_label import VirtualEventRegistrationPredefinedQuestionLabel
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

        fields: dict[str, Callable[[Any], None]] = {
            "label": lambda n : setattr(self, 'label', n.get_enum_value(VirtualEventRegistrationPredefinedQuestionLabel)),
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
        writer.write_enum_value("label", self.label)
    

