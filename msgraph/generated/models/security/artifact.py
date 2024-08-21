from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host
    from .hostname import Hostname
    from .host_component import HostComponent
    from .host_cookie import HostCookie
    from .host_ssl_certificate import HostSslCertificate
    from .host_tracker import HostTracker
    from .ip_address import IpAddress
    from .passive_dns_record import PassiveDnsRecord
    from .ssl_certificate import SslCertificate
    from .unclassified_artifact import UnclassifiedArtifact

from ..entity import Entity

@dataclass
class Artifact(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Artifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Artifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.host".casefold():
            from .host import Host

            return Host()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostComponent".casefold():
            from .host_component import HostComponent

            return HostComponent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostCookie".casefold():
            from .host_cookie import HostCookie

            return HostCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from .hostname import Hostname

            return Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostSslCertificate".casefold():
            from .host_ssl_certificate import HostSslCertificate

            return HostSslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostTracker".casefold():
            from .host_tracker import HostTracker

            return HostTracker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from .ip_address import IpAddress

            return IpAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.passiveDnsRecord".casefold():
            from .passive_dns_record import PassiveDnsRecord

            return PassiveDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sslCertificate".casefold():
            from .ssl_certificate import SslCertificate

            return SslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unclassifiedArtifact".casefold():
            from .unclassified_artifact import UnclassifiedArtifact

            return UnclassifiedArtifact()
        return Artifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host
        from .hostname import Hostname
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord
        from .ssl_certificate import SslCertificate
        from .unclassified_artifact import UnclassifiedArtifact

        from ..entity import Entity
        from .host import Host
        from .hostname import Hostname
        from .host_component import HostComponent
        from .host_cookie import HostCookie
        from .host_ssl_certificate import HostSslCertificate
        from .host_tracker import HostTracker
        from .ip_address import IpAddress
        from .passive_dns_record import PassiveDnsRecord
        from .ssl_certificate import SslCertificate
        from .unclassified_artifact import UnclassifiedArtifact

        fields: Dict[str, Callable[[Any], None]] = {
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
    

