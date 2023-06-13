from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import lobby_bypass_scope

@dataclass
class LobbyBypassSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies whether or not to always let dial-in callers bypass the lobby. Optional.
    is_dial_in_bypass_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the type of participants that are automatically admitted into a meeting, bypassing the lobby. Optional.
    scope: Optional[lobby_bypass_scope.LobbyBypassScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LobbyBypassSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LobbyBypassSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LobbyBypassSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import lobby_bypass_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "isDialInBypassEnabled": lambda n : setattr(self, 'is_dial_in_bypass_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(lobby_bypass_scope.LobbyBypassScope)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isDialInBypassEnabled", self.is_dial_in_bypass_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("scope", self.scope)
        writer.write_additional_data_value(self.additional_data)
    

