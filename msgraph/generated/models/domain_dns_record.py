from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_dns_cname_record import DomainDnsCnameRecord
    from .domain_dns_mx_record import DomainDnsMxRecord
    from .domain_dns_srv_record import DomainDnsSrvRecord
    from .domain_dns_txt_record import DomainDnsTxtRecord
    from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
    from .entity import Entity

from .entity import Entity

@dataclass
class DomainDnsRecord(Entity, Parsable):
    # If false, the customer must configure this record at the DNS host for Microsoft Online Services to operate correctly with the domain.
    is_optional: Optional[bool] = None
    # Value used when configuring the name of the DNS record at the DNS host.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates what type of DNS record this entity represents. The value can be CName, Mx, Srv, or Txt.
    record_type: Optional[str] = None
    # Microsoft Online Service or feature that has a dependency on this DNS record. Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
    supported_service: Optional[str] = None
    # Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
    ttl: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainDnsRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsCnameRecord".casefold():
            from .domain_dns_cname_record import DomainDnsCnameRecord

            return DomainDnsCnameRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsMxRecord".casefold():
            from .domain_dns_mx_record import DomainDnsMxRecord

            return DomainDnsMxRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsSrvRecord".casefold():
            from .domain_dns_srv_record import DomainDnsSrvRecord

            return DomainDnsSrvRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsTxtRecord".casefold():
            from .domain_dns_txt_record import DomainDnsTxtRecord

            return DomainDnsTxtRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsUnavailableRecord".casefold():
            from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

            return DomainDnsUnavailableRecord()
        return DomainDnsRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .entity import Entity

        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "recordType": lambda n : setattr(self, 'record_type', n.get_str_value()),
            "supportedService": lambda n : setattr(self, 'supported_service', n.get_str_value()),
            "ttl": lambda n : setattr(self, 'ttl', n.get_int_value()),
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
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("label", self.label)
        writer.write_str_value("recordType", self.record_type)
        writer.write_str_value("supportedService", self.supported_service)
        writer.write_int_value("ttl", self.ttl)
    

