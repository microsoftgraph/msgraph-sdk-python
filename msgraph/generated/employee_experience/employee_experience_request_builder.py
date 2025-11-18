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
    from ..models.employee_experience import EmployeeExperience
    from ..models.o_data_errors.o_data_error import ODataError
    from .communities.communities_request_builder import CommunitiesRequestBuilder
    from .engagement_async_operations.engagement_async_operations_request_builder import EngagementAsyncOperationsRequestBuilder
    from .learning_course_activities.learning_course_activities_request_builder import LearningCourseActivitiesRequestBuilder
    from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder
    from .learning_providers.learning_providers_request_builder import LearningProvidersRequestBuilder
    from .roles.roles_request_builder import RolesRequestBuilder

class EmployeeExperienceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the employeeExperience singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EmployeeExperienceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/employeeExperience{?%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EmployeeExperienceRequestBuilderGetQueryParameters]] = None) -> Optional[EmployeeExperience]:
        """
        Get employeeExperience
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeExperience]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.employee_experience import EmployeeExperience

        return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)
    
    def learning_course_activities_with_externalcourse_activity_id(self,externalcourse_activity_id: str) -> LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder:
        """
        Provides operations to manage the learningCourseActivities property of the microsoft.graph.employeeExperience entity.
        param externalcourse_activity_id: Alternate key of learningCourseActivity
        Returns: LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder
        """
        if externalcourse_activity_id is None:
            raise TypeError("externalcourse_activity_id cannot be null.")
        from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder

        return LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder(self.request_adapter, self.path_parameters, externalcourse_activity_id)
    
    async def patch(self,body: EmployeeExperience, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeExperience]:
        """
        Update employeeExperience
        param body: Represents a container that exposes navigation properties for employee experience resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeExperience]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.employee_experience import EmployeeExperience

        return await self.request_adapter.send_async(request_info, EmployeeExperience, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EmployeeExperienceRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get employeeExperience
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EmployeeExperience, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update employeeExperience
        param body: Represents a container that exposes navigation properties for employee experience resources.
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
    
    def with_url(self,raw_url: str) -> EmployeeExperienceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EmployeeExperienceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EmployeeExperienceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def communities(self) -> CommunitiesRequestBuilder:
        """
        Provides operations to manage the communities property of the microsoft.graph.employeeExperience entity.
        """
        from .communities.communities_request_builder import CommunitiesRequestBuilder

        return CommunitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def engagement_async_operations(self) -> EngagementAsyncOperationsRequestBuilder:
        """
        Provides operations to manage the engagementAsyncOperations property of the microsoft.graph.employeeExperience entity.
        """
        from .engagement_async_operations.engagement_async_operations_request_builder import EngagementAsyncOperationsRequestBuilder

        return EngagementAsyncOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @property
    def roles(self) -> RolesRequestBuilder:
        """
        Provides operations to manage the roles property of the microsoft.graph.employeeExperience entity.
        """
        from .roles.roles_request_builder import RolesRequestBuilder

        return RolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EmployeeExperienceRequestBuilderGetQueryParameters():
        """
        Get employeeExperience
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class EmployeeExperienceRequestBuilderGetRequestConfiguration(RequestConfiguration[EmployeeExperienceRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EmployeeExperienceRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

