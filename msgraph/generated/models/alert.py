from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_detection = lazy_import('msgraph.generated.models.alert_detection')
alert_feedback = lazy_import('msgraph.generated.models.alert_feedback')
alert_history_state = lazy_import('msgraph.generated.models.alert_history_state')
alert_severity = lazy_import('msgraph.generated.models.alert_severity')
alert_status = lazy_import('msgraph.generated.models.alert_status')
alert_trigger = lazy_import('msgraph.generated.models.alert_trigger')
cloud_app_security_state = lazy_import('msgraph.generated.models.cloud_app_security_state')
entity = lazy_import('msgraph.generated.models.entity')
file_security_state = lazy_import('msgraph.generated.models.file_security_state')
host_security_state = lazy_import('msgraph.generated.models.host_security_state')
investigation_security_state = lazy_import('msgraph.generated.models.investigation_security_state')
malware_state = lazy_import('msgraph.generated.models.malware_state')
message_security_state = lazy_import('msgraph.generated.models.message_security_state')
network_connection = lazy_import('msgraph.generated.models.network_connection')
process = lazy_import('msgraph.generated.models.process')
registry_key_state = lazy_import('msgraph.generated.models.registry_key_state')
security_resource = lazy_import('msgraph.generated.models.security_resource')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')
uri_click_security_state = lazy_import('msgraph.generated.models.uri_click_security_state')
user_security_state = lazy_import('msgraph.generated.models.user_security_state')
vulnerability_state = lazy_import('msgraph.generated.models.vulnerability_state')

