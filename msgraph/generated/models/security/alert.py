from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert_classification = lazy_import('msgraph.generated.models.security.alert_classification')
alert_comment = lazy_import('msgraph.generated.models.security.alert_comment')
alert_determination = lazy_import('msgraph.generated.models.security.alert_determination')
alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
alert_severity = lazy_import('msgraph.generated.models.security.alert_severity')
alert_status = lazy_import('msgraph.generated.models.security.alert_status')
detection_source = lazy_import('msgraph.generated.models.security.detection_source')
service_source = lazy_import('msgraph.generated.models.security.service_source')

class Alert(entity.Entity):
    @property
    def actor_display_name(self,) -> Optional[str]:
        """
        Gets the actorDisplayName property value. The adversary or activity group that is associated with this alert.
        Returns: Optional[str]
        """
        return self._actor_display_name
    
    @actor_display_name.setter
    def actor_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actorDisplayName property value. The adversary or activity group that is associated with this alert.
        Args:
            value: Value to set for the actorDisplayName property.
        """
        self._actor_display_name = value
    
    @property
    def alert_web_url(self,) -> Optional[str]:
        """
        Gets the alertWebUrl property value. URL for the alert page in the Microsoft 365 Defender portal.
        Returns: Optional[str]
        """
        return self._alert_web_url
    
    @alert_web_url.setter
    def alert_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the alertWebUrl property value. URL for the alert page in the Microsoft 365 Defender portal.
        Args:
            value: Value to set for the alertWebUrl property.
        """
        self._alert_web_url = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. Owner of the alert, or null if no owner is assigned.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. Owner of the alert, or null if no owner is assigned.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. The attack kill-chain category that the alert belongs to. Aligned with the MITRE ATT&CK framework.
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. The attack kill-chain category that the alert belongs to. Aligned with the MITRE ATT&CK framework.
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def classification(self,) -> Optional[alert_classification.AlertClassification]:
        """
        Gets the classification property value. Specifies whether the alert represents a true threat. Possible values are: unknown, falsePositive, truePositive, benignPositive, unknownFutureValue.
        Returns: Optional[alert_classification.AlertClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[alert_classification.AlertClassification] = None) -> None:
        """
        Sets the classification property value. Specifies whether the alert represents a true threat. Possible values are: unknown, falsePositive, truePositive, benignPositive, unknownFutureValue.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    @property
    def comments(self,) -> Optional[List[alert_comment.AlertComment]]:
        """
        Gets the comments property value. Array of comments created by the Security Operations (SecOps) team during the alert management process.
        Returns: Optional[List[alert_comment.AlertComment]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[alert_comment.AlertComment]] = None) -> None:
        """
        Sets the comments property value. Array of comments created by the Security Operations (SecOps) team during the alert management process.
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alert and sets the default values.
        """
        super().__init__()
        # The adversary or activity group that is associated with this alert.
        self._actor_display_name: Optional[str] = None
        # URL for the alert page in the Microsoft 365 Defender portal.
        self._alert_web_url: Optional[str] = None
        # Owner of the alert, or null if no owner is assigned.
        self._assigned_to: Optional[str] = None
        # The attack kill-chain category that the alert belongs to. Aligned with the MITRE ATT&CK framework.
        self._category: Optional[str] = None
        # Specifies whether the alert represents a true threat. Possible values are: unknown, falsePositive, truePositive, benignPositive, unknownFutureValue.
        self._classification: Optional[alert_classification.AlertClassification] = None
        # Array of comments created by the Security Operations (SecOps) team during the alert management process.
        self._comments: Optional[List[alert_comment.AlertComment]] = None
        # Time when Microsoft 365 Defender created the alert.
        self._created_date_time: Optional[datetime] = None
        # String value describing each alert.
        self._description: Optional[str] = None
        # Detection technology or sensor that identified the notable component or activity.
        self._detection_source: Optional[detection_source.DetectionSource] = None
        # The ID of the detector that triggered the alert.
        self._detector_id: Optional[str] = None
        # Specifies the result of the investigation, whether the alert represents a true attack and if so, the nature of the attack. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        self._determination: Optional[alert_determination.AlertDetermination] = None
        # Collection of evidence related to the alert.
        self._evidence: Optional[List[alert_evidence.AlertEvidence]] = None
        # The earliest activity associated with the alert.
        self._first_activity_date_time: Optional[datetime] = None
        # Unique identifier to represent the incident this alert resource is associated with.
        self._incident_id: Optional[str] = None
        # URL for the incident page in the Microsoft 365 Defender portal.
        self._incident_web_url: Optional[str] = None
        # The oldest activity associated with the alert.
        self._last_activity_date_time: Optional[datetime] = None
        # Time when the alert was last updated at Microsoft 365 Defender.
        self._last_update_date_time: Optional[datetime] = None
        # The attack techniques, as aligned with the MITRE ATT&CK framework.
        self._mitre_techniques: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ID of the alert as it appears in the security provider product that generated the alert.
        self._provider_alert_id: Optional[str] = None
        # Recommended response and remediation actions to take in the event this alert was generated.
        self._recommended_actions: Optional[str] = None
        # Time when the alert was resolved.
        self._resolved_date_time: Optional[datetime] = None
        # The serviceSource property
        self._service_source: Optional[service_source.ServiceSource] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # The status property
        self._status: Optional[alert_status.AlertStatus] = None
        # The Azure Active Directory tenant the alert was created in.
        self._tenant_id: Optional[str] = None
        # The threat associated with this alert.
        self._threat_display_name: Optional[str] = None
        # Threat family associated with this alert.
        self._threat_family_name: Optional[str] = None
        # Brief identifying string value describing the alert.
        self._title: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time when Microsoft 365 Defender created the alert.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time when Microsoft 365 Defender created the alert.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Alert()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. String value describing each alert.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. String value describing each alert.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def detection_source(self,) -> Optional[detection_source.DetectionSource]:
        """
        Gets the detectionSource property value. Detection technology or sensor that identified the notable component or activity.
        Returns: Optional[detection_source.DetectionSource]
        """
        return self._detection_source
    
    @detection_source.setter
    def detection_source(self,value: Optional[detection_source.DetectionSource] = None) -> None:
        """
        Sets the detectionSource property value. Detection technology or sensor that identified the notable component or activity.
        Args:
            value: Value to set for the detectionSource property.
        """
        self._detection_source = value
    
    @property
    def detector_id(self,) -> Optional[str]:
        """
        Gets the detectorId property value. The ID of the detector that triggered the alert.
        Returns: Optional[str]
        """
        return self._detector_id
    
    @detector_id.setter
    def detector_id(self,value: Optional[str] = None) -> None:
        """
        Sets the detectorId property value. The ID of the detector that triggered the alert.
        Args:
            value: Value to set for the detectorId property.
        """
        self._detector_id = value
    
    @property
    def determination(self,) -> Optional[alert_determination.AlertDetermination]:
        """
        Gets the determination property value. Specifies the result of the investigation, whether the alert represents a true attack and if so, the nature of the attack. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Returns: Optional[alert_determination.AlertDetermination]
        """
        return self._determination
    
    @determination.setter
    def determination(self,value: Optional[alert_determination.AlertDetermination] = None) -> None:
        """
        Sets the determination property value. Specifies the result of the investigation, whether the alert represents a true attack and if so, the nature of the attack. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Args:
            value: Value to set for the determination property.
        """
        self._determination = value
    
    @property
    def evidence(self,) -> Optional[List[alert_evidence.AlertEvidence]]:
        """
        Gets the evidence property value. Collection of evidence related to the alert.
        Returns: Optional[List[alert_evidence.AlertEvidence]]
        """
        return self._evidence
    
    @evidence.setter
    def evidence(self,value: Optional[List[alert_evidence.AlertEvidence]] = None) -> None:
        """
        Sets the evidence property value. Collection of evidence related to the alert.
        Args:
            value: Value to set for the evidence property.
        """
        self._evidence = value
    
    @property
    def first_activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the firstActivityDateTime property value. The earliest activity associated with the alert.
        Returns: Optional[datetime]
        """
        return self._first_activity_date_time
    
    @first_activity_date_time.setter
    def first_activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the firstActivityDateTime property value. The earliest activity associated with the alert.
        Args:
            value: Value to set for the firstActivityDateTime property.
        """
        self._first_activity_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "actor_display_name": lambda n : setattr(self, 'actor_display_name', n.get_str_value()),
            "alert_web_url": lambda n : setattr(self, 'alert_web_url', n.get_str_value()),
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(alert_classification.AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(alert_comment.AlertComment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detection_source": lambda n : setattr(self, 'detection_source', n.get_enum_value(detection_source.DetectionSource)),
            "detector_id": lambda n : setattr(self, 'detector_id', n.get_str_value()),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(alert_determination.AlertDetermination)),
            "evidence": lambda n : setattr(self, 'evidence', n.get_collection_of_object_values(alert_evidence.AlertEvidence)),
            "first_activity_date_time": lambda n : setattr(self, 'first_activity_date_time', n.get_datetime_value()),
            "incident_id": lambda n : setattr(self, 'incident_id', n.get_str_value()),
            "incident_web_url": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "last_activity_date_time": lambda n : setattr(self, 'last_activity_date_time', n.get_datetime_value()),
            "last_update_date_time": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "mitre_techniques": lambda n : setattr(self, 'mitre_techniques', n.get_collection_of_primitive_values(str)),
            "provider_alert_id": lambda n : setattr(self, 'provider_alert_id', n.get_str_value()),
            "recommended_actions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "resolved_date_time": lambda n : setattr(self, 'resolved_date_time', n.get_datetime_value()),
            "service_source": lambda n : setattr(self, 'service_source', n.get_enum_value(service_source.ServiceSource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "threat_display_name": lambda n : setattr(self, 'threat_display_name', n.get_str_value()),
            "threat_family_name": lambda n : setattr(self, 'threat_family_name', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incident_id(self,) -> Optional[str]:
        """
        Gets the incidentId property value. Unique identifier to represent the incident this alert resource is associated with.
        Returns: Optional[str]
        """
        return self._incident_id
    
    @incident_id.setter
    def incident_id(self,value: Optional[str] = None) -> None:
        """
        Sets the incidentId property value. Unique identifier to represent the incident this alert resource is associated with.
        Args:
            value: Value to set for the incidentId property.
        """
        self._incident_id = value
    
    @property
    def incident_web_url(self,) -> Optional[str]:
        """
        Gets the incidentWebUrl property value. URL for the incident page in the Microsoft 365 Defender portal.
        Returns: Optional[str]
        """
        return self._incident_web_url
    
    @incident_web_url.setter
    def incident_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the incidentWebUrl property value. URL for the incident page in the Microsoft 365 Defender portal.
        Args:
            value: Value to set for the incidentWebUrl property.
        """
        self._incident_web_url = value
    
    @property
    def last_activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActivityDateTime property value. The oldest activity associated with the alert.
        Returns: Optional[datetime]
        """
        return self._last_activity_date_time
    
    @last_activity_date_time.setter
    def last_activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActivityDateTime property value. The oldest activity associated with the alert.
        Args:
            value: Value to set for the lastActivityDateTime property.
        """
        self._last_activity_date_time = value
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. Time when the alert was last updated at Microsoft 365 Defender.
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. Time when the alert was last updated at Microsoft 365 Defender.
        Args:
            value: Value to set for the lastUpdateDateTime property.
        """
        self._last_update_date_time = value
    
    @property
    def mitre_techniques(self,) -> Optional[List[str]]:
        """
        Gets the mitreTechniques property value. The attack techniques, as aligned with the MITRE ATT&CK framework.
        Returns: Optional[List[str]]
        """
        return self._mitre_techniques
    
    @mitre_techniques.setter
    def mitre_techniques(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the mitreTechniques property value. The attack techniques, as aligned with the MITRE ATT&CK framework.
        Args:
            value: Value to set for the mitreTechniques property.
        """
        self._mitre_techniques = value
    
    @property
    def provider_alert_id(self,) -> Optional[str]:
        """
        Gets the providerAlertId property value. The ID of the alert as it appears in the security provider product that generated the alert.
        Returns: Optional[str]
        """
        return self._provider_alert_id
    
    @provider_alert_id.setter
    def provider_alert_id(self,value: Optional[str] = None) -> None:
        """
        Sets the providerAlertId property value. The ID of the alert as it appears in the security provider product that generated the alert.
        Args:
            value: Value to set for the providerAlertId property.
        """
        self._provider_alert_id = value
    
    @property
    def recommended_actions(self,) -> Optional[str]:
        """
        Gets the recommendedActions property value. Recommended response and remediation actions to take in the event this alert was generated.
        Returns: Optional[str]
        """
        return self._recommended_actions
    
    @recommended_actions.setter
    def recommended_actions(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedActions property value. Recommended response and remediation actions to take in the event this alert was generated.
        Args:
            value: Value to set for the recommendedActions property.
        """
        self._recommended_actions = value
    
    @property
    def resolved_date_time(self,) -> Optional[datetime]:
        """
        Gets the resolvedDateTime property value. Time when the alert was resolved.
        Returns: Optional[datetime]
        """
        return self._resolved_date_time
    
    @resolved_date_time.setter
    def resolved_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the resolvedDateTime property value. Time when the alert was resolved.
        Args:
            value: Value to set for the resolvedDateTime property.
        """
        self._resolved_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actorDisplayName", self.actor_display_name)
        writer.write_str_value("alertWebUrl", self.alert_web_url)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("category", self.category)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("detectionSource", self.detection_source)
        writer.write_str_value("detectorId", self.detector_id)
        writer.write_enum_value("determination", self.determination)
        writer.write_collection_of_object_values("evidence", self.evidence)
        writer.write_datetime_value("firstActivityDateTime", self.first_activity_date_time)
        writer.write_str_value("incidentId", self.incident_id)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_datetime_value("lastActivityDateTime", self.last_activity_date_time)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_collection_of_primitive_values("mitreTechniques", self.mitre_techniques)
        writer.write_str_value("providerAlertId", self.provider_alert_id)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_datetime_value("resolvedDateTime", self.resolved_date_time)
        writer.write_enum_value("serviceSource", self.service_source)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("threatDisplayName", self.threat_display_name)
        writer.write_str_value("threatFamilyName", self.threat_family_name)
        writer.write_str_value("title", self.title)
    
    @property
    def service_source(self,) -> Optional[service_source.ServiceSource]:
        """
        Gets the serviceSource property value. The serviceSource property
        Returns: Optional[service_source.ServiceSource]
        """
        return self._service_source
    
    @service_source.setter
    def service_source(self,value: Optional[service_source.ServiceSource] = None) -> None:
        """
        Sets the serviceSource property value. The serviceSource property
        Args:
            value: Value to set for the serviceSource property.
        """
        self._service_source = value
    
    @property
    def severity(self,) -> Optional[alert_severity.AlertSeverity]:
        """
        Gets the severity property value. The severity property
        Returns: Optional[alert_severity.AlertSeverity]
        """
        return self._severity
    
    @severity.setter
    def severity(self,value: Optional[alert_severity.AlertSeverity] = None) -> None:
        """
        Sets the severity property value. The severity property
        Args:
            value: Value to set for the severity property.
        """
        self._severity = value
    
    @property
    def status(self,) -> Optional[alert_status.AlertStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[alert_status.AlertStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[alert_status.AlertStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant the alert was created in.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant the alert was created in.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def threat_display_name(self,) -> Optional[str]:
        """
        Gets the threatDisplayName property value. The threat associated with this alert.
        Returns: Optional[str]
        """
        return self._threat_display_name
    
    @threat_display_name.setter
    def threat_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the threatDisplayName property value. The threat associated with this alert.
        Args:
            value: Value to set for the threatDisplayName property.
        """
        self._threat_display_name = value
    
    @property
    def threat_family_name(self,) -> Optional[str]:
        """
        Gets the threatFamilyName property value. Threat family associated with this alert.
        Returns: Optional[str]
        """
        return self._threat_family_name
    
    @threat_family_name.setter
    def threat_family_name(self,value: Optional[str] = None) -> None:
        """
        Sets the threatFamilyName property value. Threat family associated with this alert.
        Args:
            value: Value to set for the threatFamilyName property.
        """
        self._threat_family_name = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Brief identifying string value describing the alert.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Brief identifying string value describing the alert.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

