from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_grading_category import EducationGradingCategory
    from .education_grading_scheme import EducationGradingScheme
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationAssignmentSettings(Entity, Parsable):
    # The default grading scheme for assignments created in this class.
    default_grading_scheme: Optional[EducationGradingScheme] = None
    # When set, enables users to weight assignments differently when computing a class average grade.
    grading_categories: Optional[list[EducationGradingCategory]] = None
    # The grading schemes that can be attached to assignments created in this class.
    grading_schemes: Optional[list[EducationGradingScheme]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether to show the turn-in celebration animation. If true, indicates to skip the animation. The default value is false.
    submission_animation_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .entity import Entity

        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "defaultGradingScheme": lambda n : setattr(self, 'default_grading_scheme', n.get_object_value(EducationGradingScheme)),
            "gradingCategories": lambda n : setattr(self, 'grading_categories', n.get_collection_of_object_values(EducationGradingCategory)),
            "gradingSchemes": lambda n : setattr(self, 'grading_schemes', n.get_collection_of_object_values(EducationGradingScheme)),
            "submissionAnimationDisabled": lambda n : setattr(self, 'submission_animation_disabled', n.get_bool_value()),
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
        writer.write_object_value("defaultGradingScheme", self.default_grading_scheme)
        writer.write_collection_of_object_values("gradingCategories", self.grading_categories)
        writer.write_collection_of_object_values("gradingSchemes", self.grading_schemes)
        writer.write_bool_value("submissionAnimationDisabled", self.submission_animation_disabled)
    

