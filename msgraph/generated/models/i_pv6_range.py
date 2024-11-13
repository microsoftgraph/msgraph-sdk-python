from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ip_range import IpRange

from .ip_range import IpRange

@dataclass
class IPv6Range(IpRange, Parsable):
    """
    IPv6 Range definition.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iPv6Range"
    # Lower address.
    lower_address: Optional[str] = None
    # Upper address.
    upper_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IPv6Range:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IPv6Range
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IPv6Range()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ip_range import IpRange

        from .ip_range import IpRange

        fields: Dict[str, Callable[[Any], None]] = {
            "lowerAddress": lambda n : setattr(self, 'lower_address', n.get_str_value()),
            "upperAddress": lambda n : setattr(self, 'upper_address', n.get_str_value()),
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
        from .ip_range import IpRange

        writer.write_str_value("lowerAddress", self.lower_address)
        writer.write_str_value("upperAddress", self.upper_address)
    

