from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bucket_aggregation_range = lazy_import('msgraph.generated.models.bucket_aggregation_range')
bucket_aggregation_sort_property = lazy_import('msgraph.generated.models.bucket_aggregation_sort_property')

class BucketAggregationDefinition(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new bucketAggregationDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # True to specify the sort order as descending. The default is false, with the sort order as ascending. Optional.
        self._is_descending: Optional[bool] = None
        # The minimum number of items that should be present in the aggregation to be returned in a bucket. Optional.
        self._minimum_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A filter to define a matching criteria. The key should start with the specified prefix to be returned in the response. Optional.
        self._prefix_filter: Optional[str] = None
        # Specifies the manual ranges to compute the aggregations. This is only valid for non-string refiners of date or numeric type. Optional.
        self._ranges: Optional[List[bucket_aggregation_range.BucketAggregationRange]] = None
        # The sortBy property
        self._sort_by: Optional[bucket_aggregation_sort_property.BucketAggregationSortProperty] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BucketAggregationDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BucketAggregationDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BucketAggregationDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_descending": lambda n : setattr(self, 'is_descending', n.get_bool_value()),
            "minimum_count": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prefix_filter": lambda n : setattr(self, 'prefix_filter', n.get_str_value()),
            "ranges": lambda n : setattr(self, 'ranges', n.get_collection_of_object_values(bucket_aggregation_range.BucketAggregationRange)),
            "sort_by": lambda n : setattr(self, 'sort_by', n.get_enum_value(bucket_aggregation_sort_property.BucketAggregationSortProperty)),
        }
        return fields
    
    @property
    def is_descending(self,) -> Optional[bool]:
        """
        Gets the isDescending property value. True to specify the sort order as descending. The default is false, with the sort order as ascending. Optional.
        Returns: Optional[bool]
        """
        return self._is_descending
    
    @is_descending.setter
    def is_descending(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDescending property value. True to specify the sort order as descending. The default is false, with the sort order as ascending. Optional.
        Args:
            value: Value to set for the isDescending property.
        """
        self._is_descending = value
    
    @property
    def minimum_count(self,) -> Optional[int]:
        """
        Gets the minimumCount property value. The minimum number of items that should be present in the aggregation to be returned in a bucket. Optional.
        Returns: Optional[int]
        """
        return self._minimum_count
    
    @minimum_count.setter
    def minimum_count(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumCount property value. The minimum number of items that should be present in the aggregation to be returned in a bucket. Optional.
        Args:
            value: Value to set for the minimumCount property.
        """
        self._minimum_count = value
    
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
    
    @property
    def prefix_filter(self,) -> Optional[str]:
        """
        Gets the prefixFilter property value. A filter to define a matching criteria. The key should start with the specified prefix to be returned in the response. Optional.
        Returns: Optional[str]
        """
        return self._prefix_filter
    
    @prefix_filter.setter
    def prefix_filter(self,value: Optional[str] = None) -> None:
        """
        Sets the prefixFilter property value. A filter to define a matching criteria. The key should start with the specified prefix to be returned in the response. Optional.
        Args:
            value: Value to set for the prefixFilter property.
        """
        self._prefix_filter = value
    
    @property
    def ranges(self,) -> Optional[List[bucket_aggregation_range.BucketAggregationRange]]:
        """
        Gets the ranges property value. Specifies the manual ranges to compute the aggregations. This is only valid for non-string refiners of date or numeric type. Optional.
        Returns: Optional[List[bucket_aggregation_range.BucketAggregationRange]]
        """
        return self._ranges
    
    @ranges.setter
    def ranges(self,value: Optional[List[bucket_aggregation_range.BucketAggregationRange]] = None) -> None:
        """
        Sets the ranges property value. Specifies the manual ranges to compute the aggregations. This is only valid for non-string refiners of date or numeric type. Optional.
        Args:
            value: Value to set for the ranges property.
        """
        self._ranges = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isDescending", self.is_descending)
        writer.write_int_value("minimumCount", self.minimum_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("prefixFilter", self.prefix_filter)
        writer.write_collection_of_object_values("ranges", self.ranges)
        writer.write_enum_value("sortBy", self.sort_by)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sort_by(self,) -> Optional[bucket_aggregation_sort_property.BucketAggregationSortProperty]:
        """
        Gets the sortBy property value. The sortBy property
        Returns: Optional[bucket_aggregation_sort_property.BucketAggregationSortProperty]
        """
        return self._sort_by
    
    @sort_by.setter
    def sort_by(self,value: Optional[bucket_aggregation_sort_property.BucketAggregationSortProperty] = None) -> None:
        """
        Sets the sortBy property value. The sortBy property
        Args:
            value: Value to set for the sortBy property.
        """
        self._sort_by = value
    

