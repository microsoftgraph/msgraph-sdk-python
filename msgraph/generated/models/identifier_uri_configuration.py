from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identifier_uri_restriction import IdentifierUriRestriction

@dataclass
class IdentifierUriConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Block new identifier URIs for applications, unless they are the 'default' URI of the format api://{appId} or api://{tenantId}/{appId}.
    non_default_uri_addition: Optional[IdentifierUriRestriction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Block new identifier URIs for applications, unless they contain a unique tenant identifier like the tenant ID, appId (client ID), or verified domain. For example, api://{tenantId}/string, api://{appId}/string, {scheme}://string/{tenantId}, {scheme}://string/{appId}, https://{verified-domain.com}/path, {scheme}://{subdomain}.{verified-domain.com}/path.
    uri_addition_without_unique_tenant_identifier: Optional[IdentifierUriRestriction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentifierUriConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentifierUriConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentifierUriConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identifier_uri_restriction import IdentifierUriRestriction

        from .identifier_uri_restriction import IdentifierUriRestriction

        fields: dict[str, Callable[[Any], None]] = {
            "nonDefaultUriAddition": lambda n : setattr(self, 'non_default_uri_addition', n.get_object_value(IdentifierUriRestriction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uriAdditionWithoutUniqueTenantIdentifier": lambda n : setattr(self, 'uri_addition_without_unique_tenant_identifier', n.get_object_value(IdentifierUriRestriction)),
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
        writer.write_object_value("nonDefaultUriAddition", self.non_default_uri_addition)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("uriAdditionWithoutUniqueTenantIdentifier", self.uri_addition_without_unique_tenant_identifier)
        writer.write_additional_data_value(self.additional_data)
    

