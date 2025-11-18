from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .web_application_firewall_dns_record_type import WebApplicationFirewallDnsRecordType

@dataclass
class WebApplicationFirewallDnsConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the domain owning this DNS record has been verified by the WAF provider.
    is_domain_verified: Optional[bool] = None
    # Indicates whether traffic for this DNS record is proxied through the WAF provider's network (for example, using a CDN or reverse proxy).
    is_proxied: Optional[bool] = None
    # The DNS record name (for example, www.contoso.com or contoso.com). This is the host or zone name to which the configuration applies.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordType property
    record_type: Optional[WebApplicationFirewallDnsRecordType] = None
    # The value of the DNS record.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplicationFirewallDnsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationFirewallDnsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebApplicationFirewallDnsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .web_application_firewall_dns_record_type import WebApplicationFirewallDnsRecordType

        from .web_application_firewall_dns_record_type import WebApplicationFirewallDnsRecordType

        fields: dict[str, Callable[[Any], None]] = {
            "isDomainVerified": lambda n : setattr(self, 'is_domain_verified', n.get_bool_value()),
            "isProxied": lambda n : setattr(self, 'is_proxied', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recordType": lambda n : setattr(self, 'record_type', n.get_enum_value(WebApplicationFirewallDnsRecordType)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isDomainVerified", self.is_domain_verified)
        writer.write_bool_value("isProxied", self.is_proxied)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recordType", self.record_type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

