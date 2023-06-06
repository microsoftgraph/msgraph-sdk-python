from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import azure_active_directory_tenant, cross_cloud_azure_active_directory_tenant, domain_identity_source, external_domain_federation

@dataclass
class IdentitySource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentitySource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.azureActiveDirectoryTenant":
                from . import azure_active_directory_tenant

                return azure_active_directory_tenant.AzureActiveDirectoryTenant()
            if mapping_value == "#microsoft.graph.crossCloudAzureActiveDirectoryTenant":
                from . import cross_cloud_azure_active_directory_tenant

                return cross_cloud_azure_active_directory_tenant.CrossCloudAzureActiveDirectoryTenant()
            if mapping_value == "#microsoft.graph.domainIdentitySource":
                from . import domain_identity_source

                return domain_identity_source.DomainIdentitySource()
            if mapping_value == "#microsoft.graph.externalDomainFederation":
                from . import external_domain_federation

                return external_domain_federation.ExternalDomainFederation()
        return IdentitySource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import azure_active_directory_tenant, cross_cloud_azure_active_directory_tenant, domain_identity_source, external_domain_federation

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

