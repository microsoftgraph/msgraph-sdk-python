from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
    from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

from .entity import Entity

@dataclass
class VirtualEventRegistrationQuestionBase(Entity):
    # Display name of the registration question.
    display_name: Optional[str] = None
    # Indicates whether an answer to the question is required. The default value is false.
    is_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventRegistrationQuestionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrationQuestionBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationCustomQuestion".casefold():
            from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion

            return VirtualEventRegistrationCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationPredefinedQuestion".casefold():
            from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

            return VirtualEventRegistrationPredefinedQuestion()
        return VirtualEventRegistrationQuestionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

        from .entity import Entity
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isRequired": lambda n : setattr(self, 'is_required', n.get_bool_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isRequired", self.is_required)
    

