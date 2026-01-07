from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_directory_domain_evidence import ActiveDirectoryDomainEvidence
    from .ai_agent_evidence import AiAgentEvidence
    from .amazon_resource_evidence import AmazonResourceEvidence
    from .analyzed_message_evidence import AnalyzedMessageEvidence
    from .azure_resource_evidence import AzureResourceEvidence
    from .blob_container_evidence import BlobContainerEvidence
    from .blob_evidence import BlobEvidence
    from .cloud_application_evidence import CloudApplicationEvidence
    from .cloud_logon_request_evidence import CloudLogonRequestEvidence
    from .cloud_logon_session_evidence import CloudLogonSessionEvidence
    from .container_evidence import ContainerEvidence
    from .container_image_evidence import ContainerImageEvidence
    from .container_registry_evidence import ContainerRegistryEvidence
    from .device_evidence import DeviceEvidence
    from .dns_evidence import DnsEvidence
    from .evidence_remediation_status import EvidenceRemediationStatus
    from .evidence_role import EvidenceRole
    from .evidence_verdict import EvidenceVerdict
    from .file_evidence import FileEvidence
    from .file_hash_evidence import FileHashEvidence
    from .git_hub_organization_evidence import GitHubOrganizationEvidence
    from .git_hub_repo_evidence import GitHubRepoEvidence
    from .git_hub_user_evidence import GitHubUserEvidence
    from .google_cloud_resource_evidence import GoogleCloudResourceEvidence
    from .host_logon_session_evidence import HostLogonSessionEvidence
    from .io_t_device_evidence import IoTDeviceEvidence
    from .ip_evidence import IpEvidence
    from .kubernetes_cluster_evidence import KubernetesClusterEvidence
    from .kubernetes_controller_evidence import KubernetesControllerEvidence
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
    from .kubernetes_pod_evidence import KubernetesPodEvidence
    from .kubernetes_secret_evidence import KubernetesSecretEvidence
    from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence
    from .kubernetes_service_evidence import KubernetesServiceEvidence
    from .mailbox_configuration_evidence import MailboxConfigurationEvidence
    from .mailbox_evidence import MailboxEvidence
    from .mail_cluster_evidence import MailClusterEvidence
    from .malware_evidence import MalwareEvidence
    from .network_connection_evidence import NetworkConnectionEvidence
    from .nic_evidence import NicEvidence
    from .oauth_application_evidence import OauthApplicationEvidence
    from .process_evidence import ProcessEvidence
    from .registry_key_evidence import RegistryKeyEvidence
    from .registry_value_evidence import RegistryValueEvidence
    from .sas_token_evidence import SasTokenEvidence
    from .security_group_evidence import SecurityGroupEvidence
    from .service_principal_evidence import ServicePrincipalEvidence
    from .submission_mail_evidence import SubmissionMailEvidence
    from .teams_message_evidence import TeamsMessageEvidence
    from .url_evidence import UrlEvidence
    from .user_evidence import UserEvidence

