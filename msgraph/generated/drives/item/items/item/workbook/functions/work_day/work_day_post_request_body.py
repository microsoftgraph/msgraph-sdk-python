from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class WorkDayPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The days property
    days: Optional[Json] = None
    # The holidays property
    holidays: Optional[Json] = None
    # The startDate property
    start_date: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkDayPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkDayPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkDayPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "days": lambda n : setattr(self, 'days', n.get_object_value(Json)),
            "holidays": lambda n : setattr(self, 'holidays', n.get_object_value(Json)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_object_value(Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("days", self.days)
        writer.write_object_value("holidays", self.holidays)
        writer.write_object_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    

