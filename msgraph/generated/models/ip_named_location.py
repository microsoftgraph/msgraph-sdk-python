from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_range import IpRange
    from .named_location import NamedLocation

from .named_location import NamedLocation

@dataclass
class IpNamedLocation(NamedLocation):
    # List of IP address ranges in IPv4 CIDR format (for example, 1.2.3.4/32) or any allowable IPv6 format from IETF RFC5969. Required.
    ip_ranges: Optional[List[IpRange]] = None
    # true if this location is explicitly trusted. Optional. Default value is false.
    is_trusted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpNamedLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpNamedLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ip_range import IpRange
        from .named_location import NamedLocation

        from .ip_range import IpRange
        from .named_location import NamedLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "ipRanges": lambda n : setattr(self, 'ip_ranges', n.get_collection_of_object_values(IpRange)),
            "isTrusted": lambda n : setattr(self, 'is_trusted', n.get_bool_value()),
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
        writer.write_collection_of_object_values("ipRanges", self.ip_ranges)
        writer.write_bool_value("isTrusted", self.is_trusted)
    

