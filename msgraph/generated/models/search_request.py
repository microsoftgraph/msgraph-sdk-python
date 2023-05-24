from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

class SearchRequest(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new searchRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The aggregationFilters property
        self._aggregation_filters: Optional[List[str]] = None
        # The aggregations property
        self._aggregations: Optional[List[aggregation_option.AggregationOption]] = None
        # The collapseProperties property
        self._collapse_properties: Optional[List[collapse_property.CollapseProperty]] = None
        # The contentSources property
        self._content_sources: Optional[List[str]] = None
        # The enableTopResults property
        self._enable_top_results: Optional[bool] = None
        # The entityTypes property
        self._entity_types: Optional[List[entity_type.EntityType]] = None
        # The fields property
        self._fields: Optional[List[str]] = None
        # The from property
        self._from_: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The query property
        self._query: Optional[search_query.SearchQuery] = None
        # The queryAlterationOptions property
        self._query_alteration_options: Optional[search_alteration_options.SearchAlterationOptions] = None
        # The region property
        self._region: Optional[str] = None
        # The resultTemplateOptions property
        self._result_template_options: Optional[result_template_option.ResultTemplateOption] = None
        # The sharePointOneDriveOptions property
        self._share_point_one_drive_options: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None
        # The size property
        self._size: Optional[int] = None
        # The sortProperties property
        self._sort_properties: Optional[List[sort_property.SortProperty]] = None
    
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
    def aggregation_filters(self,) -> Optional[List[str]]:
        """
        Gets the aggregationFilters property value. The aggregationFilters property
        Returns: Optional[List[str]]
        """
        return self._aggregation_filters
    
    @aggregation_filters.setter
    def aggregation_filters(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aggregationFilters property value. The aggregationFilters property
        Args:
            value: Value to set for the aggregation_filters property.
        """
        self._aggregation_filters = value
    
    @property
    def aggregations(self,) -> Optional[List[aggregation_option.AggregationOption]]:
        """
        Gets the aggregations property value. The aggregations property
        Returns: Optional[List[aggregation_option.AggregationOption]]
        """
        return self._aggregations
    
    @aggregations.setter
    def aggregations(self,value: Optional[List[aggregation_option.AggregationOption]] = None) -> None:
        """
        Sets the aggregations property value. The aggregations property
        Args:
            value: Value to set for the aggregations property.
        """
        self._aggregations = value
    
    @property
    def collapse_properties(self,) -> Optional[List[collapse_property.CollapseProperty]]:
        """
        Gets the collapseProperties property value. The collapseProperties property
        Returns: Optional[List[collapse_property.CollapseProperty]]
        """
        return self._collapse_properties
    
    @collapse_properties.setter
    def collapse_properties(self,value: Optional[List[collapse_property.CollapseProperty]] = None) -> None:
        """
        Sets the collapseProperties property value. The collapseProperties property
        Args:
            value: Value to set for the collapse_properties property.
        """
        self._collapse_properties = value
    
    @property
    def content_sources(self,) -> Optional[List[str]]:
        """
        Gets the contentSources property value. The contentSources property
        Returns: Optional[List[str]]
        """
        return self._content_sources
    
    @content_sources.setter
    def content_sources(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contentSources property value. The contentSources property
        Args:
            value: Value to set for the content_sources property.
        """
        self._content_sources = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchRequest()
    
    @property
    def enable_top_results(self,) -> Optional[bool]:
        """
        Gets the enableTopResults property value. The enableTopResults property
        Returns: Optional[bool]
        """
        return self._enable_top_results
    
    @enable_top_results.setter
    def enable_top_results(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableTopResults property value. The enableTopResults property
        Args:
            value: Value to set for the enable_top_results property.
        """
        self._enable_top_results = value
    
    @property
    def entity_types(self,) -> Optional[List[entity_type.EntityType]]:
        """
        Gets the entityTypes property value. The entityTypes property
        Returns: Optional[List[entity_type.EntityType]]
        """
        return self._entity_types
    
    @entity_types.setter
    def entity_types(self,value: Optional[List[entity_type.EntityType]] = None) -> None:
        """
        Sets the entityTypes property value. The entityTypes property
        Args:
            value: Value to set for the entity_types property.
        """
        self._entity_types = value
    
    @property
    def fields(self,) -> Optional[List[str]]:
        """
        Gets the fields property value. The fields property
        Returns: Optional[List[str]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the fields property value. The fields property
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    @property
    def from_(self,) -> Optional[int]:
        """
        Gets the from property value. The from property
        Returns: Optional[int]
        """
        return self._from_
    
    @from_.setter
    def from_(self,value: Optional[int] = None) -> None:
        """
        Sets the from property value. The from property
        Args:
            value: Value to set for the from_ property.
        """
        self._from_ = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(aggregation_option.AggregationOption)),
            "aggregationFilters": lambda n : setattr(self, 'aggregation_filters', n.get_collection_of_primitive_values(str)),
            "collapseProperties": lambda n : setattr(self, 'collapse_properties', n.get_collection_of_object_values(collapse_property.CollapseProperty)),
            "contentSources": lambda n : setattr(self, 'content_sources', n.get_collection_of_primitive_values(str)),
            "enableTopResults": lambda n : setattr(self, 'enable_top_results', n.get_bool_value()),
            "entityTypes": lambda n : setattr(self, 'entity_types', n.get_collection_of_enum_values(entity_type.EntityType)),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "from": lambda n : setattr(self, 'from_', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_object_value(search_query.SearchQuery)),
            "queryAlterationOptions": lambda n : setattr(self, 'query_alteration_options', n.get_object_value(search_alteration_options.SearchAlterationOptions)),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "resultTemplateOptions": lambda n : setattr(self, 'result_template_options', n.get_object_value(result_template_option.ResultTemplateOption)),
            "sharePointOneDriveOptions": lambda n : setattr(self, 'share_point_one_drive_options', n.get_object_value(share_point_one_drive_options.SharePointOneDriveOptions)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sortProperties": lambda n : setattr(self, 'sort_properties', n.get_collection_of_object_values(sort_property.SortProperty)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def query(self,) -> Optional[search_query.SearchQuery]:
        """
        Gets the query property value. The query property
        Returns: Optional[search_query.SearchQuery]
        """
        return self._query
    
    @query.setter
    def query(self,value: Optional[search_query.SearchQuery] = None) -> None:
        """
        Sets the query property value. The query property
        Args:
            value: Value to set for the query property.
        """
        self._query = value
    
    @property
    def query_alteration_options(self,) -> Optional[search_alteration_options.SearchAlterationOptions]:
        """
        Gets the queryAlterationOptions property value. The queryAlterationOptions property
        Returns: Optional[search_alteration_options.SearchAlterationOptions]
        """
        return self._query_alteration_options
    
    @query_alteration_options.setter
    def query_alteration_options(self,value: Optional[search_alteration_options.SearchAlterationOptions] = None) -> None:
        """
        Sets the queryAlterationOptions property value. The queryAlterationOptions property
        Args:
            value: Value to set for the query_alteration_options property.
        """
        self._query_alteration_options = value
    
    @property
    def region(self,) -> Optional[str]:
        """
        Gets the region property value. The region property
        Returns: Optional[str]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[str] = None) -> None:
        """
        Sets the region property value. The region property
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    @property
    def result_template_options(self,) -> Optional[result_template_option.ResultTemplateOption]:
        """
        Gets the resultTemplateOptions property value. The resultTemplateOptions property
        Returns: Optional[result_template_option.ResultTemplateOption]
        """
        return self._result_template_options
    
    @result_template_options.setter
    def result_template_options(self,value: Optional[result_template_option.ResultTemplateOption] = None) -> None:
        """
        Sets the resultTemplateOptions property value. The resultTemplateOptions property
        Args:
            value: Value to set for the result_template_options property.
        """
        self._result_template_options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_collection_of_primitive_values("aggregationFilters", self.aggregation_filters)
        writer.write_collection_of_object_values("collapseProperties", self.collapse_properties)
        writer.write_collection_of_primitive_values("contentSources", self.content_sources)
        writer.write_bool_value("enableTopResults", self.enable_top_results)
        writer.write_enum_value("entityTypes", self.entity_types)
        writer.write_collection_of_primitive_values("fields", self.fields)
        writer.write_int_value("from", self.from_)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("query", self.query)
        writer.write_object_value("queryAlterationOptions", self.query_alteration_options)
        writer.write_str_value("region", self.region)
        writer.write_object_value("resultTemplateOptions", self.result_template_options)
        writer.write_object_value("sharePointOneDriveOptions", self.share_point_one_drive_options)
        writer.write_int_value("size", self.size)
        writer.write_collection_of_object_values("sortProperties", self.sort_properties)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def share_point_one_drive_options(self,) -> Optional[share_point_one_drive_options.SharePointOneDriveOptions]:
        """
        Gets the sharePointOneDriveOptions property value. The sharePointOneDriveOptions property
        Returns: Optional[share_point_one_drive_options.SharePointOneDriveOptions]
        """
        return self._share_point_one_drive_options
    
    @share_point_one_drive_options.setter
    def share_point_one_drive_options(self,value: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None) -> None:
        """
        Sets the sharePointOneDriveOptions property value. The sharePointOneDriveOptions property
        Args:
            value: Value to set for the share_point_one_drive_options property.
        """
        self._share_point_one_drive_options = value
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size property
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size property
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def sort_properties(self,) -> Optional[List[sort_property.SortProperty]]:
        """
        Gets the sortProperties property value. The sortProperties property
        Returns: Optional[List[sort_property.SortProperty]]
        """
        return self._sort_properties
    
    @sort_properties.setter
    def sort_properties(self,value: Optional[List[sort_property.SortProperty]] = None) -> None:
        """
        Sets the sortProperties property value. The sortProperties property
        Args:
            value: Value to set for the sort_properties property.
        """
        self._sort_properties = value
    

