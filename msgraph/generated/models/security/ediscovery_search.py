from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_source = lazy_import('msgraph.generated.models.security.data_source')
data_source_scopes = lazy_import('msgraph.generated.models.security.data_source_scopes')
ediscovery_add_to_review_set_operation = lazy_import('msgraph.generated.models.security.ediscovery_add_to_review_set_operation')
ediscovery_estimate_operation = lazy_import('msgraph.generated.models.security.ediscovery_estimate_operation')
ediscovery_noncustodial_data_source = lazy_import('msgraph.generated.models.security.ediscovery_noncustodial_data_source')
search = lazy_import('msgraph.generated.models.security.search')

class EdiscoverySearch(search.Search):
    @property
    def additional_sources(self,) -> Optional[List[data_source.DataSource]]:
        """
        Gets the additionalSources property value. Adds an additional source to the eDiscovery search.
        Returns: Optional[List[data_source.DataSource]]
        """
        return self._additional_sources
    
    @additional_sources.setter
    def additional_sources(self,value: Optional[List[data_source.DataSource]] = None) -> None:
        """
        Sets the additionalSources property value. Adds an additional source to the eDiscovery search.
        Args:
            value: Value to set for the additionalSources property.
        """
        self._additional_sources = value
    
    @property
    def add_to_review_set_operation(self,) -> Optional[ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation]:
        """
        Gets the addToReviewSetOperation property value. Adds the results of the eDiscovery search to the specified reviewSet.
        Returns: Optional[ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation]
        """
        return self._add_to_review_set_operation
    
    @add_to_review_set_operation.setter
    def add_to_review_set_operation(self,value: Optional[ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation] = None) -> None:
        """
        Sets the addToReviewSetOperation property value. Adds the results of the eDiscovery search to the specified reviewSet.
        Args:
            value: Value to set for the addToReviewSetOperation property.
        """
        self._add_to_review_set_operation = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoverySearch and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoverySearch"
        # Adds an additional source to the eDiscovery search.
        self._additional_sources: Optional[List[data_source.DataSource]] = None
        # Adds the results of the eDiscovery search to the specified reviewSet.
        self._add_to_review_set_operation: Optional[ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation] = None
        # Custodian sources that are included in the eDiscovery search.
        self._custodian_sources: Optional[List[data_source.DataSource]] = None
        # When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        self._data_source_scopes: Optional[data_source_scopes.DataSourceScopes] = None
        # The last estimate operation associated with the eDiscovery search.
        self._last_estimate_statistics_operation: Optional[ediscovery_estimate_operation.EdiscoveryEstimateOperation] = None
        # noncustodialDataSource sources that are included in the eDiscovery search
        self._noncustodial_sources: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None
    
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
    
    @property
    def custodian_sources(self,) -> Optional[List[data_source.DataSource]]:
        """
        Gets the custodianSources property value. Custodian sources that are included in the eDiscovery search.
        Returns: Optional[List[data_source.DataSource]]
        """
        return self._custodian_sources
    
    @custodian_sources.setter
    def custodian_sources(self,value: Optional[List[data_source.DataSource]] = None) -> None:
        """
        Sets the custodianSources property value. Custodian sources that are included in the eDiscovery search.
        Args:
            value: Value to set for the custodianSources property.
        """
        self._custodian_sources = value
    
    @property
    def data_source_scopes(self,) -> Optional[data_source_scopes.DataSourceScopes]:
        """
        Gets the dataSourceScopes property value. When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        Returns: Optional[data_source_scopes.DataSourceScopes]
        """
        return self._data_source_scopes
    
    @data_source_scopes.setter
    def data_source_scopes(self,value: Optional[data_source_scopes.DataSourceScopes] = None) -> None:
        """
        Sets the dataSourceScopes property value. When specified, the collection will span across a service for an entire workload. Possible values are: none, allTenantMailboxes, allTenantSites, allCaseCustodians, allCaseNoncustodialDataSources.
        Args:
            value: Value to set for the dataSourceScopes property.
        """
        self._data_source_scopes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_sources": lambda n : setattr(self, 'additional_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "add_to_review_set_operation": lambda n : setattr(self, 'add_to_review_set_operation', n.get_object_value(ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation)),
            "custodian_sources": lambda n : setattr(self, 'custodian_sources', n.get_collection_of_object_values(data_source.DataSource)),
            "data_source_scopes": lambda n : setattr(self, 'data_source_scopes', n.get_enum_value(data_source_scopes.DataSourceScopes)),
            "last_estimate_statistics_operation": lambda n : setattr(self, 'last_estimate_statistics_operation', n.get_object_value(ediscovery_estimate_operation.EdiscoveryEstimateOperation)),
            "noncustodial_sources": lambda n : setattr(self, 'noncustodial_sources', n.get_collection_of_object_values(ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_estimate_statistics_operation(self,) -> Optional[ediscovery_estimate_operation.EdiscoveryEstimateOperation]:
        """
        Gets the lastEstimateStatisticsOperation property value. The last estimate operation associated with the eDiscovery search.
        Returns: Optional[ediscovery_estimate_operation.EdiscoveryEstimateOperation]
        """
        return self._last_estimate_statistics_operation
    
    @last_estimate_statistics_operation.setter
    def last_estimate_statistics_operation(self,value: Optional[ediscovery_estimate_operation.EdiscoveryEstimateOperation] = None) -> None:
        """
        Sets the lastEstimateStatisticsOperation property value. The last estimate operation associated with the eDiscovery search.
        Args:
            value: Value to set for the lastEstimateStatisticsOperation property.
        """
        self._last_estimate_statistics_operation = value
    
    @property
    def noncustodial_sources(self,) -> Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]]:
        """
        Gets the noncustodialSources property value. noncustodialDataSource sources that are included in the eDiscovery search
        Returns: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]]
        """
        return self._noncustodial_sources
    
    @noncustodial_sources.setter
    def noncustodial_sources(self,value: Optional[List[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]] = None) -> None:
        """
        Sets the noncustodialSources property value. noncustodialDataSource sources that are included in the eDiscovery search
        Args:
            value: Value to set for the noncustodialSources property.
        """
        self._noncustodial_sources = value
    
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
    

