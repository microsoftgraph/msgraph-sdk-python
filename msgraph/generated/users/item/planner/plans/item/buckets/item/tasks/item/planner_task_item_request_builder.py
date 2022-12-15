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

planner_task = lazy_import('msgraph.generated.models.planner_task')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
assigned_to_task_board_format_request_builder = lazy_import('msgraph.generated.users.item.planner.plans.item.buckets.item.tasks.item.assigned_to_task_board_format.assigned_to_task_board_format_request_builder')
bucket_task_board_format_request_builder = lazy_import('msgraph.generated.users.item.planner.plans.item.buckets.item.tasks.item.bucket_task_board_format.bucket_task_board_format_request_builder')
details_request_builder = lazy_import('msgraph.generated.users.item.planner.plans.item.buckets.item.tasks.item.details.details_request_builder')
progress_task_board_format_request_builder = lazy_import('msgraph.generated.users.item.planner.plans.item.buckets.item.tasks.item.progress_task_board_format.progress_task_board_format_request_builder')

class PlannerTaskItemRequestBuilder():
    """
    Provides operations to manage the tasks property of the microsoft.graph.plannerBucket entity.
    """
    @property
    def assigned_to_task_board_format(self) -> assigned_to_task_board_format_request_builder.AssignedToTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the assignedToTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        return assigned_to_task_board_format_request_builder.AssignedToTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bucket_task_board_format(self) -> bucket_task_board_format_request_builder.BucketTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the bucketTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        return bucket_task_board_format_request_builder.BucketTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> details_request_builder.DetailsRequestBuilder:
        """
        Provides operations to manage the details property of the microsoft.graph.plannerTask entity.
        """
        return details_request_builder.DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress_task_board_format(self) -> progress_task_board_format_request_builder.ProgressTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the progressTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        return progress_task_board_format_request_builder.ProgressTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlannerTaskItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/planner/plans/{plannerPlan%2Did}/buckets/{plannerBucket%2Did}/tasks/{plannerTask%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property tasks for users
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
    
    def create_get_request_information(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
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
    
    def create_patch_request_information(self,body: Optional[planner_task.PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property tasks in users
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
    
    async def delete(self,request_configuration: Optional[PlannerTaskItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property tasks for users
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
    
    async def get(self,request_configuration: Optional[PlannerTaskItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[planner_task.PlannerTask]:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[planner_task.PlannerTask]
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
        return await self.request_adapter.send_async(request_info, planner_task.PlannerTask, response_handler, error_mapping)
    
    async def patch(self,body: Optional[planner_task.PlannerTask] = None, request_configuration: Optional[PlannerTaskItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[planner_task.PlannerTask]:
        """
        Update the navigation property tasks in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[planner_task.PlannerTask]
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
        return await self.request_adapter.send_async(request_info, planner_task.PlannerTask, response_handler, error_mapping)
    
    @dataclass
    class PlannerTaskItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PlannerTaskItemRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. The collection of tasks in the bucket.
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
    class PlannerTaskItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PlannerTaskItemRequestBuilder.PlannerTaskItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PlannerTaskItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

