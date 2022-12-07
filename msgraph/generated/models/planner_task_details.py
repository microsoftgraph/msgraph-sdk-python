from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
planner_checklist_items = lazy_import('msgraph.generated.models.planner_checklist_items')
planner_external_references = lazy_import('msgraph.generated.models.planner_external_references')
planner_preview_type = lazy_import('msgraph.generated.models.planner_preview_type')

class PlannerTaskDetails(entity.Entity):
    @property
    def checklist(self,) -> Optional[planner_checklist_items.PlannerChecklistItems]:
        """
        Gets the checklist property value. The collection of checklist items on the task.
        Returns: Optional[planner_checklist_items.PlannerChecklistItems]
        """
        return self._checklist
    
    @checklist.setter
    def checklist(self,value: Optional[planner_checklist_items.PlannerChecklistItems] = None) -> None:
        """
        Sets the checklist property value. The collection of checklist items on the task.
        Args:
            value: Value to set for the checklist property.
        """
        self._checklist = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskDetails and sets the default values.
        """
        super().__init__()
        # The collection of checklist items on the task.
        self._checklist: Optional[planner_checklist_items.PlannerChecklistItems] = None
        # Description of the task.
        self._description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        self._preview_type: Optional[planner_preview_type.PlannerPreviewType] = None
        # The collection of references on the task.
        self._references: Optional[planner_external_references.PlannerExternalReferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskDetails()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the task.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the task.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "checklist": lambda n : setattr(self, 'checklist', n.get_object_value(planner_checklist_items.PlannerChecklistItems)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "preview_type": lambda n : setattr(self, 'preview_type', n.get_enum_value(planner_preview_type.PlannerPreviewType)),
            "references": lambda n : setattr(self, 'references', n.get_object_value(planner_external_references.PlannerExternalReferences)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def preview_type(self,) -> Optional[planner_preview_type.PlannerPreviewType]:
        """
        Gets the previewType property value. This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        Returns: Optional[planner_preview_type.PlannerPreviewType]
        """
        return self._preview_type
    
    @preview_type.setter
    def preview_type(self,value: Optional[planner_preview_type.PlannerPreviewType] = None) -> None:
        """
        Sets the previewType property value. This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference. When set to automatic the displayed preview is chosen by the app viewing the task.
        Args:
            value: Value to set for the previewType property.
        """
        self._preview_type = value
    
    @property
    def references(self,) -> Optional[planner_external_references.PlannerExternalReferences]:
        """
        Gets the references property value. The collection of references on the task.
        Returns: Optional[planner_external_references.PlannerExternalReferences]
        """
        return self._references
    
    @references.setter
    def references(self,value: Optional[planner_external_references.PlannerExternalReferences] = None) -> None:
        """
        Sets the references property value. The collection of references on the task.
        Args:
            value: Value to set for the references property.
        """
        self._references = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("checklist", self.checklist)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_object_value("references", self.references)
    

