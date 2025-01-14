from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resource_access import ResourceAccess

@dataclass
class RequiredResourceAccess(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of OAuth2.0 permission scopes and app roles that the application requires from the specified resource.
    resource_access: Optional[list[ResourceAccess]] = None
    # The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
    resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequiredResourceAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequiredResourceAccess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequiredResourceAccess()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .resource_access import ResourceAccess

        from .resource_access import ResourceAccess

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceAccess": lambda n : setattr(self, 'resource_access', n.get_collection_of_object_values(ResourceAccess)),
            "resourceAppId": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("resourceAccess", self.resource_access)
        writer.write_str_value("resourceAppId", self.resource_app_id)
        writer.write_additional_data_value(self.additional_data)
    

