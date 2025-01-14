from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_filter import ConditionalAccessFilter

@dataclass
class ConditionalAccessClientApplications(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Service principal IDs excluded from the policy scope.
    exclude_service_principals: Optional[list[str]] = None
    # Service principal IDs included in the policy scope, or ServicePrincipalsInMyTenant.
    include_service_principals: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Filter that defines the dynamic-servicePrincipal-syntax rule to include/exclude service principals. A filter can use custom security attributes to include/exclude service principals.
    service_principal_filter: Optional[ConditionalAccessFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessClientApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessClientApplications
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessClientApplications()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_filter import ConditionalAccessFilter

        from .conditional_access_filter import ConditionalAccessFilter

        fields: dict[str, Callable[[Any], None]] = {
            "excludeServicePrincipals": lambda n : setattr(self, 'exclude_service_principals', n.get_collection_of_primitive_values(str)),
            "includeServicePrincipals": lambda n : setattr(self, 'include_service_principals', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "servicePrincipalFilter": lambda n : setattr(self, 'service_principal_filter', n.get_object_value(ConditionalAccessFilter)),
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
        writer.write_collection_of_primitive_values("excludeServicePrincipals", self.exclude_service_principals)
        writer.write_collection_of_primitive_values("includeServicePrincipals", self.include_service_principals)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("servicePrincipalFilter", self.service_principal_filter)
        writer.write_additional_data_value(self.additional_data)
    

