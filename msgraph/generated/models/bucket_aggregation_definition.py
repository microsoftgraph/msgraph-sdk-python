from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bucket_aggregation_range, bucket_aggregation_sort_property

@dataclass
class BucketAggregationDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # True to specify the sort order as descending. The default is false, with the sort order as ascending. Optional.
    is_descending: Optional[bool] = None
    # The minimum number of items that should be present in the aggregation to be returned in a bucket. Optional.
    minimum_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A filter to define a matching criteria. The key should start with the specified prefix to be returned in the response. Optional.
    prefix_filter: Optional[str] = None
    # Specifies the manual ranges to compute the aggregations. This is only valid for non-string refiners of date or numeric type. Optional.
    ranges: Optional[List[bucket_aggregation_range.BucketAggregationRange]] = None
    # The sortBy property
    sort_by: Optional[bucket_aggregation_sort_property.BucketAggregationSortProperty] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BucketAggregationDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BucketAggregationDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BucketAggregationDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bucket_aggregation_range, bucket_aggregation_sort_property

        from . import bucket_aggregation_range, bucket_aggregation_sort_property

        fields: Dict[str, Callable[[Any], None]] = {
            "isDescending": lambda n : setattr(self, 'is_descending', n.get_bool_value()),
            "minimumCount": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prefixFilter": lambda n : setattr(self, 'prefix_filter', n.get_str_value()),
            "ranges": lambda n : setattr(self, 'ranges', n.get_collection_of_object_values(bucket_aggregation_range.BucketAggregationRange)),
            "sortBy": lambda n : setattr(self, 'sort_by', n.get_enum_value(bucket_aggregation_sort_property.BucketAggregationSortProperty)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isDescending", self.is_descending)
        writer.write_int_value("minimumCount", self.minimum_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("prefixFilter", self.prefix_filter)
        writer.write_collection_of_object_values("ranges", self.ranges)
        writer.write_enum_value("sortBy", self.sort_by)
        writer.write_additional_data_value(self.additional_data)
    

