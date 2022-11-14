from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import authentication_method_state, entity

class AuthenticationMethodConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.authenticationMethodConfiguration"
        # The state of the policy. Possible values are: enabled, disabled.
        self._state: Optional[authentication_method_state.AuthenticationMethodState] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodConfiguration
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodConfiguration()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "state": lambda n : setattr(self, 'state', n.get_enum_value(authentication_method_state.AuthenticationMethodState)),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("state", self.state)

    @property
    def state(self,) -> Optional[authentication_method_state.AuthenticationMethodState]:
        """
        Gets the state property value. The state of the policy. Possible values are: enabled, disabled.
        Returns: Optional[authentication_method_state.AuthenticationMethodState]
        """
        return self._state

    @state.setter
    def state(self,value: Optional[authentication_method_state.AuthenticationMethodState] = None) -> None:
        """
        Sets the state property value. The state of the policy. Possible values are: enabled, disabled.
        Args:
            value: Value to set for the state property.
        """
        self._state = value

