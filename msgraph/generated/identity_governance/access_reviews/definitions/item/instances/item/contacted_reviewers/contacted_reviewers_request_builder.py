from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ........models.access_review_reviewer import AccessReviewReviewer
    from ........models.access_review_reviewer_collection_response import AccessReviewReviewerCollectionResponse
    from ........models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.access_review_reviewer_item_request_builder import AccessReviewReviewerItemRequestBuilder

class ContactedReviewersRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the contactedReviewers property of the microsoft.graph.accessReviewInstance entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ContactedReviewersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}/instances/{accessReviewInstance%2Did}/contactedReviewers{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_access_review_reviewer_id(self,access_review_reviewer_id: str) -> AccessReviewReviewerItemRequestBuilder:
        """
        Provides operations to manage the contactedReviewers property of the microsoft.graph.accessReviewInstance entity.
        param access_review_reviewer_id: The unique identifier of accessReviewReviewer
        Returns: AccessReviewReviewerItemRequestBuilder
        """
        if access_review_reviewer_id is None:
            raise TypeError("access_review_reviewer_id cannot be null.")
        from .item.access_review_reviewer_item_request_builder import AccessReviewReviewerItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewReviewer%2Did"] = access_review_reviewer_id
        return AccessReviewReviewerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ContactedReviewersRequestBuilderGetQueryParameters]] = None) -> Optional[AccessReviewReviewerCollectionResponse]:
        """
        Get the reviewers for an access review instance, irrespective of whether or not they have received a notification. The reviewers are represented by an accessReviewReviewer object. A list of zero or more objects are returned, including all of their nested properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewReviewerCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/accessreviewinstance-list-contactedreviewers?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.access_review_reviewer_collection_response import AccessReviewReviewerCollectionResponse

        return await self.request_adapter.send_async(request_info, AccessReviewReviewerCollectionResponse, error_mapping)
    
    async def post(self,body: AccessReviewReviewer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccessReviewReviewer]:
        """
        Create new navigation property to contactedReviewers for identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewReviewer]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.access_review_reviewer import AccessReviewReviewer

        return await self.request_adapter.send_async(request_info, AccessReviewReviewer, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ContactedReviewersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the reviewers for an access review instance, irrespective of whether or not they have received a notification. The reviewers are represented by an accessReviewReviewer object. A list of zero or more objects are returned, including all of their nested properties.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AccessReviewReviewer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to contactedReviewers for identityGovernance
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
    
    def with_url(self,raw_url: str) -> ContactedReviewersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ContactedReviewersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ContactedReviewersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ContactedReviewersRequestBuilderGetQueryParameters():
        """
        Get the reviewers for an access review instance, irrespective of whether or not they have received a notification. The reviewers are represented by an accessReviewReviewer object. A list of zero or more objects are returned, including all of their nested properties.
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
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class ContactedReviewersRequestBuilderGetRequestConfiguration(RequestConfiguration[ContactedReviewersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ContactedReviewersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

