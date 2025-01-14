from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .external_activity_result import ExternalActivityResult
    from .external_activity_type import ExternalActivityType
    from .identity import Identity

from ..entity import Entity

@dataclass
class ExternalActivity(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents an identity used to identify who is responsible for the activity.
    performed_by: Optional[Identity] = None
    # The date and time when the particular activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The type property
    type: Optional[ExternalActivityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivityResult".casefold():
            from .external_activity_result import ExternalActivityResult

            return ExternalActivityResult()
        return ExternalActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .external_activity_result import ExternalActivityResult
        from .external_activity_type import ExternalActivityType
        from .identity import Identity

        from ..entity import Entity
        from .external_activity_result import ExternalActivityResult
        from .external_activity_type import ExternalActivityType
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "performedBy": lambda n : setattr(self, 'performed_by', n.get_object_value(Identity)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ExternalActivityType)),
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
        writer.write_object_value("performedBy", self.performed_by)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
    

