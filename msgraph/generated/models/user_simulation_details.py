from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_user import AttackSimulationUser
    from .user_simulation_event_info import UserSimulationEventInfo
    from .user_training_event_info import UserTrainingEventInfo

@dataclass
class UserSimulationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
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
    simulation_events: Optional[List[UserSimulationEventInfo]] = None
    # User in an attack simulation and training campaign.
    simulation_user: Optional[AttackSimulationUser] = None
    # List of training events of a user in the attack simulation and training campaign.
    training_events: Optional[List[UserTrainingEventInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSimulationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSimulationDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserSimulationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_user import AttackSimulationUser
        from .user_simulation_event_info import UserSimulationEventInfo
        from .user_training_event_info import UserTrainingEventInfo

        from .attack_simulation_user import AttackSimulationUser
        from .user_simulation_event_info import UserSimulationEventInfo
        from .user_training_event_info import UserTrainingEventInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "assigned_trainings_count": lambda n : setattr(self, 'assigned_trainings_count', n.get_int_value()),
            "completed_trainings_count": lambda n : setattr(self, 'completed_trainings_count', n.get_int_value()),
            "compromised_date_time": lambda n : setattr(self, 'compromised_date_time', n.get_datetime_value()),
            "in_progress_trainings_count": lambda n : setattr(self, 'in_progress_trainings_count', n.get_int_value()),
            "is_compromised": lambda n : setattr(self, 'is_compromised', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reported_phish_date_time": lambda n : setattr(self, 'reported_phish_date_time', n.get_datetime_value()),
            "simulation_events": lambda n : setattr(self, 'simulation_events', n.get_collection_of_object_values(UserSimulationEventInfo)),
            "simulation_user": lambda n : setattr(self, 'simulation_user', n.get_object_value(AttackSimulationUser)),
            "training_events": lambda n : setattr(self, 'training_events', n.get_collection_of_object_values(UserTrainingEventInfo)),
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
        writer.write_int_value("assigned_trainings_count", self.assigned_trainings_count)
        writer.write_int_value("completed_trainings_count", self.completed_trainings_count)
        writer.write_datetime_value("compromised_date_time", self.compromised_date_time)
        writer.write_int_value("in_progress_trainings_count", self.in_progress_trainings_count)
        writer.write_bool_value("is_compromised", self.is_compromised)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("reported_phish_date_time", self.reported_phish_date_time)
        writer.write_collection_of_object_values("simulation_events", self.simulation_events)
        writer.write_object_value("simulation_user", self.simulation_user)
        writer.write_collection_of_object_values("training_events", self.training_events)
        writer.write_additional_data_value(self.additional_data)
    

