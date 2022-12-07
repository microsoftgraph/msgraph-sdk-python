from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_user = lazy_import('msgraph.generated.models.attack_simulation_user')

class AttackSimulationSimulationUserCoverage(AdditionalDataHolder, Parsable):
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
    
    @property
    def click_count(self,) -> Optional[int]:
        """
        Gets the clickCount property value. Number of link clicks in the received payloads by the user in attack simulation and training campaigns.
        Returns: Optional[int]
        """
        return self._click_count
    
    @click_count.setter
    def click_count(self,value: Optional[int] = None) -> None:
        """
        Sets the clickCount property value. Number of link clicks in the received payloads by the user in attack simulation and training campaigns.
        Args:
            value: Value to set for the clickCount property.
        """
        self._click_count = value
    
    @property
    def compromised_count(self,) -> Optional[int]:
        """
        Gets the compromisedCount property value. Number of compromising actions by the user in attack simulation and training campaigns.
        Returns: Optional[int]
        """
        return self._compromised_count
    
    @compromised_count.setter
    def compromised_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compromisedCount property value. Number of compromising actions by the user in attack simulation and training campaigns.
        Args:
            value: Value to set for the compromisedCount property.
        """
        self._compromised_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new attackSimulationSimulationUserCoverage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # User in an attack simulation and training campaign.
        self._attack_simulation_user: Optional[attack_simulation_user.AttackSimulationUser] = None
        # Number of link clicks in the received payloads by the user in attack simulation and training campaigns.
        self._click_count: Optional[int] = None
        # Number of compromising actions by the user in attack simulation and training campaigns.
        self._compromised_count: Optional[int] = None
        # Date and time of the latest attack simulation and training campaign that the user was included in.
        self._latest_simulation_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of attack simulation and training campaigns that the user was included in.
        self._simulation_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationSimulationUserCoverage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationSimulationUserCoverage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationSimulationUserCoverage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attack_simulation_user": lambda n : setattr(self, 'attack_simulation_user', n.get_object_value(attack_simulation_user.AttackSimulationUser)),
            "click_count": lambda n : setattr(self, 'click_count', n.get_int_value()),
            "compromised_count": lambda n : setattr(self, 'compromised_count', n.get_int_value()),
            "latest_simulation_date_time": lambda n : setattr(self, 'latest_simulation_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "simulation_count": lambda n : setattr(self, 'simulation_count', n.get_int_value()),
        }
        return fields
    
    @property
    def latest_simulation_date_time(self,) -> Optional[datetime]:
        """
        Gets the latestSimulationDateTime property value. Date and time of the latest attack simulation and training campaign that the user was included in.
        Returns: Optional[datetime]
        """
        return self._latest_simulation_date_time
    
    @latest_simulation_date_time.setter
    def latest_simulation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the latestSimulationDateTime property value. Date and time of the latest attack simulation and training campaign that the user was included in.
        Args:
            value: Value to set for the latestSimulationDateTime property.
        """
        self._latest_simulation_date_time = value
    
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
        writer.write_int_value("clickCount", self.click_count)
        writer.write_int_value("compromisedCount", self.compromised_count)
        writer.write_datetime_value("latestSimulationDateTime", self.latest_simulation_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("simulationCount", self.simulation_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def simulation_count(self,) -> Optional[int]:
        """
        Gets the simulationCount property value. Number of attack simulation and training campaigns that the user was included in.
        Returns: Optional[int]
        """
        return self._simulation_count
    
    @simulation_count.setter
    def simulation_count(self,value: Optional[int] = None) -> None:
        """
        Sets the simulationCount property value. Number of attack simulation and training campaigns that the user was included in.
        Args:
            value: Value to set for the simulationCount property.
        """
        self._simulation_count = value
    

