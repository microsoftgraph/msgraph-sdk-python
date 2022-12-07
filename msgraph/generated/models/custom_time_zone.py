from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

daylight_time_zone_offset = lazy_import('msgraph.generated.models.daylight_time_zone_offset')
standard_time_zone_offset = lazy_import('msgraph.generated.models.standard_time_zone_offset')
time_zone_base = lazy_import('msgraph.generated.models.time_zone_base')

class CustomTimeZone(time_zone_base.TimeZoneBase):
    @property
    def bias(self,) -> Optional[int]:
        """
        Gets the bias property value. The time offset of the time zone from Coordinated Universal Time (UTC). This value is in minutes. Time zones that are ahead of UTC have a positive offset; time zones that are behind UTC have a negative offset.
        Returns: Optional[int]
        """
        return self._bias
    
    @bias.setter
    def bias(self,value: Optional[int] = None) -> None:
        """
        Sets the bias property value. The time offset of the time zone from Coordinated Universal Time (UTC). This value is in minutes. Time zones that are ahead of UTC have a positive offset; time zones that are behind UTC have a negative offset.
        Args:
            value: Value to set for the bias property.
        """
        self._bias = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CustomTimeZone and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.customTimeZone"
        # The time offset of the time zone from Coordinated Universal Time (UTC). This value is in minutes. Time zones that are ahead of UTC have a positive offset; time zones that are behind UTC have a negative offset.
        self._bias: Optional[int] = None
        # Specifies when the time zone switches from standard time to daylight saving time.
        self._daylight_offset: Optional[daylight_time_zone_offset.DaylightTimeZoneOffset] = None
        # Specifies when the time zone switches from daylight saving time to standard time.
        self._standard_offset: Optional[standard_time_zone_offset.StandardTimeZoneOffset] = None
    
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
    
    @property
    def daylight_offset(self,) -> Optional[daylight_time_zone_offset.DaylightTimeZoneOffset]:
        """
        Gets the daylightOffset property value. Specifies when the time zone switches from standard time to daylight saving time.
        Returns: Optional[daylight_time_zone_offset.DaylightTimeZoneOffset]
        """
        return self._daylight_offset
    
    @daylight_offset.setter
    def daylight_offset(self,value: Optional[daylight_time_zone_offset.DaylightTimeZoneOffset] = None) -> None:
        """
        Sets the daylightOffset property value. Specifies when the time zone switches from standard time to daylight saving time.
        Args:
            value: Value to set for the daylightOffset property.
        """
        self._daylight_offset = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bias": lambda n : setattr(self, 'bias', n.get_int_value()),
            "daylight_offset": lambda n : setattr(self, 'daylight_offset', n.get_object_value(daylight_time_zone_offset.DaylightTimeZoneOffset)),
            "standard_offset": lambda n : setattr(self, 'standard_offset', n.get_object_value(standard_time_zone_offset.StandardTimeZoneOffset)),
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
    
    @property
    def standard_offset(self,) -> Optional[standard_time_zone_offset.StandardTimeZoneOffset]:
        """
        Gets the standardOffset property value. Specifies when the time zone switches from daylight saving time to standard time.
        Returns: Optional[standard_time_zone_offset.StandardTimeZoneOffset]
        """
        return self._standard_offset
    
    @standard_offset.setter
    def standard_offset(self,value: Optional[standard_time_zone_offset.StandardTimeZoneOffset] = None) -> None:
        """
        Sets the standardOffset property value. Specifies when the time zone switches from daylight saving time to standard time.
        Args:
            value: Value to set for the standardOffset property.
        """
        self._standard_offset = value
    

