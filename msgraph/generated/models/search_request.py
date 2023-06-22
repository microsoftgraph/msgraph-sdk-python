from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

@dataclass
class SearchRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The aggregationFilters property
    aggregation_filters: Optional[List[str]] = None
    # The aggregations property
    aggregations: Optional[List[aggregation_option.AggregationOption]] = None
    # The collapseProperties property
    collapse_properties: Optional[List[collapse_property.CollapseProperty]] = None
    # The contentSources property
    content_sources: Optional[List[str]] = None
    # The enableTopResults property
    enable_top_results: Optional[bool] = None
    # The entityTypes property
    entity_types: Optional[List[entity_type.EntityType]] = None
    # The fields property
    fields: Optional[List[str]] = None
    # The from property
    from_: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The query property
    query: Optional[search_query.SearchQuery] = None
    # The queryAlterationOptions property
    query_alteration_options: Optional[search_alteration_options.SearchAlterationOptions] = None
    # The region property
    region: Optional[str] = None
    # The resultTemplateOptions property
    result_template_options: Optional[result_template_option.ResultTemplateOption] = None
    # The sharePointOneDriveOptions property
    share_point_one_drive_options: Optional[share_point_one_drive_options.SharePointOneDriveOptions] = None
    # The size property
    size: Optional[int] = None
    # The sortProperties property
    sort_properties: Optional[List[sort_property.SortProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SearchRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

        from . import aggregation_option, collapse_property, entity_type, result_template_option, search_alteration_options, search_query, share_point_one_drive_options, sort_property

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregationFilters": lambda n : setattr(self, 'aggregation_filters', n.get_collection_of_primitive_values(str)),
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(aggregation_option.AggregationOption)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("aggregationFilters", self.aggregation_filters)
        writer.write_collection_of_object_values("aggregations", self.aggregations)
        writer.write_collection_of_object_values("collapseProperties", self.collapse_properties)
        writer.write_collection_of_primitive_values("contentSources", self.content_sources)
        writer.write_bool_value("enableTopResults", self.enable_top_results)
        writer.write_collection_of_enum_values("entityTypes", self.entity_types)
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
    

