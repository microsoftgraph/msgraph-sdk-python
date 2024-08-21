from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair

@dataclass
class SubjectRightsRequestDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Count of items that are excluded from the request.
    excluded_item_count: Optional[int] = None
    # Count of items per insight.
    insight_counts: Optional[List[KeyValuePair]] = None
    # Count of items found.
    item_count: Optional[int] = None
    # Count of item that need review.
    item_need_review: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Count of items per product, such as Exchange, SharePoint, OneDrive, and Teams.
    product_item_counts: Optional[List[KeyValuePair]] = None
    # Count of items signed off by the administrator.
    signed_off_item_count: Optional[int] = None
    # Total item size in bytes.
    total_item_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectRightsRequestDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair

        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "excludedItemCount": lambda n : setattr(self, 'excluded_item_count', n.get_int_value()),
            "insightCounts": lambda n : setattr(self, 'insight_counts', n.get_collection_of_object_values(KeyValuePair)),
            "itemCount": lambda n : setattr(self, 'item_count', n.get_int_value()),
            "itemNeedReview": lambda n : setattr(self, 'item_need_review', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "productItemCounts": lambda n : setattr(self, 'product_item_counts', n.get_collection_of_object_values(KeyValuePair)),
            "signedOffItemCount": lambda n : setattr(self, 'signed_off_item_count', n.get_int_value()),
            "totalItemSize": lambda n : setattr(self, 'total_item_size', n.get_int_value()),
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
        writer.write_int_value("excludedItemCount", self.excluded_item_count)
        writer.write_collection_of_object_values("insightCounts", self.insight_counts)
        writer.write_int_value("itemCount", self.item_count)
        writer.write_int_value("itemNeedReview", self.item_need_review)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("productItemCounts", self.product_item_counts)
        writer.write_int_value("signedOffItemCount", self.signed_off_item_count)
        writer.write_int_value("totalItemSize", self.total_item_size)
        writer.write_additional_data_value(self.additional_data)
    

