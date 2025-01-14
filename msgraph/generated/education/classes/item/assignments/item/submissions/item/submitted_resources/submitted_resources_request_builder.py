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
    from .........models.education_submission_resource import EducationSubmissionResource
    from .........models.education_submission_resource_collection_response import EducationSubmissionResourceCollectionResponse
    from .........models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.education_submission_resource_item_request_builder import EducationSubmissionResourceItemRequestBuilder

class SubmittedResourcesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the submittedResources property of the microsoft.graph.educationSubmission entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SubmittedResourcesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/submittedResources{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_education_submission_resource_id(self,education_submission_resource_id: str) -> EducationSubmissionResourceItemRequestBuilder:
        """
        Provides operations to manage the submittedResources property of the microsoft.graph.educationSubmission entity.
        param education_submission_resource_id: The unique identifier of educationSubmissionResource
        Returns: EducationSubmissionResourceItemRequestBuilder
        """
        if education_submission_resource_id is None:
            raise TypeError("education_submission_resource_id cannot be null.")
        from .item.education_submission_resource_item_request_builder import EducationSubmissionResourceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSubmissionResource%2Did"] = education_submission_resource_id
        return EducationSubmissionResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SubmittedResourcesRequestBuilderGetQueryParameters]] = None) -> Optional[EducationSubmissionResourceCollectionResponse]:
        """
        List the educationSubmissionResource objects that were officially submitted for grading. Only teachers, students, and applications with application permissions can perform this operation. The student who owns the submission can't change the submitted list without resubmitting the assignment. This resource is a wrapper around the real resource and can contain a pointer back to the actual assignment resource if this resource was copied from the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmissionResourceCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/educationsubmission-list-submittedresources?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.education_submission_resource_collection_response import EducationSubmissionResourceCollectionResponse

        return await self.request_adapter.send_async(request_info, EducationSubmissionResourceCollectionResponse, error_mapping)
    
    async def post(self,body: EducationSubmissionResource, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EducationSubmissionResource]:
        """
        Create new navigation property to submittedResources for education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmissionResource]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.education_submission_resource import EducationSubmissionResource

        return await self.request_adapter.send_async(request_info, EducationSubmissionResource, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SubmittedResourcesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List the educationSubmissionResource objects that were officially submitted for grading. Only teachers, students, and applications with application permissions can perform this operation. The student who owns the submission can't change the submitted list without resubmitting the assignment. This resource is a wrapper around the real resource and can contain a pointer back to the actual assignment resource if this resource was copied from the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: EducationSubmissionResource, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to submittedResources for education
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
    
    def with_url(self,raw_url: str) -> SubmittedResourcesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SubmittedResourcesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SubmittedResourcesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SubmittedResourcesRequestBuilderGetQueryParameters():
        """
        List the educationSubmissionResource objects that were officially submitted for grading. Only teachers, students, and applications with application permissions can perform this operation. The student who owns the submission can't change the submitted list without resubmitting the assignment. This resource is a wrapper around the real resource and can contain a pointer back to the actual assignment resource if this resource was copied from the assignment.
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
    class SubmittedResourcesRequestBuilderGetRequestConfiguration(RequestConfiguration[SubmittedResourcesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SubmittedResourcesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

