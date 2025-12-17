from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source import DataSource
    from .data_source_scopes import DataSourceScopes
    from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
    from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
    from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
    from .search import Search

from .search import Search

@dataclass
class EdiscoverySearch(Search, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoverySearch"
    # Adds the results of the eDiscovery search to the specified reviewSet.
    add_to_review_set_operation: Optional[EdiscoveryAddToReviewSetOperation] = None
    # Adds an additional source to the eDiscovery search.
    additional_sources: Optional[list[DataSource]] = None
    # Custodian sources that are included in the eDiscovery search.
    custodian_sources: Optional[list[DataSource]] = None
    # When specified, the collection spans across a service for an entire workload. The possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
    data_source_scopes: Optional[DataSourceScopes] = None
    # The last estimate operation associated with the eDiscovery search.
    last_estimate_statistics_operation: Optional[EdiscoveryEstimateOperation] = None
    # noncustodialDataSource sources that are included in the eDiscovery search
    noncustodial_sources: Optional[list[EdiscoveryNoncustodialDataSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoverySearch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoverySearch
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoverySearch()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_source import DataSource
        from .data_source_scopes import DataSourceScopes
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .search import Search

        from .data_source import DataSource
        from .data_source_scopes import DataSourceScopes
        from .ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .search import Search

        fields: dict[str, Callable[[Any], None]] = {
            "addToReviewSetOperation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(EdiscoveryAddToReviewSetOperation)),
            "additionalSources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(DataSource)),
            "custodianSources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(DataSource)),
            "dataSourceScopes": lambda n : setattr(self, 'data_source_scopes', n.get_collection_of_enum_values(DataSourceScopes)),
            "lastEstimateStatisticsOperation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(EdiscoveryEstimateOperation)),
            "noncustodialSources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(EdiscoveryNoncustodialDataSource)),
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
        writer.write_object_value("addToReviewSetOperation", self.add_to_review_set_operation)
        writer.write_collection_of_object_values("additionalSources", self.additional_sources)
        writer.write_collection_of_object_values("custodianSources", self.custodian_sources)
        writer.write_enum_value("dataSourceScopes", self.data_source_scopes)
        writer.write_object_value("lastEstimateStatisticsOperation", self.last_estimate_statistics_operation)
        writer.write_collection_of_object_values("noncustodialSources", self.noncustodial_sources)
    

