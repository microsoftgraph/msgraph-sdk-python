from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact import Artifact
    from .host_component import HostComponent
    from .host_cookie import HostCookie
    from .hostname import Hostname
    from .host_reputation import HostReputation
    from .host_tracker import HostTracker
    from .ip_address import IpAddress
    from .passive_dns_record import PassiveDnsRecord

from .artifact import Artifact

@dataclass
class Host(Artifact):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.host"
    # The hostComponents that are associated with this host.
    components: Optional[List[HostComponent]] = None
    # The hostCookies that are associated with this host.
    cookies: Optional[List[HostCookie]] = None
    # The first date and time this host was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The most recent date and time when this host was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # Passive DNS retrieval about this host.
    passive_dns: Optional[List[PassiveDnsRecord]] = None
    # Reverse passive DNS retrieval about this host.
    passive_dns_reverse: Optional[List[PassiveDnsRecord]] = None
    # Represents a calculated reputation of this host.
    reputation: Optional[HostReputation] = None
    # The hostTrackers that are associated with this host.
    trackers: Optional[List[HostTracker]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Host:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Host
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from .hostname import Hostname

            return Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from .ip_address import IpAddress

            return IpAddress()
        return Host()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .artifact import Artifact
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .hostname import Hostname
        from .host_reputation import HostReputation
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord

        from .artifact import Artifact
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .hostname import Hostname
        from .host_reputation import HostReputation
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "components": lambda n : setattr(self, 'components', n.get_collection_of_object_values(HostComponent)),
            "cookies": lambda n : setattr(self, 'cookies', n.get_collection_of_object_values(HostCookie)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "passiveDns": lambda n : setattr(self, 'passive_dns', n.get_collection_of_object_values(PassiveDnsRecord)),
            "passiveDnsReverse": lambda n : setattr(self, 'passive_dns_reverse', n.get_collection_of_object_values(PassiveDnsRecord)),
            "reputation": lambda n : setattr(self, 'reputation', n.get_object_value(HostReputation)),
            "trackers": lambda n : setattr(self, 'trackers', n.get_collection_of_object_values(HostTracker)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("components", self.components)
        writer.write_collection_of_object_values("cookies", self.cookies)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("passiveDns", self.passive_dns)
        writer.write_collection_of_object_values("passiveDnsReverse", self.passive_dns_reverse)
        writer.write_object_value("reputation", self.reputation)
        writer.write_collection_of_object_values("trackers", self.trackers)
    

