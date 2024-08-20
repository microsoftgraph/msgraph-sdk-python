from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_governance.workflow import Workflow

from .entity import Entity

@dataclass
class DeletedItemContainer(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Deleted workflows that end up in the deletedItemsContainer.
    workflows: Optional[List[Workflow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeletedItemContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeletedItemContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeletedItemContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_governance.workflow import Workflow

        from .entity import Entity
        from .identity_governance.workflow import Workflow

        fields: Dict[str, Callable[[Any], None]] = {
            "workflows": lambda n : setattr(self, 'workflows', n.get_collection_of_object_values(Workflow)),
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
        writer.write_collection_of_object_values("workflows", self.workflows)
    

