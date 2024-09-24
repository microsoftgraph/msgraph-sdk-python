from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.security.ediscovery_review_tag import EdiscoveryReviewTag
    from ......models.security.ediscovery_review_tag_collection_response import EdiscoveryReviewTagCollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .item.ediscovery_review_tag_item_request_builder import EdiscoveryReviewTagItemRequestBuilder
    from .microsoft_graph_security_as_hierarchy.microsoft_graph_security_as_hierarchy_request_builder import MicrosoftGraphSecurityAsHierarchyRequestBuilder

class TagsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TagsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/tags{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_ediscovery_review_tag_id(self,ediscovery_review_tag_id: str) -> EdiscoveryReviewTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
        param ediscovery_review_tag_id: The unique identifier of ediscoveryReviewTag
        Returns: EdiscoveryReviewTagItemRequestBuilder
        """
        if ediscovery_review_tag_id is None:
            raise TypeError("ediscovery_review_tag_id cannot be null.")
        from .item.ediscovery_review_tag_item_request_builder import EdiscoveryReviewTagItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryReviewTag%2Did"] = ediscovery_review_tag_id
        return EdiscoveryReviewTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TagsRequestBuilderGetQueryParameters]] = None) -> Optional[EdiscoveryReviewTagCollectionResponse]:
        """
        Get a list of eDiscoveryReviewTag objects and their properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryReviewTagCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-list-tags?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security.ediscovery_review_tag_collection_response import EdiscoveryReviewTagCollectionResponse

        return await self.request_adapter.send_async(request_info, EdiscoveryReviewTagCollectionResponse, error_mapping)
    
    async def post(self,body: EdiscoveryReviewTag, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EdiscoveryReviewTag]:
        """
        Create a new ediscoveryReviewTag object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryReviewTag]
        Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-post-tags?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security.ediscovery_review_tag import EdiscoveryReviewTag

        return await self.request_adapter.send_async(request_info, EdiscoveryReviewTag, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TagsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a list of eDiscoveryReviewTag objects and their properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: EdiscoveryReviewTag, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new ediscoveryReviewTag object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TagsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TagsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TagsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_as_hierarchy(self) -> MicrosoftGraphSecurityAsHierarchyRequestBuilder:
        """
        Provides operations to call the asHierarchy method.
        """
        from .microsoft_graph_security_as_hierarchy.microsoft_graph_security_as_hierarchy_request_builder import MicrosoftGraphSecurityAsHierarchyRequestBuilder

        return MicrosoftGraphSecurityAsHierarchyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TagsRequestBuilderGetQueryParameters():
        """
        Get a list of eDiscoveryReviewTag objects and their properties.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class TagsRequestBuilderGetRequestConfiguration(RequestConfiguration[TagsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TagsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

