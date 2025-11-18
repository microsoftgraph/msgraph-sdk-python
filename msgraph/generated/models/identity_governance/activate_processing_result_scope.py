from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activation_scope import ActivationScope
    from .activation_task_scope_type import ActivationTaskScopeType
    from .user_processing_result import UserProcessingResult

from .activation_scope import ActivationScope

@dataclass
class ActivateProcessingResultScope(ActivationScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.activateProcessingResultScope"
    # The processingResults property
    processing_results: Optional[list[UserProcessingResult]] = None
    # The taskScope property
    task_scope: Optional[ActivationTaskScopeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivateProcessingResultScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivateProcessingResultScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivateProcessingResultScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activation_scope import ActivationScope
        from .activation_task_scope_type import ActivationTaskScopeType
        from .user_processing_result import UserProcessingResult

        from .activation_scope import ActivationScope
        from .activation_task_scope_type import ActivationTaskScopeType
        from .user_processing_result import UserProcessingResult

        fields: dict[str, Callable[[Any], None]] = {
            "processingResults": lambda n : setattr(self, 'processing_results', n.get_collection_of_object_values(UserProcessingResult)),
            "taskScope": lambda n : setattr(self, 'task_scope', n.get_enum_value(ActivationTaskScopeType)),
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
        writer.write_collection_of_object_values("processingResults", self.processing_results)
        writer.write_enum_value("taskScope", self.task_scope)
    

