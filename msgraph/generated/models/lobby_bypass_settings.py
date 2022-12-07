from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

lobby_bypass_scope = lazy_import('msgraph.generated.models.lobby_bypass_scope')

class LobbyBypassSettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new lobbyBypassSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether or not to always let dial-in callers bypass the lobby. Optional.
        self._is_dial_in_bypass_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the type of participants that are automatically admitted into a meeting, bypassing the lobby. Optional.
        self._scope: Optional[lobby_bypass_scope.LobbyBypassScope] = None
    
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
        fields = {
            "is_dial_in_bypass_enabled": lambda n : setattr(self, 'is_dial_in_bypass_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(lobby_bypass_scope.LobbyBypassScope)),
        }
        return fields
    
    @property
    def is_dial_in_bypass_enabled(self,) -> Optional[bool]:
        """
        Gets the isDialInBypassEnabled property value. Specifies whether or not to always let dial-in callers bypass the lobby. Optional.
        Returns: Optional[bool]
        """
        return self._is_dial_in_bypass_enabled
    
    @is_dial_in_bypass_enabled.setter
    def is_dial_in_bypass_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDialInBypassEnabled property value. Specifies whether or not to always let dial-in callers bypass the lobby. Optional.
        Args:
            value: Value to set for the isDialInBypassEnabled property.
        """
        self._is_dial_in_bypass_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def scope(self,) -> Optional[lobby_bypass_scope.LobbyBypassScope]:
        """
        Gets the scope property value. Specifies the type of participants that are automatically admitted into a meeting, bypassing the lobby. Optional.
        Returns: Optional[lobby_bypass_scope.LobbyBypassScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[lobby_bypass_scope.LobbyBypassScope] = None) -> None:
        """
        Sets the scope property value. Specifies the type of participants that are automatically admitted into a meeting, bypassing the lobby. Optional.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
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
    

