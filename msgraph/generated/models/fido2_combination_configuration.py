from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_combination_configuration import AuthenticationCombinationConfiguration

from .authentication_combination_configuration import AuthenticationCombinationConfiguration

@dataclass
class Fido2CombinationConfiguration(AuthenticationCombinationConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.fido2CombinationConfiguration"
    # A list of AAGUIDs allowed to be used as part of the specified authentication method combinations.
    allowed_a_a_g_u_i_ds: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Fido2CombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Fido2CombinationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Fido2CombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration

        from .authentication_combination_configuration import AuthenticationCombinationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedAAGUIDs": lambda n : setattr(self, 'allowed_a_a_g_u_i_ds', n.get_collection_of_primitive_values(str)),
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
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration

        writer.write_collection_of_primitive_values("allowedAAGUIDs", self.allowed_a_a_g_u_i_ds)
    

