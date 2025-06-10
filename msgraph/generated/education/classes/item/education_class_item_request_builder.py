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
    from ....models.education_class import EducationClass
    from ....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .assignment_categories.assignment_categories_request_builder import AssignmentCategoriesRequestBuilder
    from .assignment_defaults.assignment_defaults_request_builder import AssignmentDefaultsRequestBuilder
    from .assignment_settings.assignment_settings_request_builder import AssignmentSettingsRequestBuilder
    from .get_recently_modified_submissions.get_recently_modified_submissions_request_builder import GetRecentlyModifiedSubmissionsRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .modules.modules_request_builder import ModulesRequestBuilder
    from .schools.schools_request_builder import SchoolsRequestBuilder
    from .teachers.teachers_request_builder import TeachersRequestBuilder

class EducationClassItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the classes property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EducationClassItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EducationClassItemRequestBuilderGetQueryParameters]] = None) -> Optional[EducationClass]:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    async def patch(self,body: EducationClass, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EducationClass]:
        """
        Update the properties of an educationClass object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationClass]
        Find more info here: https://learn.microsoft.com/graph/api/educationclass-update?view=graph-rest-1.0
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
        from ....models.education_class import EducationClass

        return await self.request_adapter.send_async(request_info, EducationClass, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an educationClass. Because a class is also a universal group, deleting a class deletes the group.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EducationClassItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EducationClass, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of an educationClass object.
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
    
    def with_url(self,raw_url: str) -> EducationClassItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationClassItemRequestBuilder
        """
        if raw_url is None:
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
    def get_recently_modified_submissions(self) -> GetRecentlyModifiedSubmissionsRequestBuilder:
        """
        Provides operations to call the getRecentlyModifiedSubmissions method.
        """
        from .get_recently_modified_submissions.get_recently_modified_submissions_request_builder import GetRecentlyModifiedSubmissionsRequestBuilder

        return GetRecentlyModifiedSubmissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class EducationClassItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EducationClassItemRequestBuilderGetQueryParameters():
        """
        Retrieve a class from the system. A class is a universal group with a special property that indicates to the system that the group is a class. Group members represent the students; group admins represent the teachers in the class. If you're using the delegated token, the user will only see classes in which they are members.
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
    class EducationClassItemRequestBuilderGetRequestConfiguration(RequestConfiguration[EducationClassItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EducationClassItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

