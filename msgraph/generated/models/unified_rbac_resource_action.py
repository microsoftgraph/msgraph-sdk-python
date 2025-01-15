from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UnifiedRbacResourceAction(Entity, Parsable):
    # The actionVerb property
    action_verb: Optional[str] = None
    # The authenticationContextId property
    authentication_context_id: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The isAuthenticationContextSettable property
    is_authentication_context_settable: Optional[bool] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceScopeId property
    resource_scope_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRbacResourceAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacResourceAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRbacResourceAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "actionVerb": lambda n : setattr(self, 'action_verb', n.get_str_value()),
            "authenticationContextId": lambda n : setattr(self, 'authentication_context_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "isAuthenticationContextSettable": lambda n : setattr(self, 'is_authentication_context_settable', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "resourceScopeId": lambda n : setattr(self, 'resource_scope_id', n.get_str_value()),
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
        writer.write_str_value("actionVerb", self.action_verb)
        writer.write_str_value("authenticationContextId", self.authentication_context_id)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("isAuthenticationContextSettable", self.is_authentication_context_settable)
        writer.write_str_value("name", self.name)
        writer.write_str_value("resourceScopeId", self.resource_scope_id)
    

