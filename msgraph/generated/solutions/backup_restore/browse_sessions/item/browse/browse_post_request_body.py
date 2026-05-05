from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.browsable_resource_type import BrowsableResourceType
    from ......models.browse_query_order import BrowseQueryOrder

@dataclass
class BrowsePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The browseLocationItemKey property
    browse_location_item_key: Optional[str] = None
    # The browseResourceType property
    browse_resource_type: Optional[BrowsableResourceType] = None
    # The filter property
    filter: Optional[str] = None
    # The orderBy property
    order_by: Optional[BrowseQueryOrder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowsePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowsePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BrowsePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.browsable_resource_type import BrowsableResourceType
        from ......models.browse_query_order import BrowseQueryOrder

        from ......models.browsable_resource_type import BrowsableResourceType
        from ......models.browse_query_order import BrowseQueryOrder

        fields: dict[str, Callable[[Any], None]] = {
            "browseLocationItemKey": lambda n : setattr(self, 'browse_location_item_key', n.get_str_value()),
            "browseResourceType": lambda n : setattr(self, 'browse_resource_type', n.get_enum_value(BrowsableResourceType)),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "orderBy": lambda n : setattr(self, 'order_by', n.get_enum_value(BrowseQueryOrder)),
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
        writer.write_str_value("browseLocationItemKey", self.browse_location_item_key)
        writer.write_enum_value("browseResourceType", self.browse_resource_type)
        writer.write_str_value("filter", self.filter)
        writer.write_enum_value("orderBy", self.order_by)
        writer.write_additional_data_value(self.additional_data)
    

