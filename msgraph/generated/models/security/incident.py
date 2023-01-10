from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
alert = lazy_import('msgraph.generated.models.security.alert')
alert_classification = lazy_import('msgraph.generated.models.security.alert_classification')
alert_comment = lazy_import('msgraph.generated.models.security.alert_comment')
alert_determination = lazy_import('msgraph.generated.models.security.alert_determination')
alert_severity = lazy_import('msgraph.generated.models.security.alert_severity')
incident_status = lazy_import('msgraph.generated.models.security.incident_status')

class Incident(entity.Entity):
    @property
    def alerts(self,) -> Optional[List[alert.Alert]]:
        """
        Gets the alerts property value. The list of related alerts. Supports $expand.
        Returns: Optional[List[alert.Alert]]
        """
        return self._alerts
    
    @alerts.setter
    def alerts(self,value: Optional[List[alert.Alert]] = None) -> None:
        """
        Sets the alerts property value. The list of related alerts. Supports $expand.
        Args:
            value: Value to set for the alerts property.
        """
        self._alerts = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. Owner of the incident, or null if no owner is assigned. Free editable text.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. Owner of the incident, or null if no owner is assigned. Free editable text.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def classification(self,) -> Optional[alert_classification.AlertClassification]:
        """
        Gets the classification property value. The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        Returns: Optional[alert_classification.AlertClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[alert_classification.AlertClassification] = None) -> None:
        """
        Sets the classification property value. The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    @property
    def comments(self,) -> Optional[List[alert_comment.AlertComment]]:
        """
        Gets the comments property value. Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        Returns: Optional[List[alert_comment.AlertComment]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[alert_comment.AlertComment]] = None) -> None:
        """
        Sets the comments property value. Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new incident and sets the default values.
        """
        super().__init__()
        # The list of related alerts. Supports $expand.
        self._alerts: Optional[List[alert.Alert]] = None
        # Owner of the incident, or null if no owner is assigned. Free editable text.
        self._assigned_to: Optional[str] = None
        # The specification for the incident. Possible values are: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.
        self._classification: Optional[alert_classification.AlertClassification] = None
        # Array of comments created by the Security Operations (SecOps) team when the incident is managed.
        self._comments: Optional[List[alert_comment.AlertComment]] = None
        # Time when the incident was first created.
        self._created_date_time: Optional[datetime] = None
        # Array of custom tags associated with an incident.
        self._custom_tags: Optional[List[str]] = None
        # Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        self._determination: Optional[alert_determination.AlertDetermination] = None
        # The incident name.
        self._display_name: Optional[str] = None
        # The URL for the incident page in the Microsoft 365 Defender portal.
        self._incident_web_url: Optional[str] = None
        # Time when the incident was last updated.
        self._last_update_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        self._redirect_incident_id: Optional[str] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # The status property
        self._status: Optional[incident_status.IncidentStatus] = None
        # The Azure Active Directory tenant in which the alert was created.
        self._tenant_id: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time when the incident was first created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time when the incident was first created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Incident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Incident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Incident()
    
    @property
    def custom_tags(self,) -> Optional[List[str]]:
        """
        Gets the customTags property value. Array of custom tags associated with an incident.
        Returns: Optional[List[str]]
        """
        return self._custom_tags
    
    @custom_tags.setter
    def custom_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the customTags property value. Array of custom tags associated with an incident.
        Args:
            value: Value to set for the customTags property.
        """
        self._custom_tags = value
    
    @property
    def determination(self,) -> Optional[alert_determination.AlertDetermination]:
        """
        Gets the determination property value. Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Returns: Optional[alert_determination.AlertDetermination]
        """
        return self._determination
    
    @determination.setter
    def determination(self,value: Optional[alert_determination.AlertDetermination] = None) -> None:
        """
        Sets the determination property value. Specifies the determination of the incident. Possible values are: unknown, apt, malware, securityPersonnel, securityTesting, unwantedSoftware, other, multiStagedAttack, compromisedUser, phishing, maliciousUserActivity, clean, insufficientData, confirmedUserActivity, lineOfBusinessApplication, unknownFutureValue.
        Args:
            value: Value to set for the determination property.
        """
        self._determination = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The incident name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The incident name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alerts": lambda n : setattr(self, 'alerts', n.get_collection_of_object_values(alert.Alert)),
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(alert_classification.AlertClassification)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(alert_comment.AlertComment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "custom_tags": lambda n : setattr(self, 'custom_tags', n.get_collection_of_primitive_values(str)),
            "determination": lambda n : setattr(self, 'determination', n.get_enum_value(alert_determination.AlertDetermination)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "incident_web_url": lambda n : setattr(self, 'incident_web_url', n.get_str_value()),
            "last_update_date_time": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "redirect_incident_id": lambda n : setattr(self, 'redirect_incident_id', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(incident_status.IncidentStatus)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incident_web_url(self,) -> Optional[str]:
        """
        Gets the incidentWebUrl property value. The URL for the incident page in the Microsoft 365 Defender portal.
        Returns: Optional[str]
        """
        return self._incident_web_url
    
    @incident_web_url.setter
    def incident_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the incidentWebUrl property value. The URL for the incident page in the Microsoft 365 Defender portal.
        Args:
            value: Value to set for the incidentWebUrl property.
        """
        self._incident_web_url = value
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. Time when the incident was last updated.
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. Time when the incident was last updated.
        Args:
            value: Value to set for the lastUpdateDateTime property.
        """
        self._last_update_date_time = value
    
    @property
    def redirect_incident_id(self,) -> Optional[str]:
        """
        Gets the redirectIncidentId property value. Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        Returns: Optional[str]
        """
        return self._redirect_incident_id
    
    @redirect_incident_id.setter
    def redirect_incident_id(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectIncidentId property value. Only populated in case an incident is grouped together with another incident, as part of the logic that processes incidents. In such a case, the status property is redirected.
        Args:
            value: Value to set for the redirectIncidentId property.
        """
        self._redirect_incident_id = value
    
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("comments", self.comments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_primitive_values("customTags", self.custom_tags)
        writer.write_enum_value("determination", self.determination)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("incidentWebUrl", self.incident_web_url)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_str_value("redirectIncidentId", self.redirect_incident_id)
        writer.write_enum_value("severity", self.severity)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
    
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
    def status(self,) -> Optional[incident_status.IncidentStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[incident_status.IncidentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[incident_status.IncidentStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant in which the alert was created.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant in which the alert was created.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

