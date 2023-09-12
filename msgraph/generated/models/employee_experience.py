from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .learning_course_activity import LearningCourseActivity
    from .learning_provider import LearningProvider

@dataclass
class EmployeeExperience(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The learningCourseActivities property
    learning_course_activities: Optional[List[LearningCourseActivity]] = None
    # A collection of learning providers.
    learning_providers: Optional[List[LearningProvider]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmployeeExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeExperience
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EmployeeExperience()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider

        fields: Dict[str, Callable[[Any], None]] = {
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(LearningCourseActivity)),
            "learningProviders": lambda n : setattr(self, 'learning_providers', n.get_collection_of_object_values(LearningProvider)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
        writer.write_collection_of_object_values("learningProviders", self.learning_providers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

