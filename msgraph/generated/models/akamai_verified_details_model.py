from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .akamai_attack_group_action_model import AkamaiAttackGroupActionModel
    from .akamai_custom_rule_model import AkamaiCustomRuleModel
    from .akamai_rapid_rules_model import AkamaiRapidRulesModel
    from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

@dataclass
class AkamaiVerifiedDetailsModel(WebApplicationFirewallVerifiedDetails, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.akamaiVerifiedDetailsModel"
    # Collection of Akamai attack groups that are currently active for the zone or host, including the action applied to each group (for example, deny, none or alert).
    active_attack_groups: Optional[list[AkamaiAttackGroupActionModel]] = None
    # Collection of Akamai custom rules that are currently enabled for the zone or host. Each entry includes rule metadata such as the rule identifier, friendly name, and the action taken when the rule matches traffic.
    active_custom_rules: Optional[list[AkamaiCustomRuleModel]] = None
    # Configuration for Akamai Rapid Rules, including whether Rapid Rules are enabled and the default action applied to matching traffic.
    rapid_rules: Optional[AkamaiRapidRulesModel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AkamaiVerifiedDetailsModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AkamaiVerifiedDetailsModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AkamaiVerifiedDetailsModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .akamai_attack_group_action_model import AkamaiAttackGroupActionModel
        from .akamai_custom_rule_model import AkamaiCustomRuleModel
        from .akamai_rapid_rules_model import AkamaiRapidRulesModel
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        from .akamai_attack_group_action_model import AkamaiAttackGroupActionModel
        from .akamai_custom_rule_model import AkamaiCustomRuleModel
        from .akamai_rapid_rules_model import AkamaiRapidRulesModel
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        fields: dict[str, Callable[[Any], None]] = {
            "activeAttackGroups": lambda n : setattr(self, 'active_attack_groups', n.get_collection_of_object_values(AkamaiAttackGroupActionModel)),
            "activeCustomRules": lambda n : setattr(self, 'active_custom_rules', n.get_collection_of_object_values(AkamaiCustomRuleModel)),
            "rapidRules": lambda n : setattr(self, 'rapid_rules', n.get_object_value(AkamaiRapidRulesModel)),
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
        writer.write_collection_of_object_values("activeAttackGroups", self.active_attack_groups)
        writer.write_collection_of_object_values("activeCustomRules", self.active_custom_rules)
        writer.write_object_value("rapidRules", self.rapid_rules)
    