class Alert(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def activity_group_name(self,) -> Optional[str]:
        """
        Gets the activityGroupName property value. Name or alias of the activity group (attacker) this alert is attributed to.
        Returns: Optional[str]
        """
        return self._activity_group_name
    
    @activity_group_name.setter
    def activity_group_name(self,value: Optional[str] = None) -> None:
        """
        Sets the activityGroupName property value. Name or alias of the activity group (attacker) this alert is attributed to.
        Args:
            value: Value to set for the activityGroupName property.
        """
        self._activity_group_name = value
    
    @property
    def alert_detections(self,) -> Optional[List[alert_detection.AlertDetection]]:
        """
        Gets the alertDetections property value. The alertDetections property
        Returns: Optional[List[alert_detection.AlertDetection]]
        """
        return self._alert_detections
    
    @alert_detections.setter
    def alert_detections(self,value: Optional[List[alert_detection.AlertDetection]] = None) -> None:
        """
        Sets the alertDetections property value. The alertDetections property
        Args:
            value: Value to set for the alertDetections property.
        """
        self._alert_detections = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def azure_subscription_id(self,) -> Optional[str]:
        """
        Gets the azureSubscriptionId property value. Azure subscription ID, present if this alert is related to an Azure resource.
        Returns: Optional[str]
        """
        return self._azure_subscription_id
    
    @azure_subscription_id.setter
    def azure_subscription_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureSubscriptionId property value. Azure subscription ID, present if this alert is related to an Azure resource.
        Args:
            value: Value to set for the azureSubscriptionId property.
        """
        self._azure_subscription_id = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. Azure Active Directory tenant ID. Required.
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. Azure Active Directory tenant ID. Required.
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    @property
    def category(self,) -> Optional[str]:
        """
        Gets the category property value. Category of the alert (for example, credentialTheft, ransomware, etc.).
        Returns: Optional[str]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[str] = None) -> None:
        """
        Sets the category property value. Category of the alert (for example, credentialTheft, ransomware, etc.).
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    @property
    def closed_date_time(self,) -> Optional[datetime]:
        """
        Gets the closedDateTime property value. Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (supports update).
        Returns: Optional[datetime]
        """
        return self._closed_date_time
    
    @closed_date_time.setter
    def closed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the closedDateTime property value. Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (supports update).
        Args:
            value: Value to set for the closedDateTime property.
        """
        self._closed_date_time = value
    
    @property
    def cloud_app_states(self,) -> Optional[List[cloud_app_security_state.CloudAppSecurityState]]:
        """
        Gets the cloudAppStates property value. Security-related stateful information generated by the provider about the cloud application/s related to this alert.
        Returns: Optional[List[cloud_app_security_state.CloudAppSecurityState]]
        """
        return self._cloud_app_states
    
    @cloud_app_states.setter
    def cloud_app_states(self,value: Optional[List[cloud_app_security_state.CloudAppSecurityState]] = None) -> None:
        """
        Sets the cloudAppStates property value. Security-related stateful information generated by the provider about the cloud application/s related to this alert.
        Args:
            value: Value to set for the cloudAppStates property.
        """
        self._cloud_app_states = value
    
    @property
    def comments(self,) -> Optional[List[str]]:
        """
        Gets the comments property value. Customer-provided comments on alert (for customer alert management) (supports update).
        Returns: Optional[List[str]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the comments property value. Customer-provided comments on alert (for customer alert management) (supports update).
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    @property
    def confidence(self,) -> Optional[int]:
        """
        Gets the confidence property value. Confidence of the detection logic (percentage between 1-100).
        Returns: Optional[int]
        """
        return self._confidence
    
    @confidence.setter
    def confidence(self,value: Optional[int] = None) -> None:
        """
        Sets the confidence property value. Confidence of the detection logic (percentage between 1-100).
        Args:
            value: Value to set for the confidence property.
        """
        self._confidence = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alert and sets the default values.
        """
        super().__init__()
        # Name or alias of the activity group (attacker) this alert is attributed to.
        self._activity_group_name: Optional[str] = None
        # The alertDetections property
        self._alert_detections: Optional[List[alert_detection.AlertDetection]] = None
        # Name of the analyst the alert is assigned to for triage, investigation, or remediation (supports update).
        self._assigned_to: Optional[str] = None
        # Azure subscription ID, present if this alert is related to an Azure resource.
        self._azure_subscription_id: Optional[str] = None
        # Azure Active Directory tenant ID. Required.
        self._azure_tenant_id: Optional[str] = None
        # Category of the alert (for example, credentialTheft, ransomware, etc.).
        self._category: Optional[str] = None
        # Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (supports update).
        self._closed_date_time: Optional[datetime] = None
        # Security-related stateful information generated by the provider about the cloud application/s related to this alert.
        self._cloud_app_states: Optional[List[cloud_app_security_state.CloudAppSecurityState]] = None
        # Customer-provided comments on alert (for customer alert management) (supports update).
        self._comments: Optional[List[str]] = None
        # Confidence of the detection logic (percentage between 1-100).
        self._confidence: Optional[int] = None
        # Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        self._created_date_time: Optional[datetime] = None
        # Alert description.
        self._description: Optional[str] = None
        # Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).
        self._detection_ids: Optional[List[str]] = None
        # Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        self._event_date_time: Optional[datetime] = None
        # Analyst feedback on the alert. Possible values are: unknown, truePositive, falsePositive, benignPositive. (supports update)
        self._feedback: Optional[alert_feedback.AlertFeedback] = None
        # Security-related stateful information generated by the provider about the file(s) related to this alert.
        self._file_states: Optional[List[file_security_state.FileSecurityState]] = None
        # The historyStates property
        self._history_states: Optional[List[alert_history_state.AlertHistoryState]] = None
        # Security-related stateful information generated by the provider about the host(s) related to this alert.
        self._host_states: Optional[List[host_security_state.HostSecurityState]] = None
        # IDs of incidents related to current alert.
        self._incident_ids: Optional[List[str]] = None
        # The investigationSecurityStates property
        self._investigation_security_states: Optional[List[investigation_security_state.InvestigationSecurityState]] = None
        # The lastEventDateTime property
        self._last_event_date_time: Optional[datetime] = None
        # Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # Threat Intelligence pertaining to malware related to this alert.
        self._malware_states: Optional[List[malware_state.MalwareState]] = None
        # The messageSecurityStates property
        self._message_security_states: Optional[List[message_security_state.MessageSecurityState]] = None
        # Security-related stateful information generated by the provider about the network connection(s) related to this alert.
        self._network_connections: Optional[List[network_connection.NetworkConnection]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Security-related stateful information generated by the provider about the process or processes related to this alert.
        self._processes: Optional[List[process.Process]] = None
        # Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).
        self._recommended_actions: Optional[List[str]] = None
        # Security-related stateful information generated by the provider about the registry keys related to this alert.
        self._registry_key_states: Optional[List[registry_key_state.RegistryKeyState]] = None
        # Resources related to current alert. For example, for some alerts this can have the Azure Resource value.
        self._security_resources: Optional[List[security_resource.SecurityResource]] = None
        # The severity property
        self._severity: Optional[alert_severity.AlertSeverity] = None
        # Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.
        self._source_materials: Optional[List[str]] = None
        # The status property
        self._status: Optional[alert_status.AlertStatus] = None
        # User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).
        self._tags: Optional[List[str]] = None
        # Alert title. Required.
        self._title: Optional[str] = None
        # Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.
        self._triggers: Optional[List[alert_trigger.AlertTrigger]] = None
        # The uriClickSecurityStates property
        self._uri_click_security_states: Optional[List[uri_click_security_state.UriClickSecurityState]] = None
        # Security-related stateful information generated by the provider about the user accounts related to this alert.
        self._user_states: Optional[List[user_security_state.UserSecurityState]] = None
        # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=Windows Defender ATP; subProvider=AppLocker). Required.
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
        # Threat intelligence pertaining to one or more vulnerabilities related to this alert.
        self._vulnerability_states: Optional[List[vulnerability_state.VulnerabilityState]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time at which the alert was created by the alert provider. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
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
        Gets the description property value. Alert description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Alert description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def detection_ids(self,) -> Optional[List[str]]:
        """
        Gets the detectionIds property value. Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).
        Returns: Optional[List[str]]
        """
        return self._detection_ids
    
    @detection_ids.setter
    def detection_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the detectionIds property value. Set of alerts related to this alert entity (each alert is pushed to the SIEM as a separate record).
        Args:
            value: Value to set for the detectionIds property.
        """
        self._detection_ids = value
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. Time at which the event(s) that served as the trigger(s) to generate the alert occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    @property
    def feedback(self,) -> Optional[alert_feedback.AlertFeedback]:
        """
        Gets the feedback property value. Analyst feedback on the alert. Possible values are: unknown, truePositive, falsePositive, benignPositive. (supports update)
        Returns: Optional[alert_feedback.AlertFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[alert_feedback.AlertFeedback] = None) -> None:
        """
        Sets the feedback property value. Analyst feedback on the alert. Possible values are: unknown, truePositive, falsePositive, benignPositive. (supports update)
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    @property
    def file_states(self,) -> Optional[List[file_security_state.FileSecurityState]]:
        """
        Gets the fileStates property value. Security-related stateful information generated by the provider about the file(s) related to this alert.
        Returns: Optional[List[file_security_state.FileSecurityState]]
        """
        return self._file_states
    
    @file_states.setter
    def file_states(self,value: Optional[List[file_security_state.FileSecurityState]] = None) -> None:
        """
        Sets the fileStates property value. Security-related stateful information generated by the provider about the file(s) related to this alert.
        Args:
            value: Value to set for the fileStates property.
        """
        self._file_states = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_group_name": lambda n : setattr(self, 'activity_group_name', n.get_str_value()),
            "alert_detections": lambda n : setattr(self, 'alert_detections', n.get_collection_of_object_values(alert_detection.AlertDetection)),
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "azure_subscription_id": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "closed_date_time": lambda n : setattr(self, 'closed_date_time', n.get_datetime_value()),
            "cloud_app_states": lambda n : setattr(self, 'cloud_app_states', n.get_collection_of_object_values(cloud_app_security_state.CloudAppSecurityState)),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detection_ids": lambda n : setattr(self, 'detection_ids', n.get_collection_of_primitive_values(str)),
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(alert_feedback.AlertFeedback)),
            "file_states": lambda n : setattr(self, 'file_states', n.get_collection_of_object_values(file_security_state.FileSecurityState)),
            "history_states": lambda n : setattr(self, 'history_states', n.get_collection_of_object_values(alert_history_state.AlertHistoryState)),
            "host_states": lambda n : setattr(self, 'host_states', n.get_collection_of_object_values(host_security_state.HostSecurityState)),
            "incident_ids": lambda n : setattr(self, 'incident_ids', n.get_collection_of_primitive_values(str)),
            "investigation_security_states": lambda n : setattr(self, 'investigation_security_states', n.get_collection_of_object_values(investigation_security_state.InvestigationSecurityState)),
            "last_event_date_time": lambda n : setattr(self, 'last_event_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "malware_states": lambda n : setattr(self, 'malware_states', n.get_collection_of_object_values(malware_state.MalwareState)),
            "message_security_states": lambda n : setattr(self, 'message_security_states', n.get_collection_of_object_values(message_security_state.MessageSecurityState)),
            "network_connections": lambda n : setattr(self, 'network_connections', n.get_collection_of_object_values(network_connection.NetworkConnection)),
            "processes": lambda n : setattr(self, 'processes', n.get_collection_of_object_values(process.Process)),
            "recommended_actions": lambda n : setattr(self, 'recommended_actions', n.get_collection_of_primitive_values(str)),
            "registry_key_states": lambda n : setattr(self, 'registry_key_states', n.get_collection_of_object_values(registry_key_state.RegistryKeyState)),
            "security_resources": lambda n : setattr(self, 'security_resources', n.get_collection_of_object_values(security_resource.SecurityResource)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(alert_severity.AlertSeverity)),
            "source_materials": lambda n : setattr(self, 'source_materials', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "triggers": lambda n : setattr(self, 'triggers', n.get_collection_of_object_values(alert_trigger.AlertTrigger)),
            "uri_click_security_states": lambda n : setattr(self, 'uri_click_security_states', n.get_collection_of_object_values(uri_click_security_state.UriClickSecurityState)),
            "user_states": lambda n : setattr(self, 'user_states', n.get_collection_of_object_values(user_security_state.UserSecurityState)),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
            "vulnerability_states": lambda n : setattr(self, 'vulnerability_states', n.get_collection_of_object_values(vulnerability_state.VulnerabilityState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history_states(self,) -> Optional[List[alert_history_state.AlertHistoryState]]:
        """
        Gets the historyStates property value. The historyStates property
        Returns: Optional[List[alert_history_state.AlertHistoryState]]
        """
        return self._history_states
    
    @history_states.setter
    def history_states(self,value: Optional[List[alert_history_state.AlertHistoryState]] = None) -> None:
        """
        Sets the historyStates property value. The historyStates property
        Args:
            value: Value to set for the historyStates property.
        """
        self._history_states = value
    
    @property
    def host_states(self,) -> Optional[List[host_security_state.HostSecurityState]]:
        """
        Gets the hostStates property value. Security-related stateful information generated by the provider about the host(s) related to this alert.
        Returns: Optional[List[host_security_state.HostSecurityState]]
        """
        return self._host_states
    
    @host_states.setter
    def host_states(self,value: Optional[List[host_security_state.HostSecurityState]] = None) -> None:
        """
        Sets the hostStates property value. Security-related stateful information generated by the provider about the host(s) related to this alert.
        Args:
            value: Value to set for the hostStates property.
        """
        self._host_states = value
    
    @property
    def incident_ids(self,) -> Optional[List[str]]:
        """
        Gets the incidentIds property value. IDs of incidents related to current alert.
        Returns: Optional[List[str]]
        """
        return self._incident_ids
    
    @incident_ids.setter
    def incident_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the incidentIds property value. IDs of incidents related to current alert.
        Args:
            value: Value to set for the incidentIds property.
        """
        self._incident_ids = value
    
    @property
    def investigation_security_states(self,) -> Optional[List[investigation_security_state.InvestigationSecurityState]]:
        """
        Gets the investigationSecurityStates property value. The investigationSecurityStates property
        Returns: Optional[List[investigation_security_state.InvestigationSecurityState]]
        """
        return self._investigation_security_states
    
    @investigation_security_states.setter
    def investigation_security_states(self,value: Optional[List[investigation_security_state.InvestigationSecurityState]] = None) -> None:
        """
        Sets the investigationSecurityStates property value. The investigationSecurityStates property
        Args:
            value: Value to set for the investigationSecurityStates property.
        """
        self._investigation_security_states = value
    
    @property
    def last_event_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastEventDateTime property value. The lastEventDateTime property
        Returns: Optional[datetime]
        """
        return self._last_event_date_time
    
    @last_event_date_time.setter
    def last_event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastEventDateTime property value. The lastEventDateTime property
        Args:
            value: Value to set for the lastEventDateTime property.
        """
        self._last_event_date_time = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Time at which the alert entity was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def malware_states(self,) -> Optional[List[malware_state.MalwareState]]:
        """
        Gets the malwareStates property value. Threat Intelligence pertaining to malware related to this alert.
        Returns: Optional[List[malware_state.MalwareState]]
        """
        return self._malware_states
    
    @malware_states.setter
    def malware_states(self,value: Optional[List[malware_state.MalwareState]] = None) -> None:
        """
        Sets the malwareStates property value. Threat Intelligence pertaining to malware related to this alert.
        Args:
            value: Value to set for the malwareStates property.
        """
        self._malware_states = value
    
    @property
    def message_security_states(self,) -> Optional[List[message_security_state.MessageSecurityState]]:
        """
        Gets the messageSecurityStates property value. The messageSecurityStates property
        Returns: Optional[List[message_security_state.MessageSecurityState]]
        """
        return self._message_security_states
    
    @message_security_states.setter
    def message_security_states(self,value: Optional[List[message_security_state.MessageSecurityState]] = None) -> None:
        """
        Sets the messageSecurityStates property value. The messageSecurityStates property
        Args:
            value: Value to set for the messageSecurityStates property.
        """
        self._message_security_states = value
    
    @property
    def network_connections(self,) -> Optional[List[network_connection.NetworkConnection]]:
        """
        Gets the networkConnections property value. Security-related stateful information generated by the provider about the network connection(s) related to this alert.
        Returns: Optional[List[network_connection.NetworkConnection]]
        """
        return self._network_connections
    
    @network_connections.setter
    def network_connections(self,value: Optional[List[network_connection.NetworkConnection]] = None) -> None:
        """
        Sets the networkConnections property value. Security-related stateful information generated by the provider about the network connection(s) related to this alert.
        Args:
            value: Value to set for the networkConnections property.
        """
        self._network_connections = value
    
    @property
    def processes(self,) -> Optional[List[process.Process]]:
        """
        Gets the processes property value. Security-related stateful information generated by the provider about the process or processes related to this alert.
        Returns: Optional[List[process.Process]]
        """
        return self._processes
    
    @processes.setter
    def processes(self,value: Optional[List[process.Process]] = None) -> None:
        """
        Sets the processes property value. Security-related stateful information generated by the provider about the process or processes related to this alert.
        Args:
            value: Value to set for the processes property.
        """
        self._processes = value
    
    @property
    def recommended_actions(self,) -> Optional[List[str]]:
        """
        Gets the recommendedActions property value. Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).
        Returns: Optional[List[str]]
        """
        return self._recommended_actions
    
    @recommended_actions.setter
    def recommended_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the recommendedActions property value. Vendor/provider recommended action(s) to take as a result of the alert (for example, isolate machine, enforce2FA, reimage host).
        Args:
            value: Value to set for the recommendedActions property.
        """
        self._recommended_actions = value
    
    @property
    def registry_key_states(self,) -> Optional[List[registry_key_state.RegistryKeyState]]:
        """
        Gets the registryKeyStates property value. Security-related stateful information generated by the provider about the registry keys related to this alert.
        Returns: Optional[List[registry_key_state.RegistryKeyState]]
        """
        return self._registry_key_states
    
    @registry_key_states.setter
    def registry_key_states(self,value: Optional[List[registry_key_state.RegistryKeyState]] = None) -> None:
        """
        Sets the registryKeyStates property value. Security-related stateful information generated by the provider about the registry keys related to this alert.
        Args:
            value: Value to set for the registryKeyStates property.
        """
        self._registry_key_states = value
    
    @property
    def security_resources(self,) -> Optional[List[security_resource.SecurityResource]]:
        """
        Gets the securityResources property value. Resources related to current alert. For example, for some alerts this can have the Azure Resource value.
        Returns: Optional[List[security_resource.SecurityResource]]
        """
        return self._security_resources
    
    @security_resources.setter
    def security_resources(self,value: Optional[List[security_resource.SecurityResource]] = None) -> None:
        """
        Sets the securityResources property value. Resources related to current alert. For example, for some alerts this can have the Azure Resource value.
        Args:
            value: Value to set for the securityResources property.
        """
        self._security_resources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activityGroupName", self.activity_group_name)
        writer.write_collection_of_object_values("alertDetections", self.alert_detections)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("category", self.category)
        writer.write_datetime_value("closedDateTime", self.closed_date_time)
        writer.write_collection_of_object_values("cloudAppStates", self.cloud_app_states)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_int_value("confidence", self.confidence)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("detectionIds", self.detection_ids)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_collection_of_object_values("fileStates", self.file_states)
        writer.write_collection_of_object_values("historyStates", self.history_states)
        writer.write_collection_of_object_values("hostStates", self.host_states)
        writer.write_collection_of_primitive_values("incidentIds", self.incident_ids)
        writer.write_collection_of_object_values("investigationSecurityStates", self.investigation_security_states)
        writer.write_datetime_value("lastEventDateTime", self.last_event_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("malwareStates", self.malware_states)
        writer.write_collection_of_object_values("messageSecurityStates", self.message_security_states)
        writer.write_collection_of_object_values("networkConnections", self.network_connections)
        writer.write_collection_of_object_values("processes", self.processes)
        writer.write_collection_of_primitive_values("recommendedActions", self.recommended_actions)
        writer.write_collection_of_object_values("registryKeyStates", self.registry_key_states)
        writer.write_collection_of_object_values("securityResources", self.security_resources)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_primitive_values("sourceMaterials", self.source_materials)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_object_values("triggers", self.triggers)
        writer.write_collection_of_object_values("uriClickSecurityStates", self.uri_click_security_states)
        writer.write_collection_of_object_values("userStates", self.user_states)
        writer.write_object_value("vendorInformation", self.vendor_information)
        writer.write_collection_of_object_values("vulnerabilityStates", self.vulnerability_states)
    
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
    def source_materials(self,) -> Optional[List[str]]:
        """
        Gets the sourceMaterials property value. Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.
        Returns: Optional[List[str]]
        """
        return self._source_materials
    
    @source_materials.setter
    def source_materials(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sourceMaterials property value. Hyperlinks (URIs) to the source material related to the alert, for example, provider's user interface for alerts or log search, etc.
        Args:
            value: Value to set for the sourceMaterials property.
        """
        self._source_materials = value
    
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
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. User-definable labels that can be applied to an alert and can serve as filter conditions (for example 'HVA', 'SAW', etc.) (supports update).
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Alert title. Required.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Alert title. Required.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def triggers(self,) -> Optional[List[alert_trigger.AlertTrigger]]:
        """
        Gets the triggers property value. Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.
        Returns: Optional[List[alert_trigger.AlertTrigger]]
        """
        return self._triggers
    
    @triggers.setter
    def triggers(self,value: Optional[List[alert_trigger.AlertTrigger]] = None) -> None:
        """
        Sets the triggers property value. Security-related information about the specific properties that triggered the alert (properties appearing in the alert). Alerts might contain information about multiple users, hosts, files, ip addresses. This field indicates which properties triggered the alert generation.
        Args:
            value: Value to set for the triggers property.
        """
        self._triggers = value
    
    @property
    def uri_click_security_states(self,) -> Optional[List[uri_click_security_state.UriClickSecurityState]]:
        """
        Gets the uriClickSecurityStates property value. The uriClickSecurityStates property
        Returns: Optional[List[uri_click_security_state.UriClickSecurityState]]
        """
        return self._uri_click_security_states
    
    @uri_click_security_states.setter
    def uri_click_security_states(self,value: Optional[List[uri_click_security_state.UriClickSecurityState]] = None) -> None:
        """
        Sets the uriClickSecurityStates property value. The uriClickSecurityStates property
        Args:
            value: Value to set for the uriClickSecurityStates property.
        """
        self._uri_click_security_states = value
    
    @property
    def user_states(self,) -> Optional[List[user_security_state.UserSecurityState]]:
        """
        Gets the userStates property value. Security-related stateful information generated by the provider about the user accounts related to this alert.
        Returns: Optional[List[user_security_state.UserSecurityState]]
        """
        return self._user_states
    
    @user_states.setter
    def user_states(self,value: Optional[List[user_security_state.UserSecurityState]] = None) -> None:
        """
        Sets the userStates property value. Security-related stateful information generated by the provider about the user accounts related to this alert.
        Args:
            value: Value to set for the userStates property.
        """
        self._user_states = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=Windows Defender ATP; subProvider=AppLocker). Required.
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=Windows Defender ATP; subProvider=AppLocker). Required.
        Args:
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    
    @property
    def vulnerability_states(self,) -> Optional[List[vulnerability_state.VulnerabilityState]]:
        """
        Gets the vulnerabilityStates property value. Threat intelligence pertaining to one or more vulnerabilities related to this alert.
        Returns: Optional[List[vulnerability_state.VulnerabilityState]]
        """
        return self._vulnerability_states
    
    @vulnerability_states.setter
    def vulnerability_states(self,value: Optional[List[vulnerability_state.VulnerabilityState]] = None) -> None:
        """
        Sets the vulnerabilityStates property value. Threat intelligence pertaining to one or more vulnerabilities related to this alert.
        Args:
            value: Value to set for the vulnerabilityStates property.
        """
        self._vulnerability_states = value
    

