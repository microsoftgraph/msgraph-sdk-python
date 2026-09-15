from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applications_required_resource_access import ApplicationsRequiredResourceAccess

@dataclass
class MultiTenantApplicationsToProvision(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appId property
    app_id: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The objectId property
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The requiredResourceAccesses property
    required_resource_accesses: Optional[list[ApplicationsRequiredResourceAccess]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantApplicationsToProvision:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantApplicationsToProvision
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantApplicationsToProvision()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applications_required_resource_access import ApplicationsRequiredResourceAccess

        from .applications_required_resource_access import ApplicationsRequiredResourceAccess

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requiredResourceAccesses": lambda n : setattr(self, 'required_resource_accesses', n.get_collection_of_object_values(ApplicationsRequiredResourceAccess)),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("requiredResourceAccesses", self.required_resource_accesses)
        writer.write_additional_data_value(self.additional_data)
    

