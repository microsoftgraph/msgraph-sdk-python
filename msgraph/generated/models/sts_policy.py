from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .directory_object import DirectoryObject
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .policy_base import PolicyBase
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy

from .policy_base import PolicyBase

@dataclass
class StsPolicy(PolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.stsPolicy"
    # The appliesTo property
    applies_to: Optional[List[DirectoryObject]] = None
    # A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.
    definition: Optional[List[str]] = None
    # If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.
    is_organization_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StsPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy

            return ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from .claims_mapping_policy import ClaimsMappingPolicy

            return ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

            return HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from .token_issuance_policy import TokenIssuancePolicy

            return TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from .token_lifetime_policy import TokenLifetimePolicy

            return TokenLifetimePolicy()
        return StsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .directory_object import DirectoryObject
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .policy_base import PolicyBase
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy

        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .directory_object import DirectoryObject
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .policy_base import PolicyBase
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(DirectoryObject)),
            "definition": lambda n : setattr(self, 'definition', n.get_collection_of_primitive_values(str)),
            "isOrganizationDefault": lambda n : setattr(self, 'is_organization_default', n.get_bool_value()),
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
        writer.write_collection_of_object_values("appliesTo", self.applies_to)
        writer.write_collection_of_primitive_values("definition", self.definition)
        writer.write_bool_value("isOrganizationDefault", self.is_organization_default)
    

