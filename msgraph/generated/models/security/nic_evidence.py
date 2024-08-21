from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .ip_evidence import IpEvidence

from .alert_evidence import AlertEvidence

@dataclass
class NicEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.nicEvidence"
    # The ipAddress property
    ip_address: Optional[IpEvidence] = None
    # The macAddress property
    mac_address: Optional[str] = None
    # The vlans property
    vlans: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NicEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NicEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NicEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence

        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_object_value(IpEvidence)),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "vlans": lambda n : setattr(self, 'vlans', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("ipAddress", self.ip_address)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_collection_of_primitive_values("vlans", self.vlans)
    

