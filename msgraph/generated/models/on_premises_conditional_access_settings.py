from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class OnPremisesConditionalAccessSettings(Entity):
    """
    Singleton entity which represents the Exchange OnPremises Conditional Access Settings for a tenant.
    """
    # Indicates if on premises conditional access is enabled for this organization
    enabled: Optional[bool] = None
    # User groups that will be exempt by on premises conditional access. All users in these groups will be exempt from the conditional access policy.
    excluded_groups: Optional[List[UUID]] = None
    # User groups that will be targeted by on premises conditional access. All users in these groups will be required to have mobile device managed and compliant for mail access.
    included_groups: Optional[List[UUID]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Override the default access rule when allowing a device to ensure access is granted.
    override_default_rule: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesConditionalAccessSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesConditionalAccessSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesConditionalAccessSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "excludedGroups": lambda n : setattr(self, 'excluded_groups', n.get_collection_of_primitive_values(UUID)),
            "includedGroups": lambda n : setattr(self, 'included_groups', n.get_collection_of_primitive_values(UUID)),
            "overrideDefaultRule": lambda n : setattr(self, 'override_default_rule', n.get_bool_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_primitive_values("excludedGroups", self.excluded_groups)
        writer.write_collection_of_primitive_values("includedGroups", self.included_groups)
        writer.write_bool_value("overrideDefaultRule", self.override_default_rule)
    

