from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_user = lazy_import('msgraph.generated.models.attack_simulation_user')
user_training_status_info = lazy_import('msgraph.generated.models.user_training_status_info')

class AttackSimulationTrainingUserCoverage(AdditionalDataHolder, Parsable):
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
    def attack_simulation_user(self,) -> Optional[attack_simulation_user.AttackSimulationUser]:
        """
        Gets the attackSimulationUser property value. User in an attack simulation and training campaign.
        Returns: Optional[attack_simulation_user.AttackSimulationUser]
        """
        return self._attack_simulation_user
    
    @attack_simulation_user.setter
    def attack_simulation_user(self,value: Optional[attack_simulation_user.AttackSimulationUser] = None) -> None:
        """
        Sets the attackSimulationUser property value. User in an attack simulation and training campaign.
        Args:
            value: Value to set for the attackSimulationUser property.
        """
        self._attack_simulation_user = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attackSimulationTrainingUserCoverage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # User in an attack simulation and training campaign.
        self._attack_simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # List of assigned trainings and their statuses for the user.
        self._user_trainings: Optional[List[user_training_status_info.UserTrainingStatusInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationTrainingUserCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationTrainingUserCoverage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationTrainingUserCoverage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_simulation_user": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_trainings": lambda n : setattr(self, 'user_trainings', n.get_collection_of_object_values(user_training_status_info.UserTrainingStatusInfo)),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("attackSimulationUser", self.attack_simulation_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userTrainings", self.user_trainings)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_trainings(self,) -> Optional[List[user_training_status_info.UserTrainingStatusInfo]]:
        """
        Gets the userTrainings property value. List of assigned trainings and their statuses for the user.
        Returns: Optional[List[user_training_status_info.UserTrainingStatusInfo]]
        """
        return self._user_trainings
    
    @user_trainings.setter
    def user_trainings(self,value: Optional[List[user_training_status_info.UserTrainingStatusInfo]] = None) -> None:
        """
        Sets the userTrainings property value. List of assigned trainings and their statuses for the user.
        Args:
            value: Value to set for the userTrainings property.
        """
        self._user_trainings = value
    

