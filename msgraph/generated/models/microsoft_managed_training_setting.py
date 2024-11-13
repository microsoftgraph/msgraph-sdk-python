from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_completion_duration import TrainingCompletionDuration
    from .training_setting import TrainingSetting

from .training_setting import TrainingSetting

@dataclass
class MicrosoftManagedTrainingSetting(TrainingSetting, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.microsoftManagedTrainingSetting"
    # The completion date for the training. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    completion_date_time: Optional[datetime.datetime] = None
    # The training completion duration that needs to be provided before scheduling the training. The possible values are: week, fortnite, month, unknownFutureValue.
    training_completion_duration: Optional[TrainingCompletionDuration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftManagedTrainingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftManagedTrainingSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftManagedTrainingSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .training_completion_duration import TrainingCompletionDuration
        from .training_setting import TrainingSetting

        from .training_completion_duration import TrainingCompletionDuration
        from .training_setting import TrainingSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "trainingCompletionDuration": lambda n : setattr(self, 'training_completion_duration', n.get_enum_value(TrainingCompletionDuration)),
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
        from .training_completion_duration import TrainingCompletionDuration
        from .training_setting import TrainingSetting

        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_enum_value("trainingCompletionDuration", self.training_completion_duration)
    

