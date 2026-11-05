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
class EntityMapping(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return EntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.accountEntityMapping".casefold():
            from .account_entity_mapping import AccountEntityMapping

            return AccountEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.amazonResourceEntityMapping".casefold():
            from .amazon_resource_entity_mapping import AmazonResourceEntityMapping

            return AmazonResourceEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.azureResourceEntityMapping".casefold():
            from .azure_resource_entity_mapping import AzureResourceEntityMapping

            return AzureResourceEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.cloudApplicationEntityMapping".casefold():
            from .cloud_application_entity_mapping import CloudApplicationEntityMapping

            return CloudApplicationEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.dnsEntityMapping".casefold():
            from .dns_entity_mapping import DnsEntityMapping

            return DnsEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.fileEntityMapping".casefold():
            from .file_entity_mapping import FileEntityMapping

            return FileEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.googleCloudResourceEntityMapping".casefold():
            from .google_cloud_resource_entity_mapping import GoogleCloudResourceEntityMapping

            return GoogleCloudResourceEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.hostEntityMapping".casefold():
            from .host_entity_mapping import HostEntityMapping

            return HostEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.ipEntityMapping".casefold():
            from .ip_entity_mapping import IpEntityMapping

            return IpEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.mailboxEntityMapping".casefold():
            from .mailbox_entity_mapping import MailboxEntityMapping

            return MailboxEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.mailClusterEntityMapping".casefold():
            from .mail_cluster_entity_mapping import MailClusterEntityMapping

            return MailClusterEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.mailMessageEntityMapping".casefold():
            from .mail_message_entity_mapping import MailMessageEntityMapping

            return MailMessageEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.oAuthApplicationEntityMapping".casefold():
            from .o_auth_application_entity_mapping import OAuthApplicationEntityMapping

            return OAuthApplicationEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.processEntityMapping".casefold():
            from .process_entity_mapping import ProcessEntityMapping

            return ProcessEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.registryValueEntityMapping".casefold():
            from .registry_value_entity_mapping import RegistryValueEntityMapping

            return RegistryValueEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.securityGroupEntityMapping".casefold():
            from .security_group_entity_mapping import SecurityGroupEntityMapping

            return SecurityGroupEntityMapping()
        if mapping_value.casefold() == "#microsoft.graph.security.urlEntityMapping".casefold():
            from .url_entity_mapping import UrlEntityMapping

            return UrlEntityMapping()
        return EntityMapping()
    
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

