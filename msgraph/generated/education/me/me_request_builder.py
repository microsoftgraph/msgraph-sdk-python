from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignments_request_builder = lazy_import('msgraph.generated.education.me.assignments.assignments_request_builder')
education_assignment_item_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.education_assignment_item_request_builder')
classes_request_builder = lazy_import('msgraph.generated.education.me.classes.classes_request_builder')
education_class_item_request_builder = lazy_import('msgraph.generated.education.me.classes.item.education_class_item_request_builder')
rubrics_request_builder = lazy_import('msgraph.generated.education.me.rubrics.rubrics_request_builder')
education_rubric_item_request_builder = lazy_import('msgraph.generated.education.me.rubrics.item.education_rubric_item_request_builder')
schools_request_builder = lazy_import('msgraph.generated.education.me.schools.schools_request_builder')
education_school_item_request_builder = lazy_import('msgraph.generated.education.me.schools.item.education_school_item_request_builder')
taught_classes_request_builder = lazy_import('msgraph.generated.education.me.taught_classes.taught_classes_request_builder')
education_class_item_request_builder = lazy_import('msgraph.generated.education.me.taught_classes.item.education_class_item_request_builder')
user_request_builder = lazy_import('msgraph.generated.education.me.user.user_request_builder')
education_user = lazy_import('msgraph.generated.models.education_user')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class MeRequestBuilder():
    """
    Provides operations to manage the me property of the microsoft.graph.educationRoot entity.
    """
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.educationUser entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classes(self) -> classes_request_builder.ClassesRequestBuilder:
        """
        Provides operations to manage the classes property of the microsoft.graph.educationUser entity.
        """
        return classes_request_builder.ClassesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rubrics(self) -> rubrics_request_builder.RubricsRequestBuilder:
        """
        Provides operations to manage the rubrics property of the microsoft.graph.educationUser entity.
        """
        return rubrics_request_builder.RubricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schools(self) -> schools_request_builder.SchoolsRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationUser entity.
        """
        return schools_request_builder.SchoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def taught_classes(self) -> taught_classes_request_builder.TaughtClassesRequestBuilder:
        """
        Provides operations to manage the taughtClasses property of the microsoft.graph.educationUser entity.
        """
        return taught_classes_request_builder.TaughtClassesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user(self) -> user_request_builder.UserRequestBuilder:
        """
        Provides operations to manage the user property of the microsoft.graph.educationUser entity.
        """
        return user_request_builder.UserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.educationUser entity.
        Args:
            id: Unique identifier of the item
        Returns: education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationAssignment%2Did"] = id
        return education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def classes_by_id(self,id: str) -> education_class_item_request_builder.EducationClassItemRequestBuilder:
        """
        Provides operations to manage the classes property of the microsoft.graph.educationUser entity.
        Args:
            id: Unique identifier of the item
        Returns: education_class_item_request_builder.EducationClassItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationClass%2Did"] = id
        return education_class_item_request_builder.EducationClassItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MeRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/me{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[MeRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property me for education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[MeRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get me from education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[education_user.EducationUser] = None, request_configuration: Optional[MeRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property me in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[MeRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property me for education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[MeRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_user.EducationUser]:
        """
        Get me from education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_user.EducationUser]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, education_user.EducationUser, response_handler, error_mapping)
    
    async def patch(self,body: Optional[education_user.EducationUser] = None, request_configuration: Optional[MeRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_user.EducationUser]:
        """
        Update the navigation property me in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_user.EducationUser]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, education_user.EducationUser, response_handler, error_mapping)
    
    def rubrics_by_id(self,id: str) -> education_rubric_item_request_builder.EducationRubricItemRequestBuilder:
        """
        Provides operations to manage the rubrics property of the microsoft.graph.educationUser entity.
        Args:
            id: Unique identifier of the item
        Returns: education_rubric_item_request_builder.EducationRubricItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationRubric%2Did"] = id
        return education_rubric_item_request_builder.EducationRubricItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def schools_by_id(self,id: str) -> education_school_item_request_builder.EducationSchoolItemRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationUser entity.
        Args:
            id: Unique identifier of the item
        Returns: education_school_item_request_builder.EducationSchoolItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSchool%2Did"] = id
        return education_school_item_request_builder.EducationSchoolItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def taught_classes_by_id(self,id: str) -> education_class_item_request_builder.EducationClassItemRequestBuilder:
        """
        Provides operations to manage the taughtClasses property of the microsoft.graph.educationUser entity.
        Args:
            id: Unique identifier of the item
        Returns: education_class_item_request_builder.EducationClassItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationClass%2Did"] = id
        return education_class_item_request_builder.EducationClassItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class MeRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MeRequestBuilderGetQueryParameters():
        """
        Get me from education
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class MeRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MeRequestBuilder.MeRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MeRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

