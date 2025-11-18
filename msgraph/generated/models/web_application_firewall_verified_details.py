from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .akamai_verified_details_model import AkamaiVerifiedDetailsModel
    from .cloud_flare_verified_details_model import CloudFlareVerifiedDetailsModel
    from .web_application_firewall_dns_configuration import WebApplicationFirewallDnsConfiguration

@dataclass
class WebApplicationFirewallVerifiedDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # DNS-related details discovered during verification for the host, such as the DNS record name, record type, record value, whether the record is proxied through the provider, and whether the domain is verified.
    dns_configuration: Optional[WebApplicationFirewallDnsConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplicationFirewallVerifiedDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationFirewallVerifiedDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.akamaiVerifiedDetailsModel".casefold():
            from .akamai_verified_details_model import AkamaiVerifiedDetailsModel

            return AkamaiVerifiedDetailsModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudFlareVerifiedDetailsModel".casefold():
            from .cloud_flare_verified_details_model import CloudFlareVerifiedDetailsModel

            return CloudFlareVerifiedDetailsModel()
        return WebApplicationFirewallVerifiedDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .akamai_verified_details_model import AkamaiVerifiedDetailsModel
        from .cloud_flare_verified_details_model import CloudFlareVerifiedDetailsModel
        from .web_application_firewall_dns_configuration import WebApplicationFirewallDnsConfiguration

        from .akamai_verified_details_model import AkamaiVerifiedDetailsModel
        from .cloud_flare_verified_details_model import CloudFlareVerifiedDetailsModel
        from .web_application_firewall_dns_configuration import WebApplicationFirewallDnsConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "dnsConfiguration": lambda n : setattr(self, 'dns_configuration', n.get_object_value(WebApplicationFirewallDnsConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("dnsConfiguration", self.dns_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

