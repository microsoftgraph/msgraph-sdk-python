from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .autonomous_system import AutonomousSystem
    from .host import Host

from .host import Host

@dataclass
class IpAddress(Host):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ipAddress"
    # The details about the autonomous system to which this IP address belongs.
    autonomous_system: Optional[AutonomousSystem] = None
    # The country/region for this IP address.
    country_or_region: Optional[str] = None
    # The hosting company listed for this host.
    hosting_provider: Optional[str] = None
    # The block of IP addresses this IP address belongs to.
    netblock: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .autonomous_system import AutonomousSystem
        from .host import Host

        from .autonomous_system import AutonomousSystem
        from .host import Host

        fields: Dict[str, Callable[[Any], None]] = {
            "autonomousSystem": lambda n : setattr(self, 'autonomous_system', n.get_object_value(AutonomousSystem)),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "hostingProvider": lambda n : setattr(self, 'hosting_provider', n.get_str_value()),
            "netblock": lambda n : setattr(self, 'netblock', n.get_str_value()),
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
        writer.write_object_value("autonomousSystem", self.autonomous_system)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("hostingProvider", self.hosting_provider)
        writer.write_str_value("netblock", self.netblock)
    

