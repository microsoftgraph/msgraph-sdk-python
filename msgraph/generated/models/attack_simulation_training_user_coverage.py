from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attack_simulation_user, user_training_status_info

@dataclass
class AttackSimulationTrainingUserCoverage(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # User in an attack simulation and training campaign.
    attack_simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of assigned trainings and their statuses for the user.
    user_trainings: Optional[List[user_training_status_info.UserTrainingStatusInfo]] = None
    
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
        from . import attack_simulation_user, user_training_status_info

        fields: Dict[str, Callable[[Any], None]] = {
            "attackSimulationUser": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userTrainings": lambda n : setattr(self, 'user_trainings', n.get_collection_of_object_values(user_training_status_info.UserTrainingStatusInfo)),
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
        writer.write_object_value("attackSimulationUser", self.attack_simulation_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userTrainings", self.user_trainings)
        writer.write_additional_data_value(self.additional_data)
    

