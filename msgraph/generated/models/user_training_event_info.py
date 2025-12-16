from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .training_status import TrainingStatus
    from .user_training_content_event_info import UserTrainingContentEventInfo

@dataclass
class UserTrainingEventInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Display name of the training.
    display_name: Optional[str] = None
    # Latest status of the training assigned to the user. The possible values are: unknown, assigned, inProgress, completed, overdue, unknownFutureValue.
    latest_training_status: Optional[TrainingStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Event details of the training when it was assigned to the user.
    training_assigned_properties: Optional[UserTrainingContentEventInfo] = None
    # Event details of the training when it was completed by the user.
    training_completed_properties: Optional[UserTrainingContentEventInfo] = None
    # Event details of the training when it was updated/in-progress by the user.
    training_updated_properties: Optional[UserTrainingContentEventInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserTrainingEventInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingEventInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserTrainingEventInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .training_status import TrainingStatus
        from .user_training_content_event_info import UserTrainingContentEventInfo

        from .training_status import TrainingStatus
        from .user_training_content_event_info import UserTrainingContentEventInfo

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "latestTrainingStatus": lambda n : setattr(self, 'latest_training_status', n.get_enum_value(TrainingStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "trainingAssignedProperties": lambda n : setattr(self, 'training_assigned_properties', n.get_object_value(UserTrainingContentEventInfo)),
            "trainingCompletedProperties": lambda n : setattr(self, 'training_completed_properties', n.get_object_value(UserTrainingContentEventInfo)),
            "trainingUpdatedProperties": lambda n : setattr(self, 'training_updated_properties', n.get_object_value(UserTrainingContentEventInfo)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("latestTrainingStatus", self.latest_training_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("trainingAssignedProperties", self.training_assigned_properties)
        writer.write_object_value("trainingCompletedProperties", self.training_completed_properties)
        writer.write_object_value("trainingUpdatedProperties", self.training_updated_properties)
        writer.write_additional_data_value(self.additional_data)
    

