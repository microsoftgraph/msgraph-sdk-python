from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_assignment_grade_type import EducationAssignmentGradeType
    from .education_item_body import EducationItemBody

@dataclass
class RubricLevel(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The description of this rubric level.
    description: Optional[EducationItemBody] = None
    # The name of this rubric level.
    display_name: Optional[str] = None
    # Null if this is a no-points rubric; educationAssignmentPointsGradeType if it's a points rubric.
    grading: Optional[EducationAssignmentGradeType] = None
    # The ID of this resource.
    level_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RubricLevel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RubricLevel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RubricLevel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_assignment_grade_type import EducationAssignmentGradeType
        from .education_item_body import EducationItemBody

        from .education_assignment_grade_type import EducationAssignmentGradeType
        from .education_item_body import EducationItemBody

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_object_value(EducationItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grading": lambda n : setattr(self, 'grading', n.get_object_value(EducationAssignmentGradeType)),
            "levelId": lambda n : setattr(self, 'level_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("grading", self.grading)
        writer.write_str_value("levelId", self.level_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

