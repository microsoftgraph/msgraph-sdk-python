from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .retention_duration import RetentionDuration

from .retention_duration import RetentionDuration

@dataclass
class RetentionDurationInDays(RetentionDuration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.retentionDurationInDays"
    # Specifies the time period in days for which an item with the applied retention label will be retained for.
    days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionDurationInDays:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionDurationInDays
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionDurationInDays()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .retention_duration import RetentionDuration

        from .retention_duration import RetentionDuration

        fields: Dict[str, Callable[[Any], None]] = {
            "days": lambda n : setattr(self, 'days', n.get_int_value()),
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
        writer.write_int_value("days", self.days)
    

