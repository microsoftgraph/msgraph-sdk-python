from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_user = lazy_import('msgraph.generated.models.attack_simulation_user')
user_simulation_event_info = lazy_import('msgraph.generated.models.user_simulation_event_info')
user_training_event_info = lazy_import('msgraph.generated.models.user_training_event_info')

class UserSimulationDetails(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def assigned_trainings_count(self,) -> Optional[int]:
        """
        Gets the assignedTrainingsCount property value. Number of trainings assigned to a user in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._assigned_trainings_count
    
    @assigned_trainings_count.setter
    def assigned_trainings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the assignedTrainingsCount property value. Number of trainings assigned to a user in an attack simulation and training campaign.
        Args:
            value: Value to set for the assignedTrainingsCount property.
        """
        self._assigned_trainings_count = value
    
    @property
    def completed_trainings_count(self,) -> Optional[int]:
        """
        Gets the completedTrainingsCount property value. Number of trainings completed by a user in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._completed_trainings_count
    
    @completed_trainings_count.setter
    def completed_trainings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedTrainingsCount property value. Number of trainings completed by a user in an attack simulation and training campaign.
        Args:
            value: Value to set for the completedTrainingsCount property.
        """
        self._completed_trainings_count = value
    
    @property
    def compromised_date_time(self,) -> Optional[datetime]:
        """
        Gets the compromisedDateTime property value. Date and time of the compromising online action by a user in an attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._compromised_date_time
    
    @compromised_date_time.setter
    def compromised_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the compromisedDateTime property value. Date and time of the compromising online action by a user in an attack simulation and training campaign.
        Args:
            value: Value to set for the compromisedDateTime property.
        """
        self._compromised_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userSimulationDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of trainings assigned to a user in an attack simulation and training campaign.
        self._assigned_trainings_count: Optional[int] = None
        # Number of trainings completed by a user in an attack simulation and training campaign.
        self._completed_trainings_count: Optional[int] = None
        # Date and time of the compromising online action by a user in an attack simulation and training campaign.
        self._compromised_date_time: Optional[datetime] = None
        # Number of trainings in progress by a user in an attack simulation and training campaign.
        self._in_progress_trainings_count: Optional[int] = None
        # Indicates whether a user was compromised in an attack simulation and training campaign.
        self._is_compromised: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Date and time when a user reported the delivered payload as phishing in the attack simulation and training campaign.
        self._reported_phish_date_time: Optional[datetime] = None
        # List of simulation events of a user in the attack simulation and training campaign.
        self._simulation_events: Optional[List[user_simulation_event_info.UserSimulationEventInfo]] = None
        # User in an attack simulation and training campaign.
        self._simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
        # List of training events of a user in the attack simulation and training campaign.
        self._training_events: Optional[List[user_training_event_info.UserTrainingEventInfo]] = None
    
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
        fields = {
            "assigned_trainings_count": lambda n : setattr(self, 'assigned_trainings_count', n.get_int_value()),
            "completed_trainings_count": lambda n : setattr(self, 'completed_trainings_count', n.get_int_value()),
            "compromised_date_time": lambda n : setattr(self, 'compromised_date_time', n.get_datetime_value()),
            "in_progress_trainings_count": lambda n : setattr(self, 'in_progress_trainings_count', n.get_int_value()),
            "is_compromised": lambda n : setattr(self, 'is_compromised', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reported_phish_date_time": lambda n : setattr(self, 'reported_phish_date_time', n.get_datetime_value()),
            "simulation_events": lambda n : setattr(self, 'simulation_events', n.get_collection_of_object_values(user_simulation_event_info.UserSimulationEventInfo)),
            "simulation_user": lambda n : setattr(self, 'simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "training_events": lambda n : setattr(self, 'training_events', n.get_collection_of_object_values(user_training_event_info.UserTrainingEventInfo)),
        }
        return fields
    
    @property
    def in_progress_trainings_count(self,) -> Optional[int]:
        """
        Gets the inProgressTrainingsCount property value. Number of trainings in progress by a user in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._in_progress_trainings_count
    
    @in_progress_trainings_count.setter
    def in_progress_trainings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the inProgressTrainingsCount property value. Number of trainings in progress by a user in an attack simulation and training campaign.
        Args:
            value: Value to set for the inProgressTrainingsCount property.
        """
        self._in_progress_trainings_count = value
    
    @property
    def is_compromised(self,) -> Optional[bool]:
        """
        Gets the isCompromised property value. Indicates whether a user was compromised in an attack simulation and training campaign.
        Returns: Optional[bool]
        """
        return self._is_compromised
    
    @is_compromised.setter
    def is_compromised(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompromised property value. Indicates whether a user was compromised in an attack simulation and training campaign.
        Args:
            value: Value to set for the isCompromised property.
        """
        self._is_compromised = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def reported_phish_date_time(self,) -> Optional[datetime]:
        """
        Gets the reportedPhishDateTime property value. Date and time when a user reported the delivered payload as phishing in the attack simulation and training campaign.
        Returns: Optional[datetime]
        """
        return self._reported_phish_date_time
    
    @reported_phish_date_time.setter
    def reported_phish_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reportedPhishDateTime property value. Date and time when a user reported the delivered payload as phishing in the attack simulation and training campaign.
        Args:
            value: Value to set for the reportedPhishDateTime property.
        """
        self._reported_phish_date_time = value
    
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
    
    @property
    def simulation_events(self,) -> Optional[List[user_simulation_event_info.UserSimulationEventInfo]]:
        """
        Gets the simulationEvents property value. List of simulation events of a user in the attack simulation and training campaign.
        Returns: Optional[List[user_simulation_event_info.UserSimulationEventInfo]]
        """
        return self._simulation_events
    
    @simulation_events.setter
    def simulation_events(self,value: Optional[List[user_simulation_event_info.UserSimulationEventInfo]] = None) -> None:
        """
        Sets the simulationEvents property value. List of simulation events of a user in the attack simulation and training campaign.
        Args:
            value: Value to set for the simulationEvents property.
        """
        self._simulation_events = value
    
    @property
    def simulation_user(self,) -> Optional[attack_simulation_user.AttackSimulationUser]:
        """
        Gets the simulationUser property value. User in an attack simulation and training campaign.
        Returns: Optional[attack_simulation_user.AttackSimulationUser]
        """
        return self._simulation_user
    
    @simulation_user.setter
    def simulation_user(self,value: Optional[attack_simulation_user.AttackSimulationUser] = None) -> None:
        """
        Sets the simulationUser property value. User in an attack simulation and training campaign.
        Args:
            value: Value to set for the simulationUser property.
        """
        self._simulation_user = value
    
    @property
    def training_events(self,) -> Optional[List[user_training_event_info.UserTrainingEventInfo]]:
        """
        Gets the trainingEvents property value. List of training events of a user in the attack simulation and training campaign.
        Returns: Optional[List[user_training_event_info.UserTrainingEventInfo]]
        """
        return self._training_events
    
    @training_events.setter
    def training_events(self,value: Optional[List[user_training_event_info.UserTrainingEventInfo]] = None) -> None:
        """
        Sets the trainingEvents property value. List of training events of a user in the attack simulation and training campaign.
        Args:
            value: Value to set for the trainingEvents property.
        """
        self._training_events = value
    

