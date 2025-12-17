from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_status import TrainingStatus

@dataclass
class UserTrainingStatusInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Date and time of assignment of the training to the user.
    assigned_date_time: Optional[datetime.datetime] = None
    # Date and time of completion of the training by the user.
    completion_date_time: Optional[datetime.datetime] = None
    # Display name of the assigned training.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the training assigned to the user. The possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
    training_status: Optional[TrainingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserTrainingStatusInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingStatusInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserTrainingStatusInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .training_status import TrainingStatus

        from .training_status import TrainingStatus

        fields: dict[str, Callable[[Any], None]] = {
            "assignedDateTime": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trainingStatus": lambda n : setattr(self, 'training_status', n.get_enum_value(TrainingStatus)),
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
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("trainingStatus", self.training_status)
        writer.write_additional_data_value(self.additional_data)
    

