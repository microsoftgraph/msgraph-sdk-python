from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.education_class import EducationClass
    from ....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .assignment_categories.assignment_categories_request_builder import AssignmentCategoriesRequestBuilder
    from .assignment_defaults.assignment_defaults_request_builder import AssignmentDefaultsRequestBuilder
    from .assignment_settings.assignment_settings_request_builder import AssignmentSettingsRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .modules.modules_request_builder import ModulesRequestBuilder
    from .schools.schools_request_builder import SchoolsRequestBuilder
    from .teachers.teachers_request_builder import TeachersRequestBuilder

class EducationClassItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the classes property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EducationClassItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property classes for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationClass]:
        """
        Get classes from education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationClass]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    async def patch(self,body: Optional[EducationClass] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationClass]:
        """
        Update the navigation property classes in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationClass]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property classes for education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get classes from education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[EducationClass] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property classes in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EducationClassItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationClassItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EducationClassItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignment_categories(self) -> AssignmentCategoriesRequestBuilder:
        """
        Provides operations to manage the assignmentCategories property of the microsoft.graph.educationClass entity.
        """
        from .assignment_categories.assignment_categories_request_builder import AssignmentCategoriesRequestBuilder

        return AssignmentCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_defaults(self) -> AssignmentDefaultsRequestBuilder:
        """
        Provides operations to manage the assignmentDefaults property of the microsoft.graph.educationClass entity.
        """
        from .assignment_defaults.assignment_defaults_request_builder import AssignmentDefaultsRequestBuilder

        return AssignmentDefaultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_settings(self) -> AssignmentSettingsRequestBuilder:
        """
        Provides operations to manage the assignmentSettings property of the microsoft.graph.educationClass entity.
        """
        from .assignment_settings.assignment_settings_request_builder import AssignmentSettingsRequestBuilder

        return AssignmentSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.educationClass entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.educationClass entity.
        """
        from .group.group_request_builder import GroupRequestBuilder

        return GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.educationClass entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def modules(self) -> ModulesRequestBuilder:
        """
        Provides operations to manage the modules property of the microsoft.graph.educationClass entity.
        """
        from .modules.modules_request_builder import ModulesRequestBuilder

        return ModulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schools(self) -> SchoolsRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationClass entity.
        """
        from .schools.schools_request_builder import SchoolsRequestBuilder

        return SchoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teachers(self) -> TeachersRequestBuilder:
        """
        Provides operations to manage the teachers property of the microsoft.graph.educationClass entity.
        """
        from .teachers.teachers_request_builder import TeachersRequestBuilder

        return TeachersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EducationClassItemRequestBuilderGetQueryParameters():
        """
        Get classes from education
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

    

