from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import amazon_resource_evidence, analyzed_message_evidence, azure_resource_evidence, cloud_application_evidence, device_evidence, evidence_remediation_status, evidence_role, evidence_verdict, file_evidence, google_cloud_resource_evidence, ip_evidence, mailbox_evidence, mail_cluster_evidence, oauth_application_evidence, process_evidence, registry_key_evidence, registry_value_evidence, security_group_evidence, url_evidence, user_evidence

@dataclass
class AlertEvidence(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date and time when the evidence was created and added to the alert. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime] = None
    # The detailedRoles property
    detailed_roles: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remediationStatus property
    remediation_status: Optional[evidence_remediation_status.EvidenceRemediationStatus] = None
    # Details about the remediation status.
    remediation_status_details: Optional[str] = None
    # One or more roles that an evidence entity represents in an alert. For example, an IP address that is associated with an attacker has the evidence role Attacker.
    roles: Optional[List[evidence_role.EvidenceRole]] = None
    # Array of custom tags associated with an evidence instance. For example, to denote a group of devices or high value assets.
    tags: Optional[List[str]] = None
    # The verdict property
    verdict: Optional[evidence_verdict.EvidenceVerdict] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.amazonResourceEvidence".casefold():
            from . import amazon_resource_evidence

            return amazon_resource_evidence.AmazonResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.analyzedMessageEvidence".casefold():
            from . import analyzed_message_evidence

            return analyzed_message_evidence.AnalyzedMessageEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureResourceEvidence".casefold():
            from . import azure_resource_evidence

            return azure_resource_evidence.AzureResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudApplicationEvidence".casefold():
            from . import cloud_application_evidence

            return cloud_application_evidence.CloudApplicationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deviceEvidence".casefold():
            from . import device_evidence

            return device_evidence.DeviceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileEvidence".casefold():
            from . import file_evidence

            return file_evidence.FileEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.googleCloudResourceEvidence".casefold():
            from . import google_cloud_resource_evidence

            return google_cloud_resource_evidence.GoogleCloudResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipEvidence".casefold():
            from . import ip_evidence

            return ip_evidence.IpEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailboxEvidence".casefold():
            from . import mailbox_evidence

            return mailbox_evidence.MailboxEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailClusterEvidence".casefold():
            from . import mail_cluster_evidence

            return mail_cluster_evidence.MailClusterEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.oauthApplicationEvidence".casefold():
            from . import oauth_application_evidence

            return oauth_application_evidence.OauthApplicationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.processEvidence".casefold():
            from . import process_evidence

            return process_evidence.ProcessEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.registryKeyEvidence".casefold():
            from . import registry_key_evidence

            return registry_key_evidence.RegistryKeyEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.registryValueEvidence".casefold():
            from . import registry_value_evidence

            return registry_value_evidence.RegistryValueEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityGroupEvidence".casefold():
            from . import security_group_evidence

            return security_group_evidence.SecurityGroupEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urlEvidence".casefold():
            from . import url_evidence

            return url_evidence.UrlEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userEvidence".casefold():
            from . import user_evidence

            return user_evidence.UserEvidence()
        return AlertEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import amazon_resource_evidence, analyzed_message_evidence, azure_resource_evidence, cloud_application_evidence, device_evidence, evidence_remediation_status, evidence_role, evidence_verdict, file_evidence, google_cloud_resource_evidence, ip_evidence, mailbox_evidence, mail_cluster_evidence, oauth_application_evidence, process_evidence, registry_key_evidence, registry_value_evidence, security_group_evidence, url_evidence, user_evidence

        from . import amazon_resource_evidence, analyzed_message_evidence, azure_resource_evidence, cloud_application_evidence, device_evidence, evidence_remediation_status, evidence_role, evidence_verdict, file_evidence, google_cloud_resource_evidence, ip_evidence, mailbox_evidence, mail_cluster_evidence, oauth_application_evidence, process_evidence, registry_key_evidence, registry_value_evidence, security_group_evidence, url_evidence, user_evidence

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "detailedRoles": lambda n : setattr(self, 'detailed_roles', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediationStatus": lambda n : setattr(self, 'remediation_status', n.get_enum_value(evidence_remediation_status.EvidenceRemediationStatus)),
            "remediationStatusDetails": lambda n : setattr(self, 'remediation_status_details', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_enum_values(evidence_role.EvidenceRole)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "verdict": lambda n : setattr(self, 'verdict', n.get_enum_value(evidence_verdict.EvidenceVerdict)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_primitive_values("detailedRoles", self.detailed_roles)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("remediationStatus", self.remediation_status)
        writer.write_str_value("remediationStatusDetails", self.remediation_status_details)
        writer.write_collection_of_enum_values("roles", self.roles)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_enum_value("verdict", self.verdict)
        writer.write_additional_data_value(self.additional_data)
    

