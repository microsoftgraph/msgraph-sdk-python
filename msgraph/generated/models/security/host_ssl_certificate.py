from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact import Artifact
    from .host import Host
    from .host_ssl_certificate_port import HostSslCertificatePort
    from .ssl_certificate import SslCertificate

from .artifact import Artifact

@dataclass
class HostSslCertificate(Artifact, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.hostSslCertificate"
    # The first date and time when this hostSslCertificate was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host for this hostSslCertificate.
    host: Optional[Host] = None
    # The most recent date and time when this hostSslCertificate was observed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The ports related with this hostSslCertificate.
    ports: Optional[list[HostSslCertificatePort]] = None
    # The sslCertificate for this hostSslCertificate.
    ssl_certificate: Optional[SslCertificate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostSslCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostSslCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostSslCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .artifact import Artifact
        from .host import Host
        from .host_ssl_certificate_port import HostSslCertificatePort
        from .ssl_certificate import SslCertificate

        from .artifact import Artifact
        from .host import Host
        from .host_ssl_certificate_port import HostSslCertificatePort
        from .ssl_certificate import SslCertificate

        fields: dict[str, Callable[[Any], None]] = {
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_object_values(HostSslCertificatePort)),
            "sslCertificate": lambda n : setattr(self, 'ssl_certificate', n.get_object_value(SslCertificate)),
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
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("ports", self.ports)
        writer.write_object_value("sslCertificate", self.ssl_certificate)
    

