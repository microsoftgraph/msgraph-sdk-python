from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval_stage, entity

from . import entity

@dataclass
class Approval(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of stages in the approval decision.
    stages: Optional[List[approval_stage.ApprovalStage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Approval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Approval
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Approval()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval_stage, entity

        from . import approval_stage, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(approval_stage.ApprovalStage)),
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
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("stages", self.stages)
    

