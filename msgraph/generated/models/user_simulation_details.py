from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attack_simulation_user, user_simulation_event_info, user_training_event_info

@dataclass
class UserSimulationDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Number of trainings assigned to a user in an attack simulation and training campaign.
    assigned_trainings_count: Optional[int] = None
    # Number of trainings completed by a user in an attack simulation and training campaign.
    completed_trainings_count: Optional[int] = None
    # Date and time of the compromising online action by a user in an attack simulation and training campaign.
    compromised_date_time: Optional[datetime] = None
    # Number of trainings in progress by a user in an attack simulation and training campaign.
    in_progress_trainings_count: Optional[int] = None
    # Indicates whether a user was compromised in an attack simulation and training campaign.
    is_compromised: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time when a user reported the delivered payload as phishing in the attack simulation and training campaign.
    reported_phish_date_time: Optional[datetime] = None
    # List of simulation events of a user in the attack simulation and training campaign.
    simulation_events: Optional[List[user_simulation_event_info.UserSimulationEventInfo]] = None
    # User in an attack simulation and training campaign.
    simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
    # List of training events of a user in the attack simulation and training campaign.
    training_events: Optional[List[user_training_event_info.UserTrainingEventInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSimulationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSimulationDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSimulationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attack_simulation_user, user_simulation_event_info, user_training_event_info

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTrainingsCount": lambda n : setattr(self, 'assigned_trainings_count', n.get_int_value()),
            "completedTrainingsCount": lambda n : setattr(self, 'completed_trainings_count', n.get_int_value()),
            "compromisedDateTime": lambda n : setattr(self, 'compromised_date_time', n.get_datetime_value()),
            "inProgressTrainingsCount": lambda n : setattr(self, 'in_progress_trainings_count', n.get_int_value()),
            "isCompromised": lambda n : setattr(self, 'is_compromised', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reportedPhishDateTime": lambda n : setattr(self, 'reported_phish_date_time', n.get_datetime_value()),
            "simulationEvents": lambda n : setattr(self, 'simulation_events', n.get_collection_of_object_values(user_simulation_event_info.UserSimulationEventInfo)),
            "simulationUser": lambda n : setattr(self, 'simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "trainingEvents": lambda n : setattr(self, 'training_events', n.get_collection_of_object_values(user_training_event_info.UserTrainingEventInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

