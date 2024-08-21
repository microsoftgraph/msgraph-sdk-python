from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_assignment_points_grade import EducationAssignmentPointsGrade
    from .identity_set import IdentitySet

@dataclass
class EducationAssignmentGrade(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # User who did the grading.
    graded_by: Optional[IdentitySet] = None
    # Moment in time when the grade was applied to this submission object. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    graded_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAssignmentGrade:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentGrade
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentPointsGrade".casefold():
            from .education_assignment_points_grade import EducationAssignmentPointsGrade

            return EducationAssignmentPointsGrade()
        return EducationAssignmentGrade()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_assignment_points_grade import EducationAssignmentPointsGrade
        from .identity_set import IdentitySet

        from .education_assignment_points_grade import EducationAssignmentPointsGrade
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "gradedBy": lambda n : setattr(self, 'graded_by', n.get_object_value(IdentitySet)),
            "gradedDateTime": lambda n : setattr(self, 'graded_date_time', n.get_datetime_value()),
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
        writer.write_object_value("gradedBy", self.graded_by)
        writer.write_datetime_value("gradedDateTime", self.graded_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

