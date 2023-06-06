from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import daylight_time_zone_offset, standard_time_zone_offset, time_zone_base

from . import time_zone_base

@dataclass
class CustomTimeZone(time_zone_base.TimeZoneBase):
    odata_type = "#microsoft.graph.customTimeZone"
    # The time offset of the time zone from Coordinated Universal Time (UTC). This value is in minutes. Time zones that are ahead of UTC have a positive offset; time zones that are behind UTC have a negative offset.
    bias: Optional[int] = None
    # Specifies when the time zone switches from standard time to daylight saving time.
    daylight_offset: Optional[daylight_time_zone_offset.DaylightTimeZoneOffset] = None
    # Specifies when the time zone switches from daylight saving time to standard time.
    standard_offset: Optional[standard_time_zone_offset.StandardTimeZoneOffset] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTimeZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTimeZone
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTimeZone()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import daylight_time_zone_offset, standard_time_zone_offset, time_zone_base

        fields: Dict[str, Callable[[Any], None]] = {
            "bias": lambda n : setattr(self, 'bias', n.get_int_value()),
            "daylightOffset": lambda n : setattr(self, 'daylight_offset', n.get_object_value(daylight_time_zone_offset.DaylightTimeZoneOffset)),
            "standardOffset": lambda n : setattr(self, 'standard_offset', n.get_object_value(standard_time_zone_offset.StandardTimeZoneOffset)),
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
        writer.write_int_value("bias", self.bias)
        writer.write_object_value("daylightOffset", self.daylight_offset)
        writer.write_object_value("standardOffset", self.standard_offset)
    

