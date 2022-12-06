from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class EducationAssignmentSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationAssignmentSettings and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates whether turn-in celebration animation will be shown. A value of true indicates that the animation will not be shown. Default value is false.
        self._submission_animation_disabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "submission_animation_disabled": lambda n : setattr(self, 'submission_animation_disabled', n.get_bool_value()),
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
        writer.write_bool_value("submissionAnimationDisabled", self.submission_animation_disabled)
    
    @property
    def submission_animation_disabled(self,) -> Optional[bool]:
        """
        Gets the submissionAnimationDisabled property value. Indicates whether turn-in celebration animation will be shown. A value of true indicates that the animation will not be shown. Default value is false.
        Returns: Optional[bool]
        """
        return self._submission_animation_disabled
    
    @submission_animation_disabled.setter
    def submission_animation_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the submissionAnimationDisabled property value. Indicates whether turn-in celebration animation will be shown. A value of true indicates that the animation will not be shown. Default value is false.
        Args:
            value: Value to set for the submissionAnimationDisabled property.
        """
        self._submission_animation_disabled = value
    

