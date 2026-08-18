from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .recovery_action import RecoveryAction
    from .resource_type_name import ResourceTypeName

from ..entity import Entity

@dataclass
class RecoveryChangeObjectBase(Entity, Parsable):
    # The display name of the changed object in its current state, used to uniquely identify the object. Supports $filter (eq, ne, startswith).
    display_name: Optional[str] = None
    # The entityTypeName property
    entity_type_name: Optional[ResourceTypeName] = None
    # The error message if the change failed to apply. Only populated in getFailedChanges responses. null otherwise.
    failure_message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recoveryAction property
    recovery_action: Optional[RecoveryAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryChangeObjectBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryChangeObjectBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecoveryChangeObjectBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .recovery_action import RecoveryAction
        from .resource_type_name import ResourceTypeName

        from ..entity import Entity
        from .recovery_action import RecoveryAction
        from .resource_type_name import ResourceTypeName

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "entityTypeName": lambda n : setattr(self, 'entity_type_name', n.get_enum_value(ResourceTypeName)),
            "failureMessage": lambda n : setattr(self, 'failure_message', n.get_str_value()),
            "recoveryAction": lambda n : setattr(self, 'recovery_action', n.get_enum_value(RecoveryAction)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("entityTypeName", self.entity_type_name)
        writer.write_str_value("failureMessage", self.failure_message)
        writer.write_enum_value("recoveryAction", self.recovery_action)
    

