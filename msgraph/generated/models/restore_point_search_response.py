from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_point_search_result import RestorePointSearchResult

@dataclass
class RestorePointSearchResponse(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Contains  alist of protection units with no restore points.
    no_result_protection_unit_ids: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the search response.
    search_response_id: Optional[str] = None
    # Contains a collection of restore points.
    search_results: Optional[list[RestorePointSearchResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestorePointSearchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestorePointSearchResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestorePointSearchResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .restore_point_search_result import RestorePointSearchResult

        from .restore_point_search_result import RestorePointSearchResult

        fields: dict[str, Callable[[Any], None]] = {
            "noResultProtectionUnitIds": lambda n : setattr(self, 'no_result_protection_unit_ids', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "searchResponseId": lambda n : setattr(self, 'search_response_id', n.get_str_value()),
            "searchResults": lambda n : setattr(self, 'search_results', n.get_collection_of_object_values(RestorePointSearchResult)),
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
        writer.write_collection_of_primitive_values("noResultProtectionUnitIds", self.no_result_protection_unit_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("searchResponseId", self.search_response_id)
        writer.write_collection_of_object_values("searchResults", self.search_results)
        writer.write_additional_data_value(self.additional_data)
    

