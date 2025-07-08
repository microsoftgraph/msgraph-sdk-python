from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..alert import Alert
    from ..attack_simulation_root import AttackSimulationRoot
    from ..entity import Entity
    from ..secure_score import SecureScore
    from ..secure_score_control_profile import SecureScoreControlProfile
    from ..subject_rights_request import SubjectRightsRequest
    from ..tenant_data_security_and_governance import TenantDataSecurityAndGovernance
    from .alert import Alert
    from .cases_root import CasesRoot
    from .identity_container import IdentityContainer
    from .incident import Incident
    from .labels_root import LabelsRoot
    from .threat_intelligence import ThreatIntelligence
    from .triggers_root import TriggersRoot
    from .trigger_types_root import TriggerTypesRoot

from ..entity import Entity

@dataclass
class Security(Entity, Parsable):
    # The alerts property
    alerts: Optional[list[Alert]] = None
    # A collection of alerts in Microsoft 365 Defender.
    alerts_v2: Optional[list[Alert]] = None
    # The attackSimulation property
    attack_simulation: Optional[AttackSimulationRoot] = None
    # The cases property
    cases: Optional[CasesRoot] = None
    # The dataSecurityAndGovernance property
    data_security_and_governance: Optional[TenantDataSecurityAndGovernance] = None
    # A container for security identities APIs.
    identities: Optional[IdentityContainer] = None
    # A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack.
    incidents: Optional[list[Incident]] = None
    # The labels property
    labels: Optional[LabelsRoot] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The secureScoreControlProfiles property
    secure_score_control_profiles: Optional[list[SecureScoreControlProfile]] = None
    # The secureScores property
    secure_scores: Optional[list[SecureScore]] = None
    # The subjectRightsRequests property
    subject_rights_requests: Optional[list[SubjectRightsRequest]] = None
    # The threatIntelligence property
    threat_intelligence: Optional[ThreatIntelligence] = None
    # The triggerTypes property
    trigger_types: Optional[TriggerTypesRoot] = None
    # The triggers property
    triggers: Optional[TriggersRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Security
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Security()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..alert import Alert
        from ..attack_simulation_root import AttackSimulationRoot
        from ..entity import Entity
        from ..secure_score import SecureScore
        from ..secure_score_control_profile import SecureScoreControlProfile
        from ..subject_rights_request import SubjectRightsRequest
        from ..tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .alert import Alert
        from .cases_root import CasesRoot
        from .identity_container import IdentityContainer
        from .incident import Incident
        from .labels_root import LabelsRoot
        from .threat_intelligence import ThreatIntelligence
        from .triggers_root import TriggersRoot
        from .trigger_types_root import TriggerTypesRoot

        from ..alert import Alert
        from ..attack_simulation_root import AttackSimulationRoot
        from ..entity import Entity
        from ..secure_score import SecureScore
        from ..secure_score_control_profile import SecureScoreControlProfile
        from ..subject_rights_request import SubjectRightsRequest
        from ..tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .alert import Alert
        from .cases_root import CasesRoot
        from .identity_container import IdentityContainer
        from .incident import Incident
        from .labels_root import LabelsRoot
        from .threat_intelligence import ThreatIntelligence
        from .triggers_root import TriggersRoot
        from .trigger_types_root import TriggerTypesRoot

        fields: dict[str, Callable[[Any], None]] = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(Alert)),
            "alerts_v2": lambda n : setattr(self, 'alerts_v2', n.get_collection_of_object_values(Alert)),
            "attackSimulation": lambda n : setattr(self, 'attack_simulation', n.get_object_value(AttackSimulationRoot)),
            "cases": lambda n : setattr(self, 'cases', n.get_object_value(CasesRoot)),
            "dataSecurityAndGovernance": lambda n : setattr(self, 'data_security_and_governance', n.get_object_value(TenantDataSecurityAndGovernance)),
            "identities": lambda n : setattr(self, 'identities', n.get_object_value(IdentityContainer)),
            "incidents": lambda n : setattr(self, 'incidents', n.get_collection_of_object_values(Incident)),
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(LabelsRoot)),
            "secureScoreControlProfiles": lambda n : setattr(self, 'secure_score_control_profiles', n.get_collection_of_object_values(SecureScoreControlProfile)),
            "secureScores": lambda n : setattr(self, 'secure_scores', n.get_collection_of_object_values(SecureScore)),
            "subjectRightsRequests": lambda n : setattr(self, 'subject_rights_requests', n.get_collection_of_object_values(SubjectRightsRequest)),
            "threatIntelligence": lambda n : setattr(self, 'threat_intelligence', n.get_object_value(ThreatIntelligence)),
            "triggerTypes": lambda n : setattr(self, 'trigger_types', n.get_object_value(TriggerTypesRoot)),
            "triggers": lambda n : setattr(self, 'triggers', n.get_object_value(TriggersRoot)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("alerts", self.alerts)
        writer.write_collection_of_object_values("alerts_v2", self.alerts_v2)
        writer.write_object_value("attackSimulation", self.attack_simulation)
        writer.write_object_value("cases", self.cases)
        writer.write_object_value("dataSecurityAndGovernance", self.data_security_and_governance)
        writer.write_object_value("identities", self.identities)
        writer.write_collection_of_object_values("incidents", self.incidents)
        writer.write_object_value("labels", self.labels)
        writer.write_collection_of_object_values("secureScoreControlProfiles", self.secure_score_control_profiles)
        writer.write_collection_of_object_values("secureScores", self.secure_scores)
        writer.write_collection_of_object_values("subjectRightsRequests", self.subject_rights_requests)
        writer.write_object_value("threatIntelligence", self.threat_intelligence)
        writer.write_object_value("triggerTypes", self.trigger_types)
        writer.write_object_value("triggers", self.triggers)
    

