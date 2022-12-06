from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

bucket_aggregation_definition = lazy_import('msgraph.generated.models.bucket_aggregation_definition')

class AggregationOption(AdditionalDataHolder, Parsable):
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
    def bucket_definition(self,) -> Optional[bucket_aggregation_definition.BucketAggregationDefinition]:
        """
        Gets the bucketDefinition property value. The bucketDefinition property
        Returns: Optional[bucket_aggregation_definition.BucketAggregationDefinition]
        """
        return self._bucket_definition
    
    @bucket_definition.setter
    def bucket_definition(self,value: Optional[bucket_aggregation_definition.BucketAggregationDefinition] = None) -> None:
        """
        Sets the bucketDefinition property value. The bucketDefinition property
        Args:
            value: Value to set for the bucketDefinition property.
        """
        self._bucket_definition = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new aggregationOption and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The bucketDefinition property
        self._bucket_definition: Optional[bucket_aggregation_definition.BucketAggregationDefinition] = None
        # Computes aggregation on the field while the field exists in current entity type. Required.
        self._field: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of searchBucket resources to be returned. This is not required when the range is provided manually in the search request. Optional.
        self._size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AggregationOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AggregationOption
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AggregationOption()
    
    @property
    def field(self,) -> Optional[str]:
        """
        Gets the field property value. Computes aggregation on the field while the field exists in current entity type. Required.
        Returns: Optional[str]
        """
        return self._field
    
    @field.setter
    def field(self,value: Optional[str] = None) -> None:
        """
        Sets the field property value. Computes aggregation on the field while the field exists in current entity type. Required.
        Args:
            value: Value to set for the field property.
        """
        self._field = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bucket_definition": lambda n : setattr(self, 'bucket_definition', n.get_object_value(bucket_aggregation_definition.BucketAggregationDefinition)),
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        return fields
    
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
        writer.write_object_value("bucketDefinition", self.bucket_definition)
        writer.write_str_value("field", self.field)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The number of searchBucket resources to be returned. This is not required when the range is provided manually in the search request. Optional.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The number of searchBucket resources to be returned. This is not required when the range is provided manually in the search request. Optional.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

