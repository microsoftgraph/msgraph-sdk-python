from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host
    from .host_port_banner import HostPortBanner
    from .host_port_component import HostPortComponent
    from .host_port_protocol import HostPortProtocol
    from .host_port_status import HostPortStatus
    from .ssl_certificate import SslCertificate

from ..entity import Entity

@dataclass
class HostPort(Entity, Parsable):
    # The hostPortBanners retrieved from scanning the port.
    banners: Optional[list[HostPortBanner]] = None
    # The first date and time when Microsoft Defender Threat Intelligence observed the hostPort. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host property
    host: Optional[Host] = None
    # The last date and time when Microsoft Defender Threat Intelligence scanned the hostPort. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    last_scan_date_time: Optional[datetime.datetime] = None
    # The last date and time when Microsoft Defender Threat Intelligence observed the hostPort. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The most recent sslCertificate used to communicate on the port.
    most_recent_ssl_certificate: Optional[SslCertificate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The numerical identifier of the port which is standardized across the internet.
    port: Optional[int] = None
    # The general protocol used to scan the port. The possible values are: tcp, udp, unknownFutureValue.
    protocol: Optional[HostPortProtocol] = None
    # The hostPortComponents retrieved from scanning the port.
    services: Optional[list[HostPortComponent]] = None
    # The status of the port. The possible values are: open, filtered, closed, unknownFutureValue.
    status: Optional[HostPortStatus] = None
    # The total amount of times that Microsoft Defender Threat Intelligence has observed the hostPort in all its scans.
    times_observed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostPort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostPort
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostPort()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host
        from .host_port_banner import HostPortBanner
        from .host_port_component import HostPortComponent
        from .host_port_protocol import HostPortProtocol
        from .host_port_status import HostPortStatus
        from .ssl_certificate import SslCertificate

        from ..entity import Entity
        from .host import Host
        from .host_port_banner import HostPortBanner
        from .host_port_component import HostPortComponent
        from .host_port_protocol import HostPortProtocol
        from .host_port_status import HostPortStatus
        from .ssl_certificate import SslCertificate

        fields: dict[str, Callable[[Any], None]] = {
            "banners": lambda n : setattr(self, 'banners', n.get_collection_of_object_values(HostPortBanner)),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastScanDateTime": lambda n : setattr(self, 'last_scan_date_time', n.get_datetime_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "mostRecentSslCertificate": lambda n : setattr(self, 'most_recent_ssl_certificate', n.get_object_value(SslCertificate)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(HostPortProtocol)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(HostPortComponent)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HostPortStatus)),
            "timesObserved": lambda n : setattr(self, 'times_observed', n.get_int_value()),
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
        writer.write_collection_of_object_values("banners", self.banners)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastScanDateTime", self.last_scan_date_time)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_object_value("mostRecentSslCertificate", self.most_recent_ssl_certificate)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("timesObserved", self.times_observed)
    

