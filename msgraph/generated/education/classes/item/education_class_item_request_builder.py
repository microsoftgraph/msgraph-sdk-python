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
    from ....models.education_class import EducationClass
    from ....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .assignment_categories.assignment_categories_request_builder import AssignmentCategoriesRequestBuilder
    from .assignment_defaults.assignment_defaults_request_builder import AssignmentDefaultsRequestBuilder
    from .assignment_settings.assignment_settings_request_builder import AssignmentSettingsRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .schools.schools_request_builder import SchoolsRequestBuilder
    from .teachers.teachers_request_builder import TeachersRequestBuilder

class EducationClassItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the classes property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationClassItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EducationClassItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an educationClass. Because a class is also a universal group, deleting a class deletes the group.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationclass-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EducationClassItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EducationClass]:
        """
        Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationClass]
        Find more info here: https://learn.microsoft.com/graph/api/educationclass-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    async def patch(self,body: Optional[EducationClass] = None, request_configuration: Optional[EducationClassItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EducationClass]:
        """
        Update the properties of an educationClass object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationClass]
        Find more info here: https://learn.microsoft.com/graph/api/educationclass-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EducationClassItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an educationClass. Because a class is also a universal group, deleting a class deletes the group.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[EducationClassItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
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
    
    def to_patch_request_information(self,body: Optional[EducationClass] = None, request_configuration: Optional[EducationClassItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an educationClass object.
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationClassItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EducationClassItemRequestBuilderGetQueryParameters():
        """
        Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
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
    class EducationClassItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EducationClassItemRequestBuilder.EducationClassItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationClassItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

