from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert, cases_root, incident, triggers_root, trigger_types_root
    from .. import alert, attack_simulation_root, entity, secure_score, secure_score_control_profile

from .. import entity

@dataclass
class Security(entity.Entity):
    # The alerts property
    alerts: Optional[List[alert.Alert]] = None
    # A collection of alerts in Microsoft 365 Defender.
    alerts_v2: Optional[List[alert.Alert]] = None
    # The attackSimulation property
    attack_simulation: Optional[attack_simulation_root.AttackSimulationRoot] = None
    # The cases property
    cases: Optional[cases_root.CasesRoot] = None
    # A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
    incidents: Optional[List[incident.Incident]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The secureScoreControlProfiles property
    secure_score_control_profiles: Optional[List[secure_score_control_profile.SecureScoreControlProfile]] = None
    # The secureScores property
    secure_scores: Optional[List[secure_score.SecureScore]] = None
    # The triggerTypes property
    trigger_types: Optional[trigger_types_root.TriggerTypesRoot] = None
    # The triggers property
    triggers: Optional[triggers_root.TriggersRoot] = None
    
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
    

