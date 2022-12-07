from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

standard_time_zone_offset = lazy_import('msgraph.generated.models.standard_time_zone_offset')

class DaylightTimeZoneOffset(standard_time_zone_offset.StandardTimeZoneOffset):
    def __init__(self,) -> None:
        """
        Instantiates a new DaylightTimeZoneOffset and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.daylightTimeZoneOffset"
        # The time offset from Coordinated Universal Time (UTC) for daylight saving time. This value is in minutes.
        self._daylight_bias: Optional[int] = None
    
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
    
    @property
    def daylight_bias(self,) -> Optional[int]:
        """
        Gets the daylightBias property value. The time offset from Coordinated Universal Time (UTC) for daylight saving time. This value is in minutes.
        Returns: Optional[int]
        """
        return self._daylight_bias
    
    @daylight_bias.setter
    def daylight_bias(self,value: Optional[int] = None) -> None:
        """
        Sets the daylightBias property value. The time offset from Coordinated Universal Time (UTC) for daylight saving time. This value is in minutes.
        Args:
            value: Value to set for the daylightBias property.
        """
        self._daylight_bias = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "daylight_bias": lambda n : setattr(self, 'daylight_bias', n.get_int_value()),
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
    

