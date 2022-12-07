from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

approval_stage = lazy_import('msgraph.generated.models.approval_stage')
entity = lazy_import('msgraph.generated.models.entity')

class Approval(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new approval and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of stages in the approval decision.
        self._stages: Optional[List[approval_stage.ApprovalStage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Approval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Approval
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Approval()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("stages", self.stages)
    
    @property
    def stages(self,) -> Optional[List[approval_stage.ApprovalStage]]:
        """
        Gets the stages property value. A collection of stages in the approval decision.
        Returns: Optional[List[approval_stage.ApprovalStage]]
        """
        return self._stages
    
    @stages.setter
    def stages(self,value: Optional[List[approval_stage.ApprovalStage]] = None) -> None:
        """
        Sets the stages property value. A collection of stages in the approval decision.
        Args:
            value: Value to set for the stages property.
        """
        self._stages = value
    

