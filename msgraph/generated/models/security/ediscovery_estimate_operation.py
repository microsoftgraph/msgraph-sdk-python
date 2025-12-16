from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .case_operation import CaseOperation
    from .ediscovery_search import EdiscoverySearch
    from .report_file_metadata import ReportFileMetadata
    from .statistics_options import StatisticsOptions

from .case_operation import CaseOperation

@dataclass
class EdiscoveryEstimateOperation(CaseOperation, Parsable):
    # The estimated count of items for the search that matched the content query.
    indexed_item_count: Optional[int] = None
    # The estimated size of items for the search that matched the content query.
    indexed_items_size: Optional[int] = None
    # The number of mailboxes that had search hits.
    mailbox_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the properties for report file metadata, including downloadUrl, fileName, and size.
    report_file_metadata: Optional[list[ReportFileMetadata]] = None
    # eDiscovery search.
    search: Optional[EdiscoverySearch] = None
    # The number of mailboxes that had search hits.
    site_count: Optional[int] = None
    # The options to generate statistics. The possible values are: includeRefiners, includeQueryStats, includeUnindexedStats, advancedIndexing, locationsWithoutHits, unknownFutureValue.
    statistics_options: Optional[StatisticsOptions] = None
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
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch
        from .report_file_metadata import ReportFileMetadata
        from .statistics_options import StatisticsOptions

        from .case_operation import CaseOperation
        from .ediscovery_search import EdiscoverySearch
        from .report_file_metadata import ReportFileMetadata
        from .statistics_options import StatisticsOptions

        fields: dict[str, Callable[[Any], None]] = {
            "indexedItemCount": lambda n : setattr(self, 'indexed_item_count', n.get_int_value()),
            "indexedItemsSize": lambda n : setattr(self, 'indexed_items_size', n.get_int_value()),
            "mailboxCount": lambda n : setattr(self, 'mailbox_count', n.get_int_value()),
            "reportFileMetadata": lambda n : setattr(self, 'report_file_metadata', n.get_collection_of_object_values(ReportFileMetadata)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
            "siteCount": lambda n : setattr(self, 'site_count', n.get_int_value()),
            "statisticsOptions": lambda n : setattr(self, 'statistics_options', n.get_collection_of_enum_values(StatisticsOptions)),
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
        writer.write_collection_of_object_values("reportFileMetadata", self.report_file_metadata)
        writer.write_object_value("search", self.search)
        writer.write_int_value("siteCount", self.site_count)
        writer.write_enum_value("statisticsOptions", self.statistics_options)
        writer.write_int_value("unindexedItemCount", self.unindexed_item_count)
        writer.write_int_value("unindexedItemsSize", self.unindexed_items_size)
    

