from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact import Artifact
    from .hostname import Hostname
    from .host_component import HostComponent
    from .host_cookie import HostCookie
    from .host_pair import HostPair
    from .host_port import HostPort
    from .host_reputation import HostReputation
    from .host_ssl_certificate import HostSslCertificate
    from .host_tracker import HostTracker
    from .ip_address import IpAddress
    from .passive_dns_record import PassiveDnsRecord
    from .subdomain import Subdomain
    from .whois_record import WhoisRecord

from .artifact import Artifact

@dataclass
class Host(Artifact, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.host"
    # The hostPairs that are resources associated with a host, where that host is the parentHost and has an outgoing pairing to a childHost.
    child_host_pairs: Optional[list[HostPair]] = None
    # The hostComponents that are associated with this host.
    components: Optional[list[HostComponent]] = None
    # The hostCookies that are associated with this host.
    cookies: Optional[list[HostCookie]] = None
    # The first date and time when this host was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The hostPairs that are associated with this host, where this host is either the parentHost or childHost.
    host_pairs: Optional[list[HostPair]] = None
    # The most recent date and time when this host was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The hostPairs that are associated with a host, where that host is the childHost and has an incoming pairing with a parentHost.
    parent_host_pairs: Optional[list[HostPair]] = None
    # Passive DNS retrieval about this host.
    passive_dns: Optional[list[PassiveDnsRecord]] = None
    # Reverse passive DNS retrieval about this host.
    passive_dns_reverse: Optional[list[PassiveDnsRecord]] = None
    # The hostPorts associated with a host.
    ports: Optional[list[HostPort]] = None
    # Represents a calculated reputation of this host.
    reputation: Optional[HostReputation] = None
    # The hostSslCertificates that are associated with this host.
    ssl_certificates: Optional[list[HostSslCertificate]] = None
    # The subdomains that are associated with this host.
    subdomains: Optional[list[Subdomain]] = None
    # The hostTrackers that are associated with this host.
    trackers: Optional[list[HostTracker]] = None
    # The most recent whoisRecord for this host.
    whois: Optional[WhoisRecord] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Host:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Host
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from .hostname import Hostname

            return Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from .ip_address import IpAddress

            return IpAddress()
        return Host()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .artifact import Artifact
        from .hostname import Hostname
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_pair import HostPair
        from .host_port import HostPort
        from .host_reputation import HostReputation
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord
        from .subdomain import Subdomain
        from .whois_record import WhoisRecord

        from .artifact import Artifact
        from .hostname import Hostname
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_pair import HostPair
        from .host_port import HostPort
        from .host_reputation import HostReputation
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord
        from .subdomain import Subdomain
        from .whois_record import WhoisRecord

        fields: dict[str, Callable[[Any], None]] = {
            "childHostPairs": lambda n : setattr(self, 'child_host_pairs', n.get_collection_of_object_values(HostPair)),
            "components": lambda n : setattr(self, 'components', n.get_collection_of_object_values(HostComponent)),
            "cookies": lambda n : setattr(self, 'cookies', n.get_collection_of_object_values(HostCookie)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "hostPairs": lambda n : setattr(self, 'host_pairs', n.get_collection_of_object_values(HostPair)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "parentHostPairs": lambda n : setattr(self, 'parent_host_pairs', n.get_collection_of_object_values(HostPair)),
            "passiveDns": lambda n : setattr(self, 'passive_dns', n.get_collection_of_object_values(PassiveDnsRecord)),
            "passiveDnsReverse": lambda n : setattr(self, 'passive_dns_reverse', n.get_collection_of_object_values(PassiveDnsRecord)),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_object_values(HostPort)),
            "reputation": lambda n : setattr(self, 'reputation', n.get_object_value(HostReputation)),
            "sslCertificates": lambda n : setattr(self, 'ssl_certificates', n.get_collection_of_object_values(HostSslCertificate)),
            "subdomains": lambda n : setattr(self, 'subdomains', n.get_collection_of_object_values(Subdomain)),
            "trackers": lambda n : setattr(self, 'trackers', n.get_collection_of_object_values(HostTracker)),
            "whois": lambda n : setattr(self, 'whois', n.get_object_value(WhoisRecord)),
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
        writer.write_collection_of_object_values("childHostPairs", self.child_host_pairs)
        writer.write_collection_of_object_values("components", self.components)
        writer.write_collection_of_object_values("cookies", self.cookies)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_collection_of_object_values("hostPairs", self.host_pairs)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("parentHostPairs", self.parent_host_pairs)
        writer.write_collection_of_object_values("passiveDns", self.passive_dns)
        writer.write_collection_of_object_values("passiveDnsReverse", self.passive_dns_reverse)
        writer.write_collection_of_object_values("ports", self.ports)
        writer.write_object_value("reputation", self.reputation)
        writer.write_collection_of_object_values("sslCertificates", self.ssl_certificates)
        writer.write_collection_of_object_values("subdomains", self.subdomains)
        writer.write_collection_of_object_values("trackers", self.trackers)
        writer.write_object_value("whois", self.whois)
    

