from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .answer_input_type import AnswerInputType
    from .entity import Entity

from .entity import Entity

@dataclass
class BookingCustomQuestion(Entity, Parsable):
    """
    Represents a custom question of the business.
    """
    # The expected answer type. The possible values are: text, radioButton, unknownFutureValue.
    answer_input_type: Optional[AnswerInputType] = None
    # List of possible answer values.
    answer_options: Optional[list[str]] = None
    # The date, time, and time zone when the custom question was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The question.
    display_name: Optional[str] = None
    # The date, time, and time zone when the custom question was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingCustomQuestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomQuestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingCustomQuestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .answer_input_type import AnswerInputType
        from .entity import Entity

        from .answer_input_type import AnswerInputType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "answerInputType": lambda n : setattr(self, 'answer_input_type', n.get_enum_value(AnswerInputType)),
            "answerOptions": lambda n : setattr(self, 'answer_options', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
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
        writer.write_enum_value("answerInputType", self.answer_input_type)
        writer.write_collection_of_primitive_values("answerOptions", self.answer_options)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
    

