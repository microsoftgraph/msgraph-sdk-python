from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .teams_user_configuration import TeamsUserConfiguration

from ..entity import Entity

@dataclass
class TeamsAdminRoot(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the configuration information of users who have accounts hosted on Microsoft Teams.
    user_configurations: Optional[list[TeamsUserConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAdminRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAdminRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAdminRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .teams_user_configuration import TeamsUserConfiguration

        from ..entity import Entity
        from .teams_user_configuration import TeamsUserConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "userConfigurations": lambda n : setattr(self, 'user_configurations', n.get_collection_of_object_values(TeamsUserConfiguration)),
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
        writer.write_collection_of_object_values("userConfigurations", self.user_configurations)
    

