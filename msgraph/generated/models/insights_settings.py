from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class InsightsSettings(Entity):
    # The ID of a Microsoft Entra group, of which the specified type of insights are disabled for its members. The default value is null. Optional.
    disabled_for_group: Optional[str] = None
    # true if insights of the specified type are enabled for the organization; false if insights of the specified type are disabled for all users without exceptions. The default value is true. Optional.
    is_enabled_in_organization: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InsightsSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsightsSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InsightsSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "disabledForGroup": lambda n : setattr(self, 'disabled_for_group', n.get_str_value()),
            "isEnabledInOrganization": lambda n : setattr(self, 'is_enabled_in_organization', n.get_bool_value()),
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
        writer.write_str_value("disabledForGroup", self.disabled_for_group)
        writer.write_bool_value("isEnabledInOrganization", self.is_enabled_in_organization)
    

