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
    from ..........models.education_submission_resource import EducationSubmissionResource
    from ..........models.o_data_errors.o_data_error import ODataError

class EducationSubmissionResourceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the resources property of the microsoft.graph.educationSubmission entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EducationSubmissionResourceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}/resources/{educationSubmissionResource%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete an educationSubmissionResource from the submission. Only teachers and students can perform this operation. If the resource was copied from the assignment, a new copy of the resource will be created after the current copy is deleted. This allows you to 'reset' the resource to its original state. If the resource wasn't copied from the assignment but was added from the student, the resource is deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationsubmissionresource-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EducationSubmissionResourceItemRequestBuilderGetQueryParameters]] = None) -> Optional[EducationSubmissionResource]:
        """
        Retrieve the properties of a specific resource associated with a submission. Only teachers, students, and applications with application permissions can perform this operation. This resource is in the 'working' resource list and should be considered work in process by a student. This resource is wrapped with a possible pointer back to the assignment resource if it was copied from the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmissionResource]
        Find more info here: https://learn.microsoft.com/graph/api/educationsubmissionresource-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.education_submission_resource import EducationSubmissionResource

        return await self.request_adapter.send_async(request_info, EducationSubmissionResource, error_mapping)
    
    async def patch(self,body: EducationSubmissionResource, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EducationSubmissionResource]:
        """
        Update the navigation property resources in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSubmissionResource]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.education_submission_resource import EducationSubmissionResource

        return await self.request_adapter.send_async(request_info, EducationSubmissionResource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an educationSubmissionResource from the submission. Only teachers and students can perform this operation. If the resource was copied from the assignment, a new copy of the resource will be created after the current copy is deleted. This allows you to 'reset' the resource to its original state. If the resource wasn't copied from the assignment but was added from the student, the resource is deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EducationSubmissionResourceItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties of a specific resource associated with a submission. Only teachers, students, and applications with application permissions can perform this operation. This resource is in the 'working' resource list and should be considered work in process by a student. This resource is wrapped with a possible pointer back to the assignment resource if it was copied from the assignment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EducationSubmissionResource, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property resources in education
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
    
    def with_url(self,raw_url: str) -> EducationSubmissionResourceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationSubmissionResourceItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EducationSubmissionResourceItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class EducationSubmissionResourceItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EducationSubmissionResourceItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties of a specific resource associated with a submission. Only teachers, students, and applications with application permissions can perform this operation. This resource is in the 'working' resource list and should be considered work in process by a student. This resource is wrapped with a possible pointer back to the assignment resource if it was copied from the assignment.
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
    class EducationSubmissionResourceItemRequestBuilderGetRequestConfiguration(RequestConfiguration[EducationSubmissionResourceItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EducationSubmissionResourceItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

