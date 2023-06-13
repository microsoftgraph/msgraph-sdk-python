from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import search_aggregation, search_hit

@dataclass
class SearchHitsContainer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The aggregations property
    aggregations: Optional[List[search_aggregation.SearchAggregation]] = None
    # A collection of the search results.
    hits: Optional[List[search_hit.SearchHit]] = None
    # Provides information if more results are available. Based on this information, you can adjust the from and size properties of the searchRequest accordingly.
    more_results_available: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of results. Note this is not the number of results on the page, but the total number of results satisfying the query.
    total: Optional[int] = None
    
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
        from . import search_aggregation, search_hit

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(search_aggregation.SearchAggregation)),
            "hits": lambda n : setattr(self, 'hits', n.get_collection_of_object_values(search_hit.SearchHit)),
            "moreResultsAvailable": lambda n : setattr(self, 'more_results_available', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        return fields
    
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
    

