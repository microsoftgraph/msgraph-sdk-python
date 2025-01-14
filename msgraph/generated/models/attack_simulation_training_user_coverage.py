from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_user import AttackSimulationUser
    from .user_training_status_info import UserTrainingStatusInfo

@dataclass
class AttackSimulationTrainingUserCoverage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # User in an attack simulation and training campaign.
    attack_simulation_user: Optional[AttackSimulationUser] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of assigned trainings and their statuses for the user.
    user_trainings: Optional[list[UserTrainingStatusInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttackSimulationTrainingUserCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationTrainingUserCoverage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationTrainingUserCoverage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_user import AttackSimulationUser
        from .user_training_status_info import UserTrainingStatusInfo

        from .attack_simulation_user import AttackSimulationUser
        from .user_training_status_info import UserTrainingStatusInfo

        fields: dict[str, Callable[[Any], None]] = {
            "attackSimulationUser": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userTrainings": lambda n : setattr(self, 'user_trainings', n.get_collection_of_object_values(UserTrainingStatusInfo)),
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
        writer.write_object_value("attackSimulationUser", self.attack_simulation_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("userTrainings", self.user_trainings)
        writer.write_additional_data_value(self.additional_data)
    

