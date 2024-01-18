from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.education_submission import EducationSubmission
    from ......models.education_submission_collection_response import EducationSubmissionCollectionResponse
    from ......models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.education_submission_item_request_builder import EducationSubmissionItemRequestBuilder

class SubmissionsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SubmissionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/me/assignments/{educationAssignment%2Did}/submissions{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_education_submission_id(self,education_submission_id: str) -> EducationSubmissionItemRequestBuilder:
        """
        Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
        param education_submission_id: The unique identifier of educationSubmission
        Returns: EducationSubmissionItemRequestBuilder
        """
        if not education_submission_id:
            raise TypeError("education_submission_id cannot be null.")
        from .item.education_submission_item_request_builder import EducationSubmissionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSubmission%2Did"] = education_submission_id
        return EducationSubmissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SubmissionsRequestBuilderGetRequestConfiguration] = None) -> Optional[EducationSubmissionCollectionResponse]:
        """
        List all the submissions associated with an assignment. Only teachers, students, and applications with application permissions can perform this operation. A teacher or an application with application permissions can get all the submissions while a student can only get submissions that they're associated with.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmissionCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/educationassignment-list-submissions?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.education_submission_collection_response import EducationSubmissionCollectionResponse

        return await self.request_adapter.send_async(request_info, EducationSubmissionCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[EducationSubmission] = None, request_configuration: Optional[SubmissionsRequestBuilderPostRequestConfiguration] = None) -> Optional[EducationSubmission]:
        """
        Create new navigation property to submissions for education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmission]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.education_submission import EducationSubmission

        return await self.request_adapter.send_async(request_info, EducationSubmission, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SubmissionsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List all the submissions associated with an assignment. Only teachers, students, and applications with application permissions can perform this operation. A teacher or an application with application permissions can get all the submissions while a student can only get submissions that they're associated with.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[EducationSubmission] = None, request_configuration: Optional[SubmissionsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to submissions for education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SubmissionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SubmissionsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SubmissionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SubmissionsRequestBuilderGetQueryParameters():
        """
        List all the submissions associated with an assignment. Only teachers, students, and applications with application permissions can perform this operation. A teacher or an application with application permissions can get all the submissions while a student can only get submissions that they're associated with.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SubmissionsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SubmissionsRequestBuilder.SubmissionsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SubmissionsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

