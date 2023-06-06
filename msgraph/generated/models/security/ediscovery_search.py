from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_source, data_source_scopes, ediscovery_add_to_review_set_operation, ediscovery_estimate_operation, ediscovery_noncustodial_data_source, search

from . import search

@dataclass
class EdiscoverySearch(search.Search):
    odata_type = "#microsoft.graph.security.ediscoverySearch"
    # Adds the results of the eDiscovery search to the specified reviewSet.
    add_to_review_set_operation: Optional[ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation] = None
    # Adds an additional source to the eDiscovery search.
    additional_sources: Optional[List[data_source.DataSource]] = None
    # Custodian sources that are included in the eDiscovery search.
    custodian_sources: Optional[List[data_source.DataSource]] = None
    # When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
    data_source_scopes: Optional[data_source_scopes.DataSourceScopes] = None
    # The last estimate operation associated with the eDiscovery search.
    last_estimate_statistics_operation: Optional[ediscovery_estimate_operation.EdiscoveryEstimateOperation] = None
    # noncustodialDataSource sources that are included in the eDiscovery search
    noncustodial_sources: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoverySearch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoverySearch
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoverySearch()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_source, data_source_scopes, ediscovery_add_to_review_set_operation, ediscovery_estimate_operation, ediscovery_noncustodial_data_source, search

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalSources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "addToReviewSetOperation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation)),
            "custodianSources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "dataSourceScopes": lambda n : setattr(self, 'data_source_scopes', n.get_enum_value(data_source_scopes.DataSourceScopes)),
            "lastEstimateStatisticsOperation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(ediscovery_estimate_operation.EdiscoveryEstimateOperation)),
            "noncustodialSources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalSources", self.additional_sources)
        writer.write_object_value("addToReviewSetOperation", self.add_to_review_set_operation)
        writer.write_collection_of_object_values("custodianSources", self.custodian_sources)
        writer.write_enum_value("dataSourceScopes", self.data_source_scopes)
        writer.write_object_value("lastEstimateStatisticsOperation", self.last_estimate_statistics_operation)
        writer.write_collection_of_object_values("noncustodialSources", self.noncustodial_sources)
    

