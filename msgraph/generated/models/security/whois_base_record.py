from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host import Host
    from .whois_contact import WhoisContact
    from .whois_history_record import WhoisHistoryRecord
    from .whois_nameserver import WhoisNameserver
    from .whois_record import WhoisRecord

from ..entity import Entity

@dataclass
class WhoisBaseRecord(Entity, Parsable):
    # The contact information for the abuse contact.
    abuse: Optional[WhoisContact] = None
    # The contact information for the admin contact.
    admin: Optional[WhoisContact] = None
    # The contact information for the billing contact.
    billing: Optional[WhoisContact] = None
    # The domain status for this WHOIS object.
    domain_status: Optional[str] = None
    # The date and time when this WHOIS record expires with the registrar. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration_date_time: Optional[datetime.datetime] = None
    # The first seen date and time of this WHOIS record. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    first_seen_date_time: Optional[datetime.datetime] = None
    # The host property
    host: Optional[Host] = None
    # The last seen date and time of this WHOIS record. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The date and time when this WHOIS record was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_update_date_time: Optional[datetime.datetime] = None
    # The nameservers for this WHOIS object.
    nameservers: Optional[list[WhoisNameserver]] = None
    # The contact information for the noc contact.
    noc: Optional[WhoisContact] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The raw WHOIS details for this WHOIS object.
    raw_whois_text: Optional[str] = None
    # The contact information for the registrant contact.
    registrant: Optional[WhoisContact] = None
    # The contact information for the registrar contact.
    registrar: Optional[WhoisContact] = None
    # The date and time when this WHOIS record was registered with a registrar. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    registration_date_time: Optional[datetime.datetime] = None
    # The contact information for the technical contact.
    technical: Optional[WhoisContact] = None
    # The WHOIS server that provides the details.
    whois_server: Optional[str] = None
    # The contact information for the zone contact.
    zone: Optional[WhoisContact] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WhoisBaseRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhoisBaseRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisHistoryRecord".casefold():
            from .whois_history_record import WhoisHistoryRecord

            return WhoisHistoryRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisRecord".casefold():
            from .whois_record import WhoisRecord

            return WhoisRecord()
        return WhoisBaseRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host import Host
        from .whois_contact import WhoisContact
        from .whois_history_record import WhoisHistoryRecord
        from .whois_nameserver import WhoisNameserver
        from .whois_record import WhoisRecord

        from ..entity import Entity
        from .host import Host
        from .whois_contact import WhoisContact
        from .whois_history_record import WhoisHistoryRecord
        from .whois_nameserver import WhoisNameserver
        from .whois_record import WhoisRecord

        fields: dict[str, Callable[[Any], None]] = {
            "abuse": lambda n : setattr(self, 'abuse', n.get_object_value(WhoisContact)),
            "admin": lambda n : setattr(self, 'admin', n.get_object_value(WhoisContact)),
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(WhoisContact)),
            "domainStatus": lambda n : setattr(self, 'domain_status', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "host": lambda n : setattr(self, 'host', n.get_object_value(Host)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "nameservers": lambda n : setattr(self, 'nameservers', n.get_collection_of_object_values(WhoisNameserver)),
            "noc": lambda n : setattr(self, 'noc', n.get_object_value(WhoisContact)),
            "rawWhoisText": lambda n : setattr(self, 'raw_whois_text', n.get_str_value()),
            "registrant": lambda n : setattr(self, 'registrant', n.get_object_value(WhoisContact)),
            "registrar": lambda n : setattr(self, 'registrar', n.get_object_value(WhoisContact)),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "technical": lambda n : setattr(self, 'technical', n.get_object_value(WhoisContact)),
            "whoisServer": lambda n : setattr(self, 'whois_server', n.get_str_value()),
            "zone": lambda n : setattr(self, 'zone', n.get_object_value(WhoisContact)),
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
        writer.write_object_value("abuse", self.abuse)
        writer.write_object_value("admin", self.admin)
        writer.write_object_value("billing", self.billing)
        writer.write_str_value("domainStatus", self.domain_status)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_object_value("host", self.host)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_collection_of_object_values("nameservers", self.nameservers)
        writer.write_object_value("noc", self.noc)
        writer.write_str_value("rawWhoisText", self.raw_whois_text)
        writer.write_object_value("registrant", self.registrant)
        writer.write_object_value("registrar", self.registrar)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_object_value("technical", self.technical)
        writer.write_str_value("whoisServer", self.whois_server)
        writer.write_object_value("zone", self.zone)
    

