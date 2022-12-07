from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_user = lazy_import('msgraph.generated.models.attack_simulation_user')

class AttackSimulationRepeatOffender(AdditionalDataHolder, Parsable):
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
        Gets the attackSimulationUser property value. The user in an attack simulation and training campaign.
        Returns: Optional[attack_simulation_user.AttackSimulationUser]
        """
        return self._attack_simulation_user
    
    @attack_simulation_user.setter
    def attack_simulation_user(self,value: Optional[attack_simulation_user.AttackSimulationUser] = None) -> None:
        """
        Sets the attackSimulationUser property value. The user in an attack simulation and training campaign.
        Args:
            value: Value to set for the attackSimulationUser property.
        """
        self._attack_simulation_user = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attackSimulationRepeatOffender and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The user in an attack simulation and training campaign.
        self._attack_simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of repeat offences of the user in attack simulation and training campaigns.
        self._repeat_offence_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationRepeatOffender:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRepeatOffender
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationRepeatOffender()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_simulation_user": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "repeat_offence_count": lambda n : setattr(self, 'repeat_offence_count', n.get_int_value()),
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
    
    @property
    def repeat_offence_count(self,) -> Optional[int]:
        """
        Gets the repeatOffenceCount property value. Number of repeat offences of the user in attack simulation and training campaigns.
        Returns: Optional[int]
        """
        return self._repeat_offence_count
    
    @repeat_offence_count.setter
    def repeat_offence_count(self,value: Optional[int] = None) -> None:
        """
        Sets the repeatOffenceCount property value. Number of repeat offences of the user in attack simulation and training campaigns.
        Args:
            value: Value to set for the repeatOffenceCount property.
        """
        self._repeat_offence_count = value
    
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
        writer.write_int_value("repeatOffenceCount", self.repeat_offence_count)
        writer.write_additional_data_value(self.additional_data)
    

