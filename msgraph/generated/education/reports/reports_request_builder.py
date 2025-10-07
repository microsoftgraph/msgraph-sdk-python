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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.reports_root import ReportsRoot
    from .reading_assignment_submissions.reading_assignment_submissions_request_builder import ReadingAssignmentSubmissionsRequestBuilder
    from .reading_coach_passages.reading_coach_passages_request_builder import ReadingCoachPassagesRequestBuilder
    from .reflect_check_in_responses.reflect_check_in_responses_request_builder import ReflectCheckInResponsesRequestBuilder
    from .speaker_assignment_submissions.speaker_assignment_submissions_request_builder import SpeakerAssignmentSubmissionsRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reports property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/reports{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property reports for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> Optional[ReportsRoot]:
        """
        Get reports from education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.reports_root import ReportsRoot

        return await self.request_adapter.send_async(request_info, ReportsRoot, error_mapping)
    
    async def patch(self,body: ReportsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ReportsRoot]:
        """
        Update the navigation property reports in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ReportsRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.reports_root import ReportsRoot

        return await self.request_adapter.send_async(request_info, ReportsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property reports for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get reports from education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ReportsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property reports in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def reading_assignment_submissions(self) -> ReadingAssignmentSubmissionsRequestBuilder:
        """
        Provides operations to manage the readingAssignmentSubmissions property of the microsoft.graph.reportsRoot entity.
        """
        from .reading_assignment_submissions.reading_assignment_submissions_request_builder import ReadingAssignmentSubmissionsRequestBuilder

        return ReadingAssignmentSubmissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reading_coach_passages(self) -> ReadingCoachPassagesRequestBuilder:
        """
        Provides operations to manage the readingCoachPassages property of the microsoft.graph.reportsRoot entity.
        """
        from .reading_coach_passages.reading_coach_passages_request_builder import ReadingCoachPassagesRequestBuilder

        return ReadingCoachPassagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reflect_check_in_responses(self) -> ReflectCheckInResponsesRequestBuilder:
        """
        Provides operations to manage the reflectCheckInResponses property of the microsoft.graph.reportsRoot entity.
        """
        from .reflect_check_in_responses.reflect_check_in_responses_request_builder import ReflectCheckInResponsesRequestBuilder

        return ReflectCheckInResponsesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def speaker_assignment_submissions(self) -> SpeakerAssignmentSubmissionsRequestBuilder:
        """
        Provides operations to manage the speakerAssignmentSubmissions property of the microsoft.graph.reportsRoot entity.
        """
        from .speaker_assignment_submissions.speaker_assignment_submissions_request_builder import SpeakerAssignmentSubmissionsRequestBuilder

        return SpeakerAssignmentSubmissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Get reports from education
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration(RequestConfiguration[ReportsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

