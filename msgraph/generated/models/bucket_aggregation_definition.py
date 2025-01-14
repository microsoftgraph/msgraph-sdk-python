from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bucket_aggregation_range import BucketAggregationRange
    from .bucket_aggregation_sort_property import BucketAggregationSortProperty

@dataclass
class BucketAggregationDefinition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # True to specify the sort order as descending. The default is false, with the sort order as ascending. Optional.
    is_descending: Optional[bool] = None
    # The minimum number of items that should be present in the aggregation to be returned in a bucket. Optional.
    minimum_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A filter to define a matching criteria. The key should start with the specified prefix to be returned in the response. Optional.
    prefix_filter: Optional[str] = None
    # Specifies the manual ranges to compute the aggregations. This is only valid for nonstring refiners of date or numeric type. Optional.
    ranges: Optional[list[BucketAggregationRange]] = None
    # The sortBy property
    sort_by: Optional[BucketAggregationSortProperty] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BucketAggregationDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BucketAggregationDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BucketAggregationDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bucket_aggregation_range import BucketAggregationRange
        from .bucket_aggregation_sort_property import BucketAggregationSortProperty

        from .bucket_aggregation_range import BucketAggregationRange
        from .bucket_aggregation_sort_property import BucketAggregationSortProperty

        fields: dict[str, Callable[[Any], None]] = {
            "isDescending": lambda n : setattr(self, 'is_descending', n.get_bool_value()),
            "minimumCount": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prefixFilter": lambda n : setattr(self, 'prefix_filter', n.get_str_value()),
            "ranges": lambda n : setattr(self, 'ranges', n.get_collection_of_object_values(BucketAggregationRange)),
            "sortBy": lambda n : setattr(self, 'sort_by', n.get_enum_value(BucketAggregationSortProperty)),
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
        writer.write_bool_value("isDescending", self.is_descending)
        writer.write_int_value("minimumCount", self.minimum_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("prefixFilter", self.prefix_filter)
        writer.write_collection_of_object_values("ranges", self.ranges)
        writer.write_enum_value("sortBy", self.sort_by)
        writer.write_additional_data_value(self.additional_data)
    

