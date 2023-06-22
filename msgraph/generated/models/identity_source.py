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
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureActiveDirectoryTenant".casefold():
            from . import azure_active_directory_tenant

            return azure_active_directory_tenant.AzureActiveDirectoryTenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossCloudAzureActiveDirectoryTenant".casefold():
            from . import cross_cloud_azure_active_directory_tenant

            return cross_cloud_azure_active_directory_tenant.CrossCloudAzureActiveDirectoryTenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainIdentitySource".casefold():
            from . import domain_identity_source

            return domain_identity_source.DomainIdentitySource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalDomainFederation".casefold():
            from . import external_domain_federation

            return external_domain_federation.ExternalDomainFederation()
        return IdentitySource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import azure_active_directory_tenant, cross_cloud_azure_active_directory_tenant, domain_identity_source, external_domain_federation

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
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

