from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_set_entry import AttributeSetEntry
    from .workflow_subject import WorkflowSubject

from .workflow_subject import WorkflowSubject

@dataclass
class ProvisioningObjectWorkflowSubject(WorkflowSubject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.provisioningObjectWorkflowSubject"
    # The attribute set entries representing the subject's attributes. Each entry is a key-value pair.
    attribute_set_entries: Optional[list[AttributeSetEntry]] = None
    # The identifier of the provisioning object subject.
    id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningObjectWorkflowSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningObjectWorkflowSubject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningObjectWorkflowSubject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_set_entry import AttributeSetEntry
        from .workflow_subject import WorkflowSubject

        from .attribute_set_entry import AttributeSetEntry
        from .workflow_subject import WorkflowSubject

        fields: dict[str, Callable[[Any], None]] = {
            "attributeSetEntries": lambda n : setattr(self, 'attribute_set_entries', n.get_collection_of_object_values(AttributeSetEntry)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_collection_of_object_values("attributeSetEntries", self.attribute_set_entries)
        writer.write_str_value("id", self.id)
    

