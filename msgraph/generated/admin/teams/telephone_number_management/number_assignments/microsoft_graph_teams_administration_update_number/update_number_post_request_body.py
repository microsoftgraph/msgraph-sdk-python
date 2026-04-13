from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateNumberPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The locationId property
    location_id: Optional[str] = None
    # The networkSiteId property
    network_site_id: Optional[str] = None
    # The reverseNumberLookupOptions property
    reverse_number_lookup_options: Optional[list[str]] = None
    # The telephoneNumber property
    telephone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateNumberPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateNumberPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateNumberPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "locationId": lambda n : setattr(self, 'location_id', n.get_str_value()),
            "networkSiteId": lambda n : setattr(self, 'network_site_id', n.get_str_value()),
            "reverseNumberLookupOptions": lambda n : setattr(self, 'reverse_number_lookup_options', n.get_collection_of_primitive_values(str)),
            "telephoneNumber": lambda n : setattr(self, 'telephone_number', n.get_str_value()),
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
        writer.write_str_value("locationId", self.location_id)
        writer.write_str_value("networkSiteId", self.network_site_id)
        writer.write_collection_of_primitive_values("reverseNumberLookupOptions", self.reverse_number_lookup_options)
        writer.write_str_value("telephoneNumber", self.telephone_number)
        writer.write_additional_data_value(self.additional_data)
    

