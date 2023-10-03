from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_assigned_to import TrainingAssignedTo
    from .training_setting import TrainingSetting

from .training_setting import TrainingSetting

@dataclass
class CustomTrainingSetting(TrainingSetting):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customTrainingSetting"
    # The assignedTo property
    assigned_to: Optional[List[TrainingAssignedTo]] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The durationInMinutes property
    duration_in_minutes: Optional[int] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTrainingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTrainingSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomTrainingSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .training_assigned_to import TrainingAssignedTo
        from .training_setting import TrainingSetting

        from .training_assigned_to import TrainingAssignedTo
        from .training_setting import TrainingSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_collection_of_enum_values(TrainingAssignedTo)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "durationInMinutes": lambda n : setattr(self, 'duration_in_minutes', n.get_int_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_enum_values("assignedTo", self.assigned_to)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("durationInMinutes", self.duration_in_minutes)
        writer.write_str_value("url", self.url)
    

