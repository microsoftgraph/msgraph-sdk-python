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

outcomes_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.outcomes.outcomes_request_builder')
education_outcome_item_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.outcomes.item.education_outcome_item_request_builder')
reassign_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.reassign.reassign_request_builder')
resources_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.resources.resources_request_builder')
education_submission_resource_item_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.resources.item.education_submission_resource_item_request_builder')
return_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.return_escaped.return_request_builder')
set_up_resources_folder_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.set_up_resources_folder.set_up_resources_folder_request_builder')
submit_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.submit.submit_request_builder')
submitted_resources_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.submitted_resources.submitted_resources_request_builder')
education_submission_resource_item_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.submitted_resources.item.education_submission_resource_item_request_builder')
unsubmit_request_builder = lazy_import('msgraph.generated.education.me.assignments.item.submissions.item.unsubmit.unsubmit_request_builder')
education_submission = lazy_import('msgraph.generated.models.education_submission')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EducationSubmissionItemRequestBuilder():
    """
    Provides operations to manage the submissions property of the microsoft.graph.educationAssignment entity.
    """
    @property
    def outcomes(self) -> outcomes_request_builder.OutcomesRequestBuilder:
        """
        Provides operations to manage the outcomes property of the microsoft.graph.educationSubmission entity.
        """
        return outcomes_request_builder.OutcomesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reassign(self) -> reassign_request_builder.ReassignRequestBuilder:
        """
        Provides operations to call the reassign method.
        """
        return reassign_request_builder.ReassignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> resources_request_builder.ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationSubmission entity.
        """
        return resources_request_builder.ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def return_escaped(self) -> return_request_builder.ReturnRequestBuilder:
        """
        Provides operations to call the return method.
        """
        return return_request_builder.ReturnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_up_resources_folder(self) -> set_up_resources_folder_request_builder.SetUpResourcesFolderRequestBuilder:
        """
        Provides operations to call the setUpResourcesFolder method.
        """
        return set_up_resources_folder_request_builder.SetUpResourcesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submit(self) -> submit_request_builder.SubmitRequestBuilder:
        """
        Provides operations to call the submit method.
        """
        return submit_request_builder.SubmitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submitted_resources(self) -> submitted_resources_request_builder.SubmittedResourcesRequestBuilder:
        """
        Provides operations to manage the submittedResources property of the microsoft.graph.educationSubmission entity.
        """
        return submitted_resources_request_builder.SubmittedResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unsubmit(self) -> unsubmit_request_builder.UnsubmitRequestBuilder:
        """
        Provides operations to call the unsubmit method.
        """
        return unsubmit_request_builder.UnsubmitRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationSubmissionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/me/assignments/{educationAssignment%2Did}/submissions/{educationSubmission%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EducationSubmissionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property submissions for education
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
    
    def create_get_request_information(self,request_configuration: Optional[EducationSubmissionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
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
    
    def create_patch_request_information(self,body: Optional[education_submission.EducationSubmission] = None, request_configuration: Optional[EducationSubmissionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property submissions in education
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
    
    async def delete(self,request_configuration: Optional[EducationSubmissionItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property submissions for education
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
    
    async def get(self,request_configuration: Optional[EducationSubmissionItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_submission.EducationSubmission]:
        """
        Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_submission.EducationSubmission]
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
        return await self.request_adapter.send_async(request_info, education_submission.EducationSubmission, response_handler, error_mapping)
    
    def outcomes_by_id(self,id: str) -> education_outcome_item_request_builder.EducationOutcomeItemRequestBuilder:
        """
        Provides operations to manage the outcomes property of the microsoft.graph.educationSubmission entity.
        Args:
            id: Unique identifier of the item
        Returns: education_outcome_item_request_builder.EducationOutcomeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationOutcome%2Did"] = id
        return education_outcome_item_request_builder.EducationOutcomeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[education_submission.EducationSubmission] = None, request_configuration: Optional[EducationSubmissionItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[education_submission.EducationSubmission]:
        """
        Update the navigation property submissions in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[education_submission.EducationSubmission]
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
        return await self.request_adapter.send_async(request_info, education_submission.EducationSubmission, response_handler, error_mapping)
    
    def resources_by_id(self,id: str) -> education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.educationSubmission entity.
        Args:
            id: Unique identifier of the item
        Returns: education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSubmissionResource%2Did"] = id
        return education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def submitted_resources_by_id(self,id: str) -> education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder:
        """
        Provides operations to manage the submittedResources property of the microsoft.graph.educationSubmission entity.
        Args:
            id: Unique identifier of the item
        Returns: education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSubmissionResource%2Did"] = id
        return education_submission_resource_item_request_builder.EducationSubmissionResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EducationSubmissionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EducationSubmissionItemRequestBuilderGetQueryParameters():
        """
        Once published, there is a submission object for each student representing their work and grade.  Read-only. Nullable.
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
    class EducationSubmissionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EducationSubmissionItemRequestBuilder.EducationSubmissionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EducationSubmissionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

