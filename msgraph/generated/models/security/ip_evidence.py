from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .geo_location import GeoLocation
    from .stream import Stream

from .alert_evidence import AlertEvidence

@dataclass
class IpEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ipEvidence"
    # The two-letter country code according to ISO 3166 format, for example: US, UK, CA, etc.
    country_letter_code: Optional[str] = None
    # The value of the IP Address, can be either in V4 address or V6 address format.
    ip_address: Optional[str] = None
    # The location property
    location: Optional[GeoLocation] = None
    # The stream property
    stream: Optional[Stream] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .geo_location import GeoLocation
        from .stream import Stream

        from .alert_evidence import AlertEvidence
        from .geo_location import GeoLocation
        from .stream import Stream

        fields: dict[str, Callable[[Any], None]] = {
            "countryLetterCode": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(GeoLocation)),
            "stream": lambda n : setattr(self, 'stream', n.get_object_value(Stream)),
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
        writer.write_str_value("countryLetterCode", self.country_letter_code)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_object_value("location", self.location)
        writer.write_object_value("stream", self.stream)
    

