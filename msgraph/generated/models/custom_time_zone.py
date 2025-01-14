from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daylight_time_zone_offset import DaylightTimeZoneOffset
    from .standard_time_zone_offset import StandardTimeZoneOffset
    from .time_zone_base import TimeZoneBase

from .time_zone_base import TimeZoneBase

@dataclass
class CustomTimeZone(TimeZoneBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customTimeZone"
    # The time offset of the time zone from Coordinated Universal Time (UTC). This value is in minutes. Time zones that are ahead of UTC have a positive offset; time zones that are behind UTC have a negative offset.
    bias: Optional[int] = None
    # Specifies when the time zone switches from standard time to daylight saving time.
    daylight_offset: Optional[DaylightTimeZoneOffset] = None
    # Specifies when the time zone switches from daylight saving time to standard time.
    standard_offset: Optional[StandardTimeZoneOffset] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomTimeZone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTimeZone
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomTimeZone()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .standard_time_zone_offset import StandardTimeZoneOffset
        from .time_zone_base import TimeZoneBase

        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .standard_time_zone_offset import StandardTimeZoneOffset
        from .time_zone_base import TimeZoneBase

        fields: dict[str, Callable[[Any], None]] = {
            "bias": lambda n : setattr(self, 'bias', n.get_int_value()),
            "daylightOffset": lambda n : setattr(self, 'daylight_offset', n.get_object_value(DaylightTimeZoneOffset)),
            "standardOffset": lambda n : setattr(self, 'standard_offset', n.get_object_value(StandardTimeZoneOffset)),
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
        writer.write_int_value("bias", self.bias)
        writer.write_object_value("daylightOffset", self.daylight_offset)
        writer.write_object_value("standardOffset", self.standard_offset)
    

