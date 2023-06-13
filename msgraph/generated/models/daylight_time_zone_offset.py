from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import standard_time_zone_offset

from . import standard_time_zone_offset

@dataclass
class DaylightTimeZoneOffset(standard_time_zone_offset.StandardTimeZoneOffset):
    odata_type = "#microsoft.graph.daylightTimeZoneOffset"
    # The time offset from Coordinated Universal Time (UTC) for daylight saving time. This value is in minutes.
    daylight_bias: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DaylightTimeZoneOffset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DaylightTimeZoneOffset
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DaylightTimeZoneOffset()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import standard_time_zone_offset

        fields: Dict[str, Callable[[Any], None]] = {
            "daylightBias": lambda n : setattr(self, 'daylight_bias', n.get_int_value()),
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
        writer.write_int_value("daylightBias", self.daylight_bias)
    

