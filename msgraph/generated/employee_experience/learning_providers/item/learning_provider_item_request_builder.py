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
    from ....models.learning_provider import LearningProvider
    from ....models.o_data_errors.o_data_error import ODataError
    from .learning_contents.learning_contents_request_builder import LearningContentsRequestBuilder
    from .learning_contents_with_external_id.learning_contents_with_external_id_request_builder import LearningContentsWithExternalIdRequestBuilder
    from .learning_course_activities.learning_course_activities_request_builder import LearningCourseActivitiesRequestBuilder
    from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder

class LearningProviderItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the learningProviders property of the microsoft.graph.employeeExperience entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new LearningProviderItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/employeeExperience/learningProviders/{learningProvider%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a learningProvider resource and remove its registration in Viva Learning for a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/employeeexperience-delete-learningproviders?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LearningProviderItemRequestBuilderGetQueryParameters]] = None) -> Optional[LearningProvider]:
        """
        Read the properties and relationships of a learningProvider object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LearningProvider]
        Find more info here: https://learn.microsoft.com/graph/api/learningprovider-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.learning_provider import LearningProvider

        return await self.request_adapter.send_async(request_info, LearningProvider, error_mapping)
    
    def learning_contents_with_external_id(self,external_id: str) -> LearningContentsWithExternalIdRequestBuilder:
        """
        Provides operations to manage the learningContents property of the microsoft.graph.learningProvider entity.
        param external_id: Alternate key of learningContent
        Returns: LearningContentsWithExternalIdRequestBuilder
        """
        if external_id is None:
            raise TypeError("external_id cannot be null.")
        from .learning_contents_with_external_id.learning_contents_with_external_id_request_builder import LearningContentsWithExternalIdRequestBuilder

        return LearningContentsWithExternalIdRequestBuilder(self.request_adapter, self.path_parameters, external_id)
    
    def learning_course_activities_with_externalcourse_activity_id(self,externalcourse_activity_id: str) -> LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder:
        """
        Provides operations to manage the learningCourseActivities property of the microsoft.graph.learningProvider entity.
        param externalcourse_activity_id: Alternate key of learningCourseActivity
        Returns: LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder
        """
        if externalcourse_activity_id is None:
            raise TypeError("externalcourse_activity_id cannot be null.")
        from .learning_course_activities_with_externalcourse_activity_id.learning_course_activities_with_externalcourse_activity_id_request_builder import LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder

        return LearningCourseActivitiesWithExternalcourseActivityIdRequestBuilder(self.request_adapter, self.path_parameters, externalcourse_activity_id)
    
    async def patch(self,body: LearningProvider, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LearningProvider]:
        """
        Update the properties of a learningProvider object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LearningProvider]
        Find more info here: https://learn.microsoft.com/graph/api/learningprovider-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.learning_provider import LearningProvider

        return await self.request_adapter.send_async(request_info, LearningProvider, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a learningProvider resource and remove its registration in Viva Learning for a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LearningProviderItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a learningProvider object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: LearningProvider, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a learningProvider object.
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
    
    def with_url(self,raw_url: str) -> LearningProviderItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LearningProviderItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LearningProviderItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def learning_contents(self) -> LearningContentsRequestBuilder:
        """
        Provides operations to manage the learningContents property of the microsoft.graph.learningProvider entity.
        """
        from .learning_contents.learning_contents_request_builder import LearningContentsRequestBuilder

        return LearningContentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def learning_course_activities(self) -> LearningCourseActivitiesRequestBuilder:
        """
        Provides operations to manage the learningCourseActivities property of the microsoft.graph.learningProvider entity.
        """
        from .learning_course_activities.learning_course_activities_request_builder import LearningCourseActivitiesRequestBuilder

        return LearningCourseActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class LearningProviderItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LearningProviderItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a learningProvider object.
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
    class LearningProviderItemRequestBuilderGetRequestConfiguration(RequestConfiguration[LearningProviderItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LearningProviderItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

