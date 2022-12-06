from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

search_aggregation = lazy_import('msgraph.generated.models.search_aggregation')
search_hit = lazy_import('msgraph.generated.models.search_hit')

class SearchHitsContainer(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def aggregations(self,) -> Optional[List[search_aggregation.SearchAggregation]]:
        """
        Gets the aggregations property value. The aggregations property
        Returns: Optional[List[search_aggregation.SearchAggregation]]
        """
        return self._aggregations
    
    @aggregations.setter
    def aggregations(self,value: Optional[List[search_aggregation.SearchAggregation]] = None) -> None:
        """
        Sets the aggregations property value. The aggregations property
        Args:
            value: Value to set for the aggregations property.
        """
        self._aggregations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new searchHitsContainer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The aggregations property
        self._aggregations: Optional[List[search_aggregation.SearchAggregation]] = None
        # A collection of the search results.
        self._hits: Optional[List[search_hit.SearchHit]] = None
        # Provides information if more results are available. Based on this information, you can adjust the from and size properties of the searchRequest accordingly.
        self._more_results_available: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The total number of results. Note this is not the number of results on the page, but the total number of results satisfying the query.
        self._total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchHitsContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchHitsContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchHitsContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(search_aggregation.SearchAggregation)),
            "hits": lambda n : setattr(self, 'hits', n.get_collection_of_object_values(search_hit.SearchHit)),
            "more_results_available": lambda n : setattr(self, 'more_results_available', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        return fields
    
    @property
    def hits(self,) -> Optional[List[search_hit.SearchHit]]:
        """
        Gets the hits property value. A collection of the search results.
        Returns: Optional[List[search_hit.SearchHit]]
        """
        return self._hits
    
    @hits.setter
    def hits(self,value: Optional[List[search_hit.SearchHit]] = None) -> None:
        """
        Sets the hits property value. A collection of the search results.
        Args:
            value: Value to set for the hits property.
        """
        self._hits = value
    
    @property
    def more_results_available(self,) -> Optional[bool]:
        """
        Gets the moreResultsAvailable property value. Provides information if more results are available. Based on this information, you can adjust the from and size properties of the searchRequest accordingly.
        Returns: Optional[bool]
        """
        return self._more_results_available
    
    @more_results_available.setter
    def more_results_available(self,value: Optional[bool] = None) -> None:
        """
        Sets the moreResultsAvailable property value. Provides information if more results are available. Based on this information, you can adjust the from and size properties of the searchRequest accordingly.
        Args:
            value: Value to set for the moreResultsAvailable property.
        """
        self._more_results_available = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_collection_of_object_values("hits", self.hits)
        writer.write_bool_value("moreResultsAvailable", self.more_results_available)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total(self,) -> Optional[int]:
        """
        Gets the total property value. The total number of results. Note this is not the number of results on the page, but the total number of results satisfying the query.
        Returns: Optional[int]
        """
        return self._total
    
    @total.setter
    def total(self,value: Optional[int] = None) -> None:
        """
        Sets the total property value. The total number of results. Note this is not the number of results on the page, but the total number of results satisfying the query.
        Args:
            value: Value to set for the total property.
        """
        self._total = value
    

