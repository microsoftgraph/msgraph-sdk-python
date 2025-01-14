from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AssociateWithHubSitesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The hubSiteUrls property
    hub_site_urls: Optional[list[str]] = None
    # The propagateToExistingLists property
    propagate_to_existing_lists: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssociateWithHubSitesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssociateWithHubSitesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssociateWithHubSitesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hubSiteUrls": lambda n : setattr(self, 'hub_site_urls', n.get_collection_of_primitive_values(str)),
            "propagateToExistingLists": lambda n : setattr(self, 'propagate_to_existing_lists', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("hubSiteUrls", self.hub_site_urls)
        writer.write_bool_value("propagateToExistingLists", self.propagate_to_existing_lists)
        writer.write_additional_data_value(self.additional_data)
    

