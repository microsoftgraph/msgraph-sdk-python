from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_entity_mapping import AccountEntityMapping
    from .amazon_resource_entity_mapping import AmazonResourceEntityMapping
    from .azure_resource_entity_mapping import AzureResourceEntityMapping
    from .cloud_application_entity_mapping import CloudApplicationEntityMapping
    from .dns_entity_mapping import DnsEntityMapping
    from .file_entity_mapping import FileEntityMapping
    from .google_cloud_resource_entity_mapping import GoogleCloudResourceEntityMapping
    from .host_entity_mapping import HostEntityMapping
    from .ip_entity_mapping import IpEntityMapping
    from .mailbox_entity_mapping import MailboxEntityMapping
    from .mail_cluster_entity_mapping import MailClusterEntityMapping
    from .mail_message_entity_mapping import MailMessageEntityMapping
    from .o_auth_application_entity_mapping import OAuthApplicationEntityMapping
    from .process_entity_mapping import ProcessEntityMapping
    from .registry_value_entity_mapping import RegistryValueEntityMapping
    from .security_group_entity_mapping import SecurityGroupEntityMapping
    from .url_entity_mapping import UrlEntityMapping

@dataclass
class EntityMappingConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Mappings from detection query columns to account entities attached to the alert.
    accounts: Optional[list[AccountEntityMapping]] = None
    # Mappings from detection query columns to Amazon Web Services resource entities attached to the alert.
    amazon_resources: Optional[list[AmazonResourceEntityMapping]] = None
    # Mappings from detection query columns to Azure resource entities attached to the alert.
    azure_resources: Optional[list[AzureResourceEntityMapping]] = None
    # Mappings from detection query columns to cloud application entities attached to the alert.
    cloud_applications: Optional[list[CloudApplicationEntityMapping]] = None
    # Mappings from detection query columns to DNS entities attached to the alert.
    dns: Optional[list[DnsEntityMapping]] = None
    # Mappings from detection query columns to file entities attached to the alert.
    files: Optional[list[FileEntityMapping]] = None
    # Mappings from detection query columns to Google Cloud resource entities attached to the alert.
    google_cloud_resources: Optional[list[GoogleCloudResourceEntityMapping]] = None
    # Mappings from detection query columns to host entities attached to the alert.
    hosts: Optional[list[HostEntityMapping]] = None
    # Mappings from detection query columns to IP address entities attached to the alert.
    ips: Optional[list[IpEntityMapping]] = None
    # Mappings from detection query columns to mail cluster entities attached to the alert.
    mail_clusters: Optional[list[MailClusterEntityMapping]] = None
    # Mappings from detection query columns to mail message entities attached to the alert.
    mail_messages: Optional[list[MailMessageEntityMapping]] = None
    # Mappings from detection query columns to mailbox entities attached to the alert.
    mailboxes: Optional[list[MailboxEntityMapping]] = None
    # Mappings from detection query columns to OAuth application entities attached to the alert.
    o_auth_applications: Optional[list[OAuthApplicationEntityMapping]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Mappings from detection query columns to process entities attached to the alert.
    processes: Optional[list[ProcessEntityMapping]] = None
    # Mappings from detection query columns to registry value entities attached to the alert.
    registry_values: Optional[list[RegistryValueEntityMapping]] = None
    # Mappings from detection query columns to security group entities attached to the alert.
    security_groups: Optional[list[SecurityGroupEntityMapping]] = None
    # Mappings from detection query columns to URL entities attached to the alert.
    urls: Optional[list[UrlEntityMapping]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntityMappingConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntityMappingConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntityMappingConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .account_entity_mapping import AccountEntityMapping
        from .amazon_resource_entity_mapping import AmazonResourceEntityMapping
        from .azure_resource_entity_mapping import AzureResourceEntityMapping
        from .cloud_application_entity_mapping import CloudApplicationEntityMapping
        from .dns_entity_mapping import DnsEntityMapping
        from .file_entity_mapping import FileEntityMapping
        from .google_cloud_resource_entity_mapping import GoogleCloudResourceEntityMapping
        from .host_entity_mapping import HostEntityMapping
        from .ip_entity_mapping import IpEntityMapping
        from .mailbox_entity_mapping import MailboxEntityMapping
        from .mail_cluster_entity_mapping import MailClusterEntityMapping
        from .mail_message_entity_mapping import MailMessageEntityMapping
        from .o_auth_application_entity_mapping import OAuthApplicationEntityMapping
        from .process_entity_mapping import ProcessEntityMapping
        from .registry_value_entity_mapping import RegistryValueEntityMapping
        from .security_group_entity_mapping import SecurityGroupEntityMapping
        from .url_entity_mapping import UrlEntityMapping

        from .account_entity_mapping import AccountEntityMapping
        from .amazon_resource_entity_mapping import AmazonResourceEntityMapping
        from .azure_resource_entity_mapping import AzureResourceEntityMapping
        from .cloud_application_entity_mapping import CloudApplicationEntityMapping
        from .dns_entity_mapping import DnsEntityMapping
        from .file_entity_mapping import FileEntityMapping
        from .google_cloud_resource_entity_mapping import GoogleCloudResourceEntityMapping
        from .host_entity_mapping import HostEntityMapping
        from .ip_entity_mapping import IpEntityMapping
        from .mailbox_entity_mapping import MailboxEntityMapping
        from .mail_cluster_entity_mapping import MailClusterEntityMapping
        from .mail_message_entity_mapping import MailMessageEntityMapping
        from .o_auth_application_entity_mapping import OAuthApplicationEntityMapping
        from .process_entity_mapping import ProcessEntityMapping
        from .registry_value_entity_mapping import RegistryValueEntityMapping
        from .security_group_entity_mapping import SecurityGroupEntityMapping
        from .url_entity_mapping import UrlEntityMapping

        fields: dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(AccountEntityMapping)),
            "amazonResources": lambda n : setattr(self, 'amazon_resources', n.get_collection_of_object_values(AmazonResourceEntityMapping)),
            "azureResources": lambda n : setattr(self, 'azure_resources', n.get_collection_of_object_values(AzureResourceEntityMapping)),
            "cloudApplications": lambda n : setattr(self, 'cloud_applications', n.get_collection_of_object_values(CloudApplicationEntityMapping)),
            "dns": lambda n : setattr(self, 'dns', n.get_collection_of_object_values(DnsEntityMapping)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(FileEntityMapping)),
            "googleCloudResources": lambda n : setattr(self, 'google_cloud_resources', n.get_collection_of_object_values(GoogleCloudResourceEntityMapping)),
            "hosts": lambda n : setattr(self, 'hosts', n.get_collection_of_object_values(HostEntityMapping)),
            "ips": lambda n : setattr(self, 'ips', n.get_collection_of_object_values(IpEntityMapping)),
            "mailClusters": lambda n : setattr(self, 'mail_clusters', n.get_collection_of_object_values(MailClusterEntityMapping)),
            "mailMessages": lambda n : setattr(self, 'mail_messages', n.get_collection_of_object_values(MailMessageEntityMapping)),
            "mailboxes": lambda n : setattr(self, 'mailboxes', n.get_collection_of_object_values(MailboxEntityMapping)),
            "oAuthApplications": lambda n : setattr(self, 'o_auth_applications', n.get_collection_of_object_values(OAuthApplicationEntityMapping)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processes": lambda n : setattr(self, 'processes', n.get_collection_of_object_values(ProcessEntityMapping)),
            "registryValues": lambda n : setattr(self, 'registry_values', n.get_collection_of_object_values(RegistryValueEntityMapping)),
            "securityGroups": lambda n : setattr(self, 'security_groups', n.get_collection_of_object_values(SecurityGroupEntityMapping)),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_object_values(UrlEntityMapping)),
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
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_collection_of_object_values("amazonResources", self.amazon_resources)
        writer.write_collection_of_object_values("azureResources", self.azure_resources)
        writer.write_collection_of_object_values("cloudApplications", self.cloud_applications)
        writer.write_collection_of_object_values("dns", self.dns)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_collection_of_object_values("googleCloudResources", self.google_cloud_resources)
        writer.write_collection_of_object_values("hosts", self.hosts)
        writer.write_collection_of_object_values("ips", self.ips)
        writer.write_collection_of_object_values("mailClusters", self.mail_clusters)
        writer.write_collection_of_object_values("mailMessages", self.mail_messages)
        writer.write_collection_of_object_values("mailboxes", self.mailboxes)
        writer.write_collection_of_object_values("oAuthApplications", self.o_auth_applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("processes", self.processes)
        writer.write_collection_of_object_values("registryValues", self.registry_values)
        writer.write_collection_of_object_values("securityGroups", self.security_groups)
        writer.write_collection_of_object_values("urls", self.urls)
        writer.write_additional_data_value(self.additional_data)
    

