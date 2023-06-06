from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence

from . import alert_evidence

@dataclass
class IpEvidence(alert_evidence.AlertEvidence):
    # The two-letter country code according to ISO 3166 format, for example: US, UK, CA, etc..).
    country_letter_code: Optional[str] = None
    # The value of the IP Address, can be either in V4 address or V6 address format.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence

        fields: Dict[str, Callable[[Any], None]] = {
            "countryLetterCode": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
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
        writer.write_str_value("countryLetterCode", self.country_letter_code)
        writer.write_str_value("ipAddress", self.ip_address)
    

