from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_flare_ruleset_model import CloudFlareRulesetModel
    from .cloud_flare_rule_model import CloudFlareRuleModel
    from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

@dataclass
class CloudFlareVerifiedDetailsModel(WebApplicationFirewallVerifiedDetails, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudFlareVerifiedDetailsModel"
    # Collection of Cloudflare custom rules that are currently enabled for the zone or host.
    enabled_custom_rules: Optional[list[CloudFlareRuleModel]] = None
    # Collection of Cloudflare recommended rulesets that are enabled for the zone or host.
    enabled_recommended_rulesets: Optional[list[CloudFlareRulesetModel]] = None
    # Cloudflare-assigned identifier for the DNS zone associated with the verified host (for example, the Cloudflare Zone ID). This ID is used to correlate verification details with the Cloudflare account and to perform configuration operations via the provider's API.
    zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFlareVerifiedDetailsModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFlareVerifiedDetailsModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFlareVerifiedDetailsModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_flare_ruleset_model import CloudFlareRulesetModel
        from .cloud_flare_rule_model import CloudFlareRuleModel
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        from .cloud_flare_ruleset_model import CloudFlareRulesetModel
        from .cloud_flare_rule_model import CloudFlareRuleModel
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        fields: dict[str, Callable[[Any], None]] = {
            "enabledCustomRules": lambda n : setattr(self, 'enabled_custom_rules', n.get_collection_of_object_values(CloudFlareRuleModel)),
            "enabledRecommendedRulesets": lambda n : setattr(self, 'enabled_recommended_rulesets', n.get_collection_of_object_values(CloudFlareRulesetModel)),
            "zoneId": lambda n : setattr(self, 'zone_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("enabledCustomRules", self.enabled_custom_rules)
        writer.write_collection_of_object_values("enabledRecommendedRulesets", self.enabled_recommended_rulesets)
        writer.write_str_value("zoneId", self.zone_id)
    

