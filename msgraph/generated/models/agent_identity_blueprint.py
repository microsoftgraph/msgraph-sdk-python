from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application import Application
    from .directory_object import DirectoryObject
    from .inheritable_permission import InheritablePermission

from .application import Application

@dataclass
class AgentIdentityBlueprint(Application, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.agentIdentityBlueprint"
    # Defines scopes of a resource application that may be automatically granted to agent identities without additional consent.
    inheritable_permissions: Optional[list[InheritablePermission]] = None
    # The sponsors for this agent identity blueprint. Sponsors are users or groups who can authorize and manage the lifecycle of agent identity instances. Required during the create operation.
    sponsors: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentIdentityBlueprint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentIdentityBlueprint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentIdentityBlueprint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application import Application
        from .directory_object import DirectoryObject
        from .inheritable_permission import InheritablePermission

        from .application import Application
        from .directory_object import DirectoryObject
        from .inheritable_permission import InheritablePermission

        fields: dict[str, Callable[[Any], None]] = {
            "inheritablePermissions": lambda n : setattr(self, 'inheritable_permissions', n.get_collection_of_object_values(InheritablePermission)),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_collection_of_object_values("inheritablePermissions", self.inheritable_permissions)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
    

