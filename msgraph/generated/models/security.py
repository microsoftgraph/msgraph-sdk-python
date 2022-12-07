from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert = lazy_import('msgraph.generated.models.alert')
attack_simulation_root = lazy_import('msgraph.generated.models.attack_simulation_root')
entity = lazy_import('msgraph.generated.models.entity')
secure_score = lazy_import('msgraph.generated.models.secure_score')
secure_score_control_profile = lazy_import('msgraph.generated.models.secure_score_control_profile')
cases_root = lazy_import('msgraph.generated.models.security.cases_root')

class Security(entity.Entity):
    @property
    def alerts(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts property value. The alerts property
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts property value. The alerts property
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @property
    def attack_simulation(self,) -> Optional[attack_simulation_root.AttackSimulationRoot]:
        """
        Gets the attackSimulation property value. The attackSimulation property
        Returns: Optional[attack_simulation_root.AttackSimulationRoot]
        """
        return self._attack_simulation
    
    @attack_simulation.setter
    def attack_simulation(self,value: Optional[attack_simulation_root.AttackSimulationRoot] = None) -> None:
        """
        Sets the attackSimulation property value. The attackSimulation property
        Args:
            value: Value to set for the attackSimulation property.
        """
        self._attack_simulation = value
    
    @property
    def cases(self,) -> Optional[cases_root.CasesRoot]:
        """
        Gets the cases property value. The cases property
        Returns: Optional[cases_root.CasesRoot]
        """
        return self._cases
    
    @cases.setter
    def cases(self,value: Optional[cases_root.CasesRoot] = None) -> None:
        """
        Sets the cases property value. The cases property
        Args:
            value: Value to set for the cases property.
        """
        self._cases = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Security and sets the default values.
        """
        super().__init__()
        # The alerts property
        self._alerts: Optional[List[alert.Alert]] = None
        # The attackSimulation property
        self._attack_simulation: Optional[attack_simulation_root.AttackSimulationRoot] = None
        # The cases property
        self._cases: Optional[cases_root.CasesRoot] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The secureScoreControlProfiles property
        self._secure_score_control_profiles: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None
        # The secureScores property
        self._secure_scores: Optional[List[secure_score.SecureScore]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Security
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Security()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(alert.Alert)),
            "attack_simulation": lambda n : setattr(self, 'attack_simulation', n.get_object_value(attack_simulation_root.AttackSimulationRoot)),
            "cases": lambda n : setattr(self, 'cases', n.get_object_value(cases_root.CasesRoot)),
            "secure_score_control_profiles": lambda n : setattr(self, 'secure_score_control_profiles', n.get_collection_of_object_values(secure_score_control_profile.SecureScoreControlProfile)),
            "secure_scores": lambda n : setattr(self, 'secure_scores', n.get_collection_of_object_values(secure_score.SecureScore)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def secure_score_control_profiles(self,) -> Optional[List[secure_score_control_profile.SecureScoreControlProfile]]:
        """
        Gets the secureScoreControlProfiles property value. The secureScoreControlProfiles property
        Returns: Optional[List[secure_score_control_profile.SecureScoreControlProfile]]
        """
        return self._secure_score_control_profiles
    
    @secure_score_control_profiles.setter
    def secure_score_control_profiles(self,value: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None) -> None:
        """
        Sets the secureScoreControlProfiles property value. The secureScoreControlProfiles property
        Args:
            value: Value to set for the secureScoreControlProfiles property.
        """
        self._secure_score_control_profiles = value
    
    @property
    def secure_scores(self,) -> Optional[List[secure_score.SecureScore]]:
        """
        Gets the secureScores property value. The secureScores property
        Returns: Optional[List[secure_score.SecureScore]]
        """
        return self._secure_scores
    
    @secure_scores.setter
    def secure_scores(self,value: Optional[List[secure_score.SecureScore]] = None) -> None:
        """
        Sets the secureScores property value. The secureScores property
        Args:
            value: Value to set for the secureScores property.
        """
        self._secure_scores = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_object_value("attackSimulation", self.attack_simulation)
        writer.write_object_value("cases", self.cases)
        writer.write_collection_of_object_values("secureScoreControlProfiles", self.secure_score_control_profiles)
        writer.write_collection_of_object_values("secureScores", self.secure_scores)
    

