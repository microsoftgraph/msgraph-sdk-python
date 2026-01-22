from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_classification import AlertClassification
    from .alert_comment import AlertComment
    from .alert_determination import AlertDetermination
    from .alert_evidence import AlertEvidence
    from .alert_severity import AlertSeverity
    from .alert_status import AlertStatus
    from .detection_source import DetectionSource
    from .dictionary import Dictionary
    from .investigation_state import InvestigationState
    from .service_source import ServiceSource

from ..entity import Entity

@dataclass
class Alert(Entity, Parsable):
    # The adversary or activity group that is associated with this alert.
    actor_display_name: Optional[str] = None
    # A collection of other alert properties, including user-defined properties. Any custom details defined in the alert, and any dynamic content in the alert details, are stored here.
    additional_data_property: Optional[Dictionary] = None
    # The ID of the policy that generated the alert, and populated when there is a specific policy that generated the alert, whether configured by a customer or a built-in policy.
    alert_policy_id: Optional[str] = None
    # URL for the Microsoft 365 Defender portal alert page.
    alert_web_url: Optional[str] = None
    # Owner of the alert, or null if no owner is assigned.
    assigned_to: Optional[str] = None
    # The attack kill-chain category that the alert belongs to. Aligned with the MITRE ATT&CK framework.
    category: Optional[str] = None
    # Specifies whether the alert represents a true threat. The possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
    classification: Optional[AlertClassification] = None
    # Array of comments created by the Security Operations (SecOps) team during the alert management process.
    comments: Optional[list[AlertComment]] = None
    # Time when Microsoft 365 Defender created the alert.
    created_date_time: Optional[datetime.datetime] = None
    # User defined custom fields with string values.
    custom_details: Optional[Dictionary] = None
    # String value describing each alert.
    description: Optional[str] = None
    # Detection technology or sensor that identified the notable component or activity.
    detection_source: Optional[DetectionSource] = None
    # The ID of the detector that triggered the alert.
    detector_id: Optional[str] = None
    # Specifies the result of the investigation, whether the alert represents a true attack and if so, the nature of the attack. The possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedAccount, phishing, maliciousUserActivity, notMalicious, notEnoughDataToValidate, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
    determination: Optional[AlertDetermination] = None
    # Collection of evidence related to the alert.
    evidence: Optional[list[AlertEvidence]] = None
    # The earliest activity associated with the alert.
    first_activity_date_time: Optional[datetime.datetime] = None
    # Unique identifier to represent the incident this alert resource is associated with.
    incident_id: Optional[str] = None
    # URL for the incident page in the Microsoft 365 Defender portal.
    incident_web_url: Optional[str] = None
    # Information on the current status of the investigation. The possible values are: unknown, terminated, successfullyRemediated, benign, failed, partiallyRemediated, running, pendingApproval, pendingResource, queued, innerFailure, preexistingAlert, unsupportedOs, unsupportedAlertType, suppressedAlert, partiallyInvestigated, terminatedByUser, terminatedBySystem, unknownFutureValue.
    investigation_state: Optional[InvestigationState] = None
    # The oldest activity associated with the alert.
    last_activity_date_time: Optional[datetime.datetime] = None
    # Time when the alert was last updated at Microsoft 365 Defender.
    last_update_date_time: Optional[datetime.datetime] = None
    # The attack techniques, as aligned with the MITRE ATT&CK framework.
    mitre_techniques: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the product which published this alert.
    product_name: Optional[str] = None
    # The ID of the alert as it appears in the security provider product that generated the alert.
    provider_alert_id: Optional[str] = None
    # Recommended response and remediation actions to take in the event this alert was generated.
    recommended_actions: Optional[str] = None
    # Time when the alert was resolved.
    resolved_date_time: Optional[datetime.datetime] = None
    # The serviceSource property
    service_source: Optional[ServiceSource] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # The status property
    status: Optional[AlertStatus] = None
    # The system tags associated with the alert.
    system_tags: Optional[list[str]] = None
    # The Microsoft Entra tenant the alert was created in.
    tenant_id: Optional[str] = None
    # The threat associated with this alert.
    threat_display_name: Optional[str] = None
    # Threat family associated with this alert.
    threat_family_name: Optional[str] = None
    # Brief identifying string value describing the alert.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_classification import AlertClassification
        from .alert_comment import AlertComment
        from .alert_determination import AlertDetermination
        from .alert_evidence import AlertEvidence
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .detection_source import DetectionSource
        from .dictionary import Dictionary
        from .investigation_state import InvestigationState
        from .service_source import ServiceSource

        from ..entity import Entity
        from .alert_classification import AlertClassification
        from .alert_comment import AlertComment
        from .alert_determination import AlertDetermination
        from .alert_evidence import AlertEvidence
        from .alert_severity import AlertSeverity
        from .alert_status import AlertStatus
        from .detection_source import DetectionSource
        from .dictionary import Dictionary
        from .investigation_state import InvestigationState
        from .service_source import ServiceSource

        fields: dict[str, Callable[[Any], None]] = {
            "actorDisplayName": lambda n : setattr(self, 'actor_display_name', n.get_str_value()),
            "additionalData": lambda n : setattr(self, 'additional_data_property', n.get_object_value(Dictionary)),
            "alertPolicyId": lambda n : setattr(self, 'alert_policy_id', n.get_str_value()),
            "alertWebUrl": lambda n : setattr(self, 'alert_web_url', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(AlertComment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customDetails": lambda n : setattr(self, 'custom_details', n.get_object_value(Dictionary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detectionSource": lambda n : setattr(self, 'detection_source', n.get_enum_value(DetectionSource)),
            "detectorId": lambda n : setattr(self, 'detector_id', n.get_str_value()),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(AlertDetermination)),
            "evidence": lambda n : setattr(self, 'evidence', n.get_collection_of_object_values(AlertEvidence)),
            "firstActivityDateTime": lambda n : setattr(self, 'first_activity_date_time', n.get_datetime_value()),
            "incidentId": lambda n : setattr(self, 'incident_id', n.get_str_value()),
            "incidentWebUrl": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "investigationState": lambda n : setattr(self, 'investigation_state', n.get_enum_value(InvestigationState)),
            "lastActivityDateTime": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "mitreTechniques": lambda n : setattr(self, 'mitre_techniques', n.get_collection_of_primitive_values(str)),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "providerAlertId": lambda n : setattr(self, 'provider_alert_id', n.get_str_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "resolvedDateTime": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "serviceSource": lambda n : setattr(self, 'service_source', n.get_enum_value(ServiceSource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AlertStatus)),
            "systemTags": lambda n : setattr(self, 'system_tags', n.get_collection_of_primitive_values(str)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "threatDisplayName": lambda n : setattr(self, 'threat_display_name', n.get_str_value()),
            "threatFamilyName": lambda n : setattr(self, 'threat_family_name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("actorDisplayName", self.actor_display_name)
        writer.write_object_value("additionalData", self.additional_data_property)
        writer.write_str_value("alertPolicyId", self.alert_policy_id)
        writer.write_str_value("alertWebUrl", self.alert_web_url)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("category", self.category)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customDetails", self.custom_details)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("detectionSource", self.detection_source)
        writer.write_str_value("detectorId", self.detector_id)
        writer.write_enum_value("determination", self.determination)
        writer.write_collection_of_object_values("evidence", self.evidence)
        writer.write_datetime_value("firstActivityDateTime", self.first_activity_date_time)
        writer.write_str_value("incidentId", self.incident_id)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_enum_value("investigationState", self.investigation_state)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_collection_of_primitive_values("mitreTechniques", self.mitre_techniques)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("providerAlertId", self.provider_alert_id)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_enum_value("serviceSource", self.service_source)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("systemTags", self.system_tags)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("threatDisplayName", self.threat_display_name)
        writer.write_str_value("threatFamilyName", self.threat_family_name)
        writer.write_str_value("title", self.title)
    

