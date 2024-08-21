from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .ip_evidence import IpEvidence
    from .protocol_type import ProtocolType

from .alert_evidence import AlertEvidence

@dataclass
class NetworkConnectionEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.networkConnectionEvidence"
    # The destinationAddress property
    destination_address: Optional[IpEvidence] = None
    # The destinationPort property
    destination_port: Optional[int] = None
    # The protocol property
    protocol: Optional[ProtocolType] = None
    # The sourceAddress property
    source_address: Optional[IpEvidence] = None
    # The sourcePort property
    source_port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkConnectionEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkConnectionEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkConnectionEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence
        from .protocol_type import ProtocolType

        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence
        from .protocol_type import ProtocolType

        fields: Dict[str, Callable[[Any], None]] = {
            "destinationAddress": lambda n : setattr(self, 'destination_address', n.get_object_value(IpEvidence)),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(ProtocolType)),
            "sourceAddress": lambda n : setattr(self, 'source_address', n.get_object_value(IpEvidence)),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_int_value()),
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
        writer.write_object_value("destinationAddress", self.destination_address)
        writer.write_int_value("destinationPort", self.destination_port)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_object_value("sourceAddress", self.source_address)
        writer.write_int_value("sourcePort", self.source_port)
    