@dataclass
class AlertEvidence(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The date and time when the evidence was created and added to the alert. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Detailed description of the entity role/s in an alert. Values are free-form.
    detailed_roles: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remediationStatus property
    remediation_status: Optional[EvidenceRemediationStatus] = None
    # Details about the remediation status.
    remediation_status_details: Optional[str] = None
    # The role/s that an evidence entity represents in an alert, for example, an IP address that is associated with an attacker has the evidence role Attacker.
    roles: Optional[list[EvidenceRole]] = None
    # Array of custom tags associated with an evidence instance, for example, to denote a group of devices, high-value assets, etc.
    tags: Optional[list[str]] = None
    # The verdict property
    verdict: Optional[EvidenceVerdict] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.activeDirectoryDomainEvidence".casefold():
            from .active_directory_domain_evidence import ActiveDirectoryDomainEvidence

            return ActiveDirectoryDomainEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.aiAgentEvidence".casefold():
            from .ai_agent_evidence import AiAgentEvidence

            return AiAgentEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.amazonResourceEvidence".casefold():
            from .amazon_resource_evidence import AmazonResourceEvidence

            return AmazonResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.analyzedMessageEvidence".casefold():
            from .analyzed_message_evidence import AnalyzedMessageEvidence

            return AnalyzedMessageEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.azureResourceEvidence".casefold():
            from .azure_resource_evidence import AzureResourceEvidence

            return AzureResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.blobContainerEvidence".casefold():
            from .blob_container_evidence import BlobContainerEvidence

            return BlobContainerEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.blobEvidence".casefold():
            from .blob_evidence import BlobEvidence

            return BlobEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudApplicationEvidence".casefold():
            from .cloud_application_evidence import CloudApplicationEvidence

            return CloudApplicationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudLogonRequestEvidence".casefold():
            from .cloud_logon_request_evidence import CloudLogonRequestEvidence

            return CloudLogonRequestEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.cloudLogonSessionEvidence".casefold():
            from .cloud_logon_session_evidence import CloudLogonSessionEvidence

            return CloudLogonSessionEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.containerEvidence".casefold():
            from .container_evidence import ContainerEvidence

            return ContainerEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.containerImageEvidence".casefold():
            from .container_image_evidence import ContainerImageEvidence

            return ContainerImageEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.containerRegistryEvidence".casefold():
            from .container_registry_evidence import ContainerRegistryEvidence

            return ContainerRegistryEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.deviceEvidence".casefold():
            from .device_evidence import DeviceEvidence

            return DeviceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dnsEvidence".casefold():
            from .dns_evidence import DnsEvidence

            return DnsEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileEvidence".casefold():
            from .file_evidence import FileEvidence

            return FileEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileHashEvidence".casefold():
            from .file_hash_evidence import FileHashEvidence

            return FileHashEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.gitHubOrganizationEvidence".casefold():
            from .git_hub_organization_evidence import GitHubOrganizationEvidence

            return GitHubOrganizationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.gitHubRepoEvidence".casefold():
            from .git_hub_repo_evidence import GitHubRepoEvidence

            return GitHubRepoEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.gitHubUserEvidence".casefold():
            from .git_hub_user_evidence import GitHubUserEvidence

            return GitHubUserEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.googleCloudResourceEvidence".casefold():
            from .google_cloud_resource_evidence import GoogleCloudResourceEvidence

            return GoogleCloudResourceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostLogonSessionEvidence".casefold():
            from .host_logon_session_evidence import HostLogonSessionEvidence

            return HostLogonSessionEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ioTDeviceEvidence".casefold():
            from .io_t_device_evidence import IoTDeviceEvidence

            return IoTDeviceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipEvidence".casefold():
            from .ip_evidence import IpEvidence

            return IpEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesClusterEvidence".casefold():
            from .kubernetes_cluster_evidence import KubernetesClusterEvidence

            return KubernetesClusterEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesControllerEvidence".casefold():
            from .kubernetes_controller_evidence import KubernetesControllerEvidence

            return KubernetesControllerEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesNamespaceEvidence".casefold():
            from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

            return KubernetesNamespaceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesPodEvidence".casefold():
            from .kubernetes_pod_evidence import KubernetesPodEvidence

            return KubernetesPodEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesSecretEvidence".casefold():
            from .kubernetes_secret_evidence import KubernetesSecretEvidence

            return KubernetesSecretEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesServiceAccountEvidence".casefold():
            from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence

            return KubernetesServiceAccountEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.kubernetesServiceEvidence".casefold():
            from .kubernetes_service_evidence import KubernetesServiceEvidence

            return KubernetesServiceEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailboxConfigurationEvidence".casefold():
            from .mailbox_configuration_evidence import MailboxConfigurationEvidence

            return MailboxConfigurationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailboxEvidence".casefold():
            from .mailbox_evidence import MailboxEvidence

            return MailboxEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.mailClusterEvidence".casefold():
            from .mail_cluster_evidence import MailClusterEvidence

            return MailClusterEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.malwareEvidence".casefold():
            from .malware_evidence import MalwareEvidence

            return MalwareEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.networkConnectionEvidence".casefold():
            from .network_connection_evidence import NetworkConnectionEvidence

            return NetworkConnectionEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.nicEvidence".casefold():
            from .nic_evidence import NicEvidence

            return NicEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.oauthApplicationEvidence".casefold():
            from .oauth_application_evidence import OauthApplicationEvidence

            return OauthApplicationEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.processEvidence".casefold():
            from .process_evidence import ProcessEvidence

            return ProcessEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.registryKeyEvidence".casefold():
            from .registry_key_evidence import RegistryKeyEvidence

            return RegistryKeyEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.registryValueEvidence".casefold():
            from .registry_value_evidence import RegistryValueEvidence

            return RegistryValueEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sasTokenEvidence".casefold():
            from .sas_token_evidence import SasTokenEvidence

            return SasTokenEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.securityGroupEvidence".casefold():
            from .security_group_evidence import SecurityGroupEvidence

            return SecurityGroupEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.servicePrincipalEvidence".casefold():
            from .service_principal_evidence import ServicePrincipalEvidence

            return ServicePrincipalEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.submissionMailEvidence".casefold():
            from .submission_mail_evidence import SubmissionMailEvidence

            return SubmissionMailEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.teamsMessageEvidence".casefold():
            from .teams_message_evidence import TeamsMessageEvidence

            return TeamsMessageEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urlEvidence".casefold():
            from .url_evidence import UrlEvidence

            return UrlEvidence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userEvidence".casefold():
            from .user_evidence import UserEvidence

            return UserEvidence()
        return AlertEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .active_directory_domain_evidence import ActiveDirectoryDomainEvidence
        from .ai_agent_evidence import AiAgentEvidence
        from .amazon_resource_evidence import AmazonResourceEvidence
        from .analyzed_message_evidence import AnalyzedMessageEvidence
        from .azure_resource_evidence import AzureResourceEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .blob_evidence import BlobEvidence
        from .cloud_application_evidence import CloudApplicationEvidence
        from .cloud_logon_request_evidence import CloudLogonRequestEvidence
        from .cloud_logon_session_evidence import CloudLogonSessionEvidence
        from .container_evidence import ContainerEvidence
        from .container_image_evidence import ContainerImageEvidence
        from .container_registry_evidence import ContainerRegistryEvidence
        from .device_evidence import DeviceEvidence
        from .dns_evidence import DnsEvidence
        from .evidence_remediation_status import EvidenceRemediationStatus
        from .evidence_role import EvidenceRole
        from .evidence_verdict import EvidenceVerdict
        from .file_evidence import FileEvidence
        from .file_hash_evidence import FileHashEvidence
        from .git_hub_organization_evidence import GitHubOrganizationEvidence
        from .git_hub_repo_evidence import GitHubRepoEvidence
        from .git_hub_user_evidence import GitHubUserEvidence
        from .google_cloud_resource_evidence import GoogleCloudResourceEvidence
        from .host_logon_session_evidence import HostLogonSessionEvidence
        from .io_t_device_evidence import IoTDeviceEvidence
        from .ip_evidence import IpEvidence
        from .kubernetes_cluster_evidence import KubernetesClusterEvidence
        from .kubernetes_controller_evidence import KubernetesControllerEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_pod_evidence import KubernetesPodEvidence
        from .kubernetes_secret_evidence import KubernetesSecretEvidence
        from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence
        from .kubernetes_service_evidence import KubernetesServiceEvidence
        from .mailbox_configuration_evidence import MailboxConfigurationEvidence
        from .mailbox_evidence import MailboxEvidence
        from .mail_cluster_evidence import MailClusterEvidence
        from .malware_evidence import MalwareEvidence
        from .network_connection_evidence import NetworkConnectionEvidence
        from .nic_evidence import NicEvidence
        from .oauth_application_evidence import OauthApplicationEvidence
        from .process_evidence import ProcessEvidence
        from .registry_key_evidence import RegistryKeyEvidence
        from .registry_value_evidence import RegistryValueEvidence
        from .sas_token_evidence import SasTokenEvidence
        from .security_group_evidence import SecurityGroupEvidence
        from .service_principal_evidence import ServicePrincipalEvidence
        from .submission_mail_evidence import SubmissionMailEvidence
        from .teams_message_evidence import TeamsMessageEvidence
        from .url_evidence import UrlEvidence
        from .user_evidence import UserEvidence

        from .active_directory_domain_evidence import ActiveDirectoryDomainEvidence
        from .ai_agent_evidence import AiAgentEvidence
        from .amazon_resource_evidence import AmazonResourceEvidence
        from .analyzed_message_evidence import AnalyzedMessageEvidence
        from .azure_resource_evidence import AzureResourceEvidence
        from .blob_container_evidence import BlobContainerEvidence
        from .blob_evidence import BlobEvidence
        from .cloud_application_evidence import CloudApplicationEvidence
        from .cloud_logon_request_evidence import CloudLogonRequestEvidence
        from .cloud_logon_session_evidence import CloudLogonSessionEvidence
        from .container_evidence import ContainerEvidence
        from .container_image_evidence import ContainerImageEvidence
        from .container_registry_evidence import ContainerRegistryEvidence
        from .device_evidence import DeviceEvidence
        from .dns_evidence import DnsEvidence
        from .evidence_remediation_status import EvidenceRemediationStatus
        from .evidence_role import EvidenceRole
        from .evidence_verdict import EvidenceVerdict
        from .file_evidence import FileEvidence
        from .file_hash_evidence import FileHashEvidence
        from .git_hub_organization_evidence import GitHubOrganizationEvidence
        from .git_hub_repo_evidence import GitHubRepoEvidence
        from .git_hub_user_evidence import GitHubUserEvidence
        from .google_cloud_resource_evidence import GoogleCloudResourceEvidence
        from .host_logon_session_evidence import HostLogonSessionEvidence
        from .io_t_device_evidence import IoTDeviceEvidence
        from .ip_evidence import IpEvidence
        from .kubernetes_cluster_evidence import KubernetesClusterEvidence
        from .kubernetes_controller_evidence import KubernetesControllerEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_pod_evidence import KubernetesPodEvidence
        from .kubernetes_secret_evidence import KubernetesSecretEvidence
        from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence
        from .kubernetes_service_evidence import KubernetesServiceEvidence
        from .mailbox_configuration_evidence import MailboxConfigurationEvidence
        from .mailbox_evidence import MailboxEvidence
        from .mail_cluster_evidence import MailClusterEvidence
        from .malware_evidence import MalwareEvidence
        from .network_connection_evidence import NetworkConnectionEvidence
        from .nic_evidence import NicEvidence
        from .oauth_application_evidence import OauthApplicationEvidence
        from .process_evidence import ProcessEvidence
        from .registry_key_evidence import RegistryKeyEvidence
        from .registry_value_evidence import RegistryValueEvidence
        from .sas_token_evidence import SasTokenEvidence
        from .security_group_evidence import SecurityGroupEvidence
        from .service_principal_evidence import ServicePrincipalEvidence
        from .submission_mail_evidence import SubmissionMailEvidence
        from .teams_message_evidence import TeamsMessageEvidence
        from .url_evidence import UrlEvidence
        from .user_evidence import UserEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "detailedRoles": lambda n : setattr(self, 'detailed_roles', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediationStatus": lambda n : setattr(self, 'remediation_status', n.get_enum_value(EvidenceRemediationStatus)),
            "remediationStatusDetails": lambda n : setattr(self, 'remediation_status_details', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_enum_values(EvidenceRole)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "verdict": lambda n : setattr(self, 'verdict', n.get_enum_value(EvidenceVerdict)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
    

