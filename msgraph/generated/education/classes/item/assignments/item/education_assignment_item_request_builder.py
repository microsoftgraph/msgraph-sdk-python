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

categories_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.categories.categories_request_builder')
education_category_item_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.categories.item.education_category_item_request_builder')
publish_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.publish.publish_request_builder')
resources_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.resources.resources_request_builder')
education_assignment_resource_item_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.resources.item.education_assignment_resource_item_request_builder')
rubric_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.rubric.rubric_request_builder')
set_up_feedback_resources_folder_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.set_up_feedback_resources_folder.set_up_feedback_resources_folder_request_builder')
set_up_resources_folder_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.set_up_resources_folder.set_up_resources_folder_request_builder')
submissions_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.submissions.submissions_request_builder')
education_submission_item_request_builder = lazy_import('msgraph.generated.education.classes.item.assignments.item.submissions.item.education_submission_item_request_builder')
education_assignment = lazy_import('msgraph.generated.models.education_assignment')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EducationAssignmentItemRequestBuilder():
    """
    Provides operations to manage the assignments property of the microsoft.graph.educationClass entity.
    """
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.educationAssignment entity.
        """
        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> resources_request_builder.ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationAssignment entity.
        """
        return resources_request_builder.ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rubric(self) -> rubric_request_builder.RubricRequestBuilder:
        """
        Provides operations to manage the rubric property of the microsoft.graph.educationAssignment entity.
        """
        return rubric_request_builder.RubricRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_up_feedback_resources_folder(self) -> set_up_feedback_resources_folder_request_builder.SetUpFeedbackResourcesFolderRequestBuilder:
        """
        Provides operations to call the setUpFeedbackResourcesFolder method.
        """
        return set_up_feedback_resources_folder_request_builder.SetUpFeedbackResourcesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_up_resources_folder(self) -> set_up_resources_folder_request_builder.SetUpResourcesFolderRequestBuilder:
        """
        Provides operations to call the setUpResourcesFolder method.
        """
        return set_up_resources_folder_request_builder.SetUpResourcesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submissions(self) -> submissions_request_builder.SubmissionsRequestBuilder:
        """
        Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
        """
        return submissions_request_builder.SubmissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def categories_by_id(self,id: str) -> education_category_item_request_builder.EducationCategoryItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.education.classes.item.assignments.item.categories.item collection
        Args:
            id: Unique identifier of the item
        Returns: education_category_item_request_builder.EducationCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationCategory%2Did"] = id
        return education_category_item_request_builder.EducationCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationAssignmentItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EducationAssignmentItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property assignments for education
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
    
    def create_get_request_information(self,request_configuration: Optional[EducationAssignmentItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        All assignments associated with this class. Nullable.
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
    
    def create_patch_request_information(self,body: Optional[education_assignment.EducationAssignment] = None, request_configuration: Optional[EducationAssignmentItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property assignments in education
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
    
    async def delete(self,request_configuration: Optional[EducationAssignmentItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property assignments for education
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
    
    async def get(self,request_configuration: Optional[EducationAssignmentItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_assignment.EducationAssignment]:
        """
        All assignments associated with this class. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_assignment.EducationAssignment]
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
        return await self.request_adapter.send_async(request_info, education_assignment.EducationAssignment, response_handler, error_mapping)
    
    async def patch(self,body: Optional[education_assignment.EducationAssignment] = None, request_configuration: Optional[EducationAssignmentItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_assignment.EducationAssignment]:
        """
        Update the navigation property assignments in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_assignment.EducationAssignment]
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
        return await self.request_adapter.send_async(request_info, education_assignment.EducationAssignment, response_handler, error_mapping)
    
    def resources_by_id(self,id: str) -> education_assignment_resource_item_request_builder.EducationAssignmentResourceItemRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationAssignment entity.
        Args:
            id: Unique identifier of the item
        Returns: education_assignment_resource_item_request_builder.EducationAssignmentResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationAssignmentResource%2Did"] = id
        return education_assignment_resource_item_request_builder.EducationAssignmentResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def submissions_by_id(self,id: str) -> education_submission_item_request_builder.EducationSubmissionItemRequestBuilder:
        """
        Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
        Args:
            id: Unique identifier of the item
        Returns: education_submission_item_request_builder.EducationSubmissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSubmission%2Did"] = id
        return education_submission_item_request_builder.EducationSubmissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EducationAssignmentItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EducationAssignmentItemRequestBuilderGetQueryParameters():
        """
        All assignments associated with this class. Nullable.
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
    class EducationAssignmentItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EducationAssignmentItemRequestBuilder.EducationAssignmentItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EducationAssignmentItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

