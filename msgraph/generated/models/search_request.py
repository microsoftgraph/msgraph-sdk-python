from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aggregation_option import AggregationOption
    from .collapse_property import CollapseProperty
    from .entity_type import EntityType
    from .result_template_option import ResultTemplateOption
    from .search_alteration_options import SearchAlterationOptions
    from .search_query import SearchQuery
    from .share_point_one_drive_options import SharePointOneDriveOptions
    from .sort_property import SortProperty

@dataclass
class SearchRequest(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Contains one or more filters to obtain search results aggregated and filtered to a specific value of a field. Optional.Build this filter based on a prior search that aggregates by the same field. From the response of the prior search, identify the searchBucket that filters results to the specific value of the field, use the string in its aggregationFilterToken property, and build an aggregation filter string in the format '{field}:/'{aggregationFilterToken}/''. If multiple values for the same field need to be provided, use the strings in its aggregationFilterToken property and build an aggregation filter string in the format '{field}:or(/'{aggregationFilterToken1}/',/'{aggregationFilterToken2}/')'. For example, searching and aggregating drive items by file type returns a searchBucket for the file type docx in the response. You can conveniently use the aggregationFilterToken returned for this searchBucket in a subsequent search query and filter matches down to drive items of the docx file type. Example 1 and example 2 show the actual requests and responses.
    aggregation_filters: Optional[list[str]] = None
    # Specifies aggregations (also known as refiners) to be returned alongside search results. Optional.
    aggregations: Optional[list[AggregationOption]] = None
    # Contains the ordered collection of fields and limit to collapse results. Optional.
    collapse_properties: Optional[list[CollapseProperty]] = None
    # Contains the connection to be targeted.
    content_sources: Optional[list[str]] = None
    # This triggers hybrid sort for messages : the first 3 messages are the most relevant. This property is only applicable to entityType=message. Optional.
    enable_top_results: Optional[bool] = None
    # One or more types of resources expected in the response. The possible values are: event, message, driveItem, externalItem, site, list, listItem, drive, chatMessage, person, acronym, bookmark.  Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: chatMessage, person, acronym, bookmark. See known limitations for those combinations of two or more entity types that are supported in the same search request. Required.
    entity_types: Optional[list[EntityType]] = None
    # Contains the fields to be returned for each resource object specified in entityTypes, allowing customization of the fields returned by default; otherwise, including additional fields such as custom managed properties from SharePoint and OneDrive, or custom fields in externalItem from the content that Microsoft 365 Copilot connectors bring in. The fields property can use the semantic labels applied to properties. For example, if a property is labeled as title, you can retrieve it using the following syntax: label_title. Optional.
    fields: Optional[list[str]] = None
    # Specifies the offset for the search results. Offset 0 returns the very first result. Optional.
    from_: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The query property
    query: Optional[SearchQuery] = None
    # Query alteration options formatted in a JSON blob that contains two optional flags related to spelling correction. Optional.
    query_alteration_options: Optional[SearchAlterationOptions] = None
    # The geographic location for the search. Required for searches that use application permissions. For details, see Get the region value.
    region: Optional[str] = None
    # Provides the search result template options to render search results from connectors.
    result_template_options: Optional[ResultTemplateOption] = None
    # Indicates the kind of contents to be searched when a search is performed using application permissions. Optional.
    share_point_one_drive_options: Optional[SharePointOneDriveOptions] = None
    # The size of the page to be retrieved. The maximum value is 500. Optional.
    size: Optional[int] = None
    # Contains the ordered collection of fields and direction to sort results. There can be at most 5 sort properties in the collection. Optional.
    sort_properties: Optional[list[SortProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aggregation_option import AggregationOption
        from .collapse_property import CollapseProperty
        from .entity_type import EntityType
        from .result_template_option import ResultTemplateOption
        from .search_alteration_options import SearchAlterationOptions
        from .search_query import SearchQuery
        from .share_point_one_drive_options import SharePointOneDriveOptions
        from .sort_property import SortProperty

        from .aggregation_option import AggregationOption
        from .collapse_property import CollapseProperty
        from .entity_type import EntityType
        from .result_template_option import ResultTemplateOption
        from .search_alteration_options import SearchAlterationOptions
        from .search_query import SearchQuery
        from .share_point_one_drive_options import SharePointOneDriveOptions
        from .sort_property import SortProperty

        fields: dict[str, Callable[[Any], None]] = {
            "aggregationFilters": lambda n : setattr(self, 'aggregation_filters', n.get_collection_of_primitive_values(str)),
            "aggregations": lambda n : setattr(self, 'aggregations', n.get_collection_of_object_values(AggregationOption)),
            "collapseProperties": lambda n : setattr(self, 'collapse_properties', n.get_collection_of_object_values(CollapseProperty)),
            "contentSources": lambda n : setattr(self, 'content_sources', n.get_collection_of_primitive_values(str)),
            "enableTopResults": lambda n : setattr(self, 'enable_top_results', n.get_bool_value()),
            "entityTypes": lambda n : setattr(self, 'entity_types', n.get_collection_of_enum_values(EntityType)),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_primitive_values(str)),
            "from": lambda n : setattr(self, 'from_', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_object_value(SearchQuery)),
            "queryAlterationOptions": lambda n : setattr(self, 'query_alteration_options', n.get_object_value(SearchAlterationOptions)),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "resultTemplateOptions": lambda n : setattr(self, 'result_template_options', n.get_object_value(ResultTemplateOption)),
            "sharePointOneDriveOptions": lambda n : setattr(self, 'share_point_one_drive_options', n.get_object_value(SharePointOneDriveOptions)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sortProperties": lambda n : setattr(self, 'sort_properties', n.get_collection_of_object_values(SortProperty)),
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
    

