from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .answer_state import AnswerState
    from .search_answer import SearchAnswer

from .search_answer import SearchAnswer

@dataclass
class Acronym(SearchAnswer, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # What the acronym stands for.
    stands_for: Optional[str] = None
    # The state property
    state: Optional[AnswerState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Acronym:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Acronym
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Acronym()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .answer_state import AnswerState
        from .search_answer import SearchAnswer

        from .answer_state import AnswerState
        from .search_answer import SearchAnswer

        fields: dict[str, Callable[[Any], None]] = {
            "standsFor": lambda n : setattr(self, 'stands_for', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AnswerState)),
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
        writer.write_str_value("standsFor", self.stands_for)
        writer.write_enum_value("state", self.state)
    

