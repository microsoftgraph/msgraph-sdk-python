from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_combination_configuration

from . import authentication_combination_configuration

@dataclass
class Fido2CombinationConfiguration(authentication_combination_configuration.AuthenticationCombinationConfiguration):
    odata_type = "#microsoft.graph.fido2CombinationConfiguration"
    # A list of AAGUIDs allowed to be used as part of the specified authentication method combinations.
    allowed_a_a_g_u_i_ds: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Fido2CombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Fido2CombinationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Fido2CombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_combination_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedAAGUIDs": lambda n : setattr(self, 'allowed_a_a_g_u_i_ds', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("allowedAAGUIDs", self.allowed_a_a_g_u_i_ds)
    

