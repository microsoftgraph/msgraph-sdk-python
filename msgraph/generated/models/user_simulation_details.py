from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_user import AttackSimulationUser
    from .user_simulation_event_info import UserSimulationEventInfo
    from .user_training_event_info import UserTrainingEventInfo

@dataclass
class UserSimulationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Number of trainings assigned to a user in an attack simulation and training campaign.
    assigned_trainings_count: Optional[int] = None
    # Number of trainings completed by a user in an attack simulation and training campaign.
    completed_trainings_count: Optional[int] = None
    # Date and time of the compromising online action by a user in an attack simulation and training campaign.
    compromised_date_time: Optional[datetime.datetime] = None
    # Number of trainings in progress by a user in an attack simulation and training campaign.
    in_progress_trainings_count: Optional[int] = None
    # Indicates whether a user was compromised in an attack simulation and training campaign.
    is_compromised: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time when a user reported the delivered payload as phishing in the attack simulation and training campaign.
    reported_phish_date_time: Optional[datetime.datetime] = None
    # List of simulation events of a user in the attack simulation and training campaign.
    simulation_events: Optional[list[UserSimulationEventInfo]] = None
    # User in an attack simulation and training campaign.
    simulation_user: Optional[AttackSimulationUser] = None
    # List of training events of a user in the attack simulation and training campaign.
    training_events: Optional[list[UserTrainingEventInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSimulationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSimulationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSimulationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_user import AttackSimulationUser
        from .user_simulation_event_info import UserSimulationEventInfo
        from .user_training_event_info import UserTrainingEventInfo

        from .attack_simulation_user import AttackSimulationUser
        from .user_simulation_event_info import UserSimulationEventInfo
        from .user_training_event_info import UserTrainingEventInfo

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTrainingsCount": lambda n : setattr(self, 'assigned_trainings_count', n.get_int_value()),
            "completedTrainingsCount": lambda n : setattr(self, 'completed_trainings_count', n.get_int_value()),
            "compromisedDateTime": lambda n : setattr(self, 'compromised_date_time', n.get_datetime_value()),
            "inProgressTrainingsCount": lambda n : setattr(self, 'in_progress_trainings_count', n.get_int_value()),
            "isCompromised": lambda n : setattr(self, 'is_compromised', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reportedPhishDateTime": lambda n : setattr(self, 'reported_phish_date_time', n.get_datetime_value()),
            "simulationEvents": lambda n : setattr(self, 'simulation_events', n.get_collection_of_object_values(UserSimulationEventInfo)),
            "simulationUser": lambda n : setattr(self, 'simulation_user', n.get_object_value(AttackSimulationUser)),
            "trainingEvents": lambda n : setattr(self, 'training_events', n.get_collection_of_object_values(UserTrainingEventInfo)),
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
        writer.write_int_value("assignedTrainingsCount", self.assigned_trainings_count)
        writer.write_int_value("completedTrainingsCount", self.completed_trainings_count)
        writer.write_datetime_value("compromisedDateTime", self.compromised_date_time)
        writer.write_int_value("inProgressTrainingsCount", self.in_progress_trainings_count)
        writer.write_bool_value("isCompromised", self.is_compromised)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("reportedPhishDateTime", self.reported_phish_date_time)
        writer.write_collection_of_object_values("simulationEvents", self.simulation_events)
        writer.write_object_value("simulationUser", self.simulation_user)
        writer.write_collection_of_object_values("trainingEvents", self.training_events)
        writer.write_additional_data_value(self.additional_data)
    

