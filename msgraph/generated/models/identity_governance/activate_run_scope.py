from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activation_scope import ActivationScope
    from .activation_task_scope_type import ActivationTaskScopeType
    from .activation_user_scope_type import ActivationUserScopeType
    from .run import Run

from .activation_scope import ActivationScope

@dataclass
class ActivateRunScope(ActivationScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.activateRunScope"
    # The run property
    run: Optional[Run] = None
    # The taskScope property
    task_scope: Optional[ActivationTaskScopeType] = None
    # The userScope property
    user_scope: Optional[ActivationUserScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivateRunScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivateRunScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivateRunScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activation_scope import ActivationScope
        from .activation_task_scope_type import ActivationTaskScopeType
        from .activation_user_scope_type import ActivationUserScopeType
        from .run import Run

        from .activation_scope import ActivationScope
        from .activation_task_scope_type import ActivationTaskScopeType
        from .activation_user_scope_type import ActivationUserScopeType
        from .run import Run

        fields: dict[str, Callable[[Any], None]] = {
            "run": lambda n : setattr(self, 'run', n.get_object_value(Run)),
            "taskScope": lambda n : setattr(self, 'task_scope', n.get_enum_value(ActivationTaskScopeType)),
            "userScope": lambda n : setattr(self, 'user_scope', n.get_enum_value(ActivationUserScopeType)),
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
        writer.write_object_value("run", self.run)
        writer.write_enum_value("taskScope", self.task_scope)
        writer.write_enum_value("userScope", self.user_scope)
    

