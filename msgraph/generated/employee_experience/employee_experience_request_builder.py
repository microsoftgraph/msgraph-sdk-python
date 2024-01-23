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
    from ..models.employee_experience import EmployeeExperience
    from ..models.o_data_errors.o_data_error import ODataError
    from .learning_course_activities.learning_course_activities_request_builder import LearningCourseActivitiesRequestBuilder
    from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder
    from .learning_providers.learning_providers_request_builder import LearningProvidersRequestBuilder

class EmployeeExperienceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the employeeExperience singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EmployeeExperienceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/employeeExperience{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[EmployeeExperienceRequestBuilderGetRequestConfiguration] = None) -> Optional[EmployeeExperience]:
        """
        Get employeeExperience
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeExperience]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.employee_experience import EmployeeExperience

        return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)
    
    def learning_course_activities_with_externalcourse_activity_id(self,externalcourse_activity_id: Optional[str] = None) -> LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder:
        """
        Provides operations to manage the learningCourseActivities property of the microsoft.graph.employeeExperience entity.
        param externalcourse_activity_id: Alternate key of learningCourseActivity
        Returns: LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder
        """
        if not externalcourse_activity_id:
            raise TypeError("externalcourse_activity_id cannot be null.")
        from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder

        return LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder(self.request_adapter, self.path_parameters, externalcourse_activity_id)
    
    async def patch(self,body: Optional[EmployeeExperience] = None, request_configuration: Optional[EmployeeExperienceRequestBuilderPatchRequestConfiguration] = None) -> Optional[EmployeeExperience]:
        """
        Update employeeExperience
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeExperience]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.employee_experience import EmployeeExperience

        return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[EmployeeExperienceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get employeeExperience
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
    
    def to_patch_request_information(self,body: Optional[EmployeeExperience] = None, request_configuration: Optional[EmployeeExperienceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update employeeExperience
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EmployeeExperienceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeeExperienceRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EmployeeExperienceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def learning_course_activities(self) -> LearningCourseActivitiesRequestBuilder:
        """
        Provides operations to manage the learningCourseActivities property of the microsoft.graph.employeeExperience entity.
        """
        from .learning_course_activities.learning_course_activities_request_builder import LearningCourseActivitiesRequestBuilder

        return LearningCourseActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def learning_providers(self) -> LearningProvidersRequestBuilder:
        """
        Provides operations to manage the learningProviders property of the microsoft.graph.employeeExperience entity.
        """
        from .learning_providers.learning_providers_request_builder import LearningProvidersRequestBuilder

        return LearningProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeeExperienceRequestBuilderGetQueryParameters():
        """
        Get employeeExperience
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EmployeeExperienceRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EmployeeExperienceRequestBuilder.EmployeeExperienceRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EmployeeExperienceRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

