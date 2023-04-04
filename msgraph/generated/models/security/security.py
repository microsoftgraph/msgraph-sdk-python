from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert, cases_root, incident, triggers_root, trigger_types_root
    from .. import alert, attack_simulation_root, entity, secure_score, secure_score_control_profile

from .. import entity

class Security(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Security and sets the default values.
        """
        super().__init__()
        # The alerts property
        self._alerts: Optional[List[alert.Alert]] = None
        # A collection of alerts in Microsoft 365 Defender.
        self._alerts_v2: Optional[List[alert.Alert]] = None
        # The attackSimulation property
        self._attack_simulation: Optional[attack_simulation_root.AttackSimulationRoot] = None
        # The cases property
        self._cases: Optional[cases_root.CasesRoot] = None
        # A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        self._incidents: Optional[List[incident.Incident]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The secureScoreControlProfiles property
        self._secure_score_control_profiles: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None
        # The secureScores property
        self._secure_scores: Optional[List[secure_score.SecureScore]] = None
        # The triggerTypes property
        self._trigger_types: Optional[trigger_types_root.TriggerTypesRoot] = None
        # The triggers property
        self._triggers: Optional[triggers_root.TriggersRoot] = None
    
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
    def alerts_v2(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts_v2 property value. A collection of alerts in Microsoft 365 Defender.
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts_v2
    
    @alerts_v2.setter
    def alerts_v2(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts_v2 property value. A collection of alerts in Microsoft 365 Defender.
        Args:
            value: Value to set for the alerts_v2 property.
        """
        self._alerts_v2 = value
    
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
            value: Value to set for the attack_simulation property.
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
        from . import alert, cases_root, incident, triggers_root, trigger_types_root
        from .. import alert, attack_simulation_root, entity, secure_score, secure_score_control_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(alert.Alert)),
            "alerts_v2": lambda n : setattr(self, 'alerts_v2', n.get_collection_of_object_values(alert.Alert)),
            "attackSimulation": lambda n : setattr(self, 'attack_simulation', n.get_object_value(attack_simulation_root.AttackSimulationRoot)),
            "cases": lambda n : setattr(self, 'cases', n.get_object_value(cases_root.CasesRoot)),
            "incidents": lambda n : setattr(self, 'incidents', n.get_collection_of_object_values(incident.Incident)),
            "secureScores": lambda n : setattr(self, 'secure_scores', n.get_collection_of_object_values(secure_score.SecureScore)),
            "secureScoreControlProfiles": lambda n : setattr(self, 'secure_score_control_profiles', n.get_collection_of_object_values(secure_score_control_profile.SecureScoreControlProfile)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_object_value(triggers_root.TriggersRoot)),
            "triggerTypes": lambda n : setattr(self, 'trigger_types', n.get_object_value(trigger_types_root.TriggerTypesRoot)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incidents(self,) -> Optional[List[incident.Incident]]:
        """
        Gets the incidents property value. A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        Returns: Optional[List[incident.Incident]]
        """
        return self._incidents
    
    @incidents.setter
    def incidents(self,value: Optional[List[incident.Incident]] = None) -> None:
        """
        Sets the incidents property value. A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
        Args:
            value: Value to set for the incidents property.
        """
        self._incidents = value
    
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
            value: Value to set for the secure_score_control_profiles property.
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
            value: Value to set for the secure_scores property.
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
        writer.write_collection_of_object_values("alerts_v2", self.alerts_v2)
        writer.write_object_value("attackSimulation", self.attack_simulation)
        writer.write_object_value("cases", self.cases)
        writer.write_collection_of_object_values("incidents", self.incidents)
        writer.write_collection_of_object_values("secureScores", self.secure_scores)
        writer.write_collection_of_object_values("secureScoreControlProfiles", self.secure_score_control_profiles)
        writer.write_object_value("triggers", self.triggers)
        writer.write_object_value("triggerTypes", self.trigger_types)
    
    @property
    def trigger_types(self,) -> Optional[trigger_types_root.TriggerTypesRoot]:
        """
        Gets the triggerTypes property value. The triggerTypes property
        Returns: Optional[trigger_types_root.TriggerTypesRoot]
        """
        return self._trigger_types
    
    @trigger_types.setter
    def trigger_types(self,value: Optional[trigger_types_root.TriggerTypesRoot] = None) -> None:
        """
        Sets the triggerTypes property value. The triggerTypes property
        Args:
            value: Value to set for the trigger_types property.
        """
        self._trigger_types = value
    
    @property
    def triggers(self,) -> Optional[triggers_root.TriggersRoot]:
        """
        Gets the triggers property value. The triggers property
        Returns: Optional[triggers_root.TriggersRoot]
        """
        return self._triggers
    
    @triggers.setter
    def triggers(self,value: Optional[triggers_root.TriggersRoot] = None) -> None:
        """
        Sets the triggers property value. The triggers property
        Args:
            value: Value to set for the triggers property.
        """
        self._triggers = value
    

