from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .ediscovery_search import EdiscoverySearch

from .case_operation import CaseOperation

@dataclass
class EdiscoveryEstimateOperation(CaseOperation):
    # The estimated count of items for the search that matched the content query.
    indexed_item_count: Optional[int] = None
    # The estimated size of items for the search that matched the content query.
    indexed_items_size: Optional[int] = None
    # The number of mailboxes that had search hits.
    mailbox_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # eDiscovery search.
    search: Optional[EdiscoverySearch] = None
    # The number of mailboxes that had search hits.
    site_count: Optional[int] = None
    # The estimated count of unindexed items for the collection.
    unindexed_item_count: Optional[int] = None
    # The estimated size of unindexed items for the collection.
    unindexed_items_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryEstimateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryEstimateOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryEstimateOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch

        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch

        fields: Dict[str, Callable[[Any], None]] = {
            "indexedItemCount": lambda n : setattr(self, 'indexed_item_count', n.get_int_value()),
            "indexedItemsSize": lambda n : setattr(self, 'indexed_items_size', n.get_int_value()),
            "mailboxCount": lambda n : setattr(self, 'mailbox_count', n.get_int_value()),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
            "siteCount": lambda n : setattr(self, 'site_count', n.get_int_value()),
            "unindexedItemCount": lambda n : setattr(self, 'unindexed_item_count', n.get_int_value()),
            "unindexedItemsSize": lambda n : setattr(self, 'unindexed_items_size', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("indexedItemCount", self.indexed_item_count)
        writer.write_int_value("indexedItemsSize", self.indexed_items_size)
        writer.write_int_value("mailboxCount", self.mailbox_count)
        writer.write_object_value("search", self.search)
        writer.write_int_value("siteCount", self.site_count)
        writer.write_int_value("unindexedItemCount", self.unindexed_item_count)
        writer.write_int_value("unindexedItemsSize", self.unindexed_items_size)
    

