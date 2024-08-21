from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training import Training
    from .training_assigned_to import TrainingAssignedTo
    from .training_setting import TrainingSetting

from .training_setting import TrainingSetting

@dataclass
class MicrosoftTrainingAssignmentMapping(TrainingSetting):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.microsoftTrainingAssignmentMapping"
    # A user collection that specifies to whom the training should be assigned. Possible values are: none, allUsers, clickedPayload, compromised, reportedPhish, readButNotClicked, didNothing, unknownFutureValue.
    assigned_to: Optional[List[TrainingAssignedTo]] = None
    # The training property
    training: Optional[Training] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTrainingAssignmentMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTrainingAssignmentMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTrainingAssignmentMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .training import Training
        from .training_assigned_to import TrainingAssignedTo
        from .training_setting import TrainingSetting

        from .training import Training
        from .training_assigned_to import TrainingAssignedTo
        from .training_setting import TrainingSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_collection_of_enum_values(TrainingAssignedTo)),
            "training": lambda n : setattr(self, 'training', n.get_object_value(Training)),
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
        writer.write_collection_of_enum_values("assignedTo", self.assigned_to)
        writer.write_object_value("training", self.training)
    

