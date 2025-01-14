from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_checklist_items import PlannerChecklistItems
    from .planner_external_references import PlannerExternalReferences
    from .planner_preview_type import PlannerPreviewType

from .entity import Entity

@dataclass
class PlannerTaskDetails(Entity, Parsable):
    # The collection of checklist items on the task.
    checklist: Optional[PlannerChecklistItems] = None
    # Description of the task.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
    preview_type: Optional[PlannerPreviewType] = None
    # The collection of references on the task.
    references: Optional[PlannerExternalReferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_external_references import PlannerExternalReferences
        from .planner_preview_type import PlannerPreviewType

        from .entity import Entity
        from .planner_checklist_items import PlannerChecklistItems
        from .planner_external_references import PlannerExternalReferences
        from .planner_preview_type import PlannerPreviewType

        fields: dict[str, Callable[[Any], None]] = {
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(PlannerChecklistItems)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(PlannerExternalReferences)),
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
        writer.write_object_value("checklist", self.checklist)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
    

