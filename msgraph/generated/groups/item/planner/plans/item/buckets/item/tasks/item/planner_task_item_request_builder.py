from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..........models.o_data_errors.o_data_error import ODataError
    from ..........models.planner_task import PlannerTask
    from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder
    from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder
    from .details.details_request_builder import DetailsRequestBuilder
    from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

class PlannerTaskItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tasks property of the microsoft.graph.plannerBucket entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PlannerTaskItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/planner/plans/{plannerPlan%2Did}/buckets/{plannerBucket%2Did}/tasks/{plannerTask%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property tasks for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PlannerTaskItemRequestBuilderGetQueryParameters]] = None) -> Optional[PlannerTask]:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    async def patch(self,body: PlannerTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PlannerTask]:
        """
        Update the navigation property tasks in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PlannerTask]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.planner_task import PlannerTask

        return await self.request_adapter.send_async(request_info, PlannerTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property tasks for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlannerTaskItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read-only. Nullable. The collection of tasks in the bucket.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: PlannerTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property tasks in groups
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
    
    def with_url(self,raw_url: str) -> PlannerTaskItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlannerTaskItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlannerTaskItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assigned_to_task_board_format(self) -> AssignedToTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the assignedToTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .assigned_to_task_board_format.assigned_to_task_board_format_request_builder import AssignedToTaskBoardFormatRequestBuilder

        return AssignedToTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bucket_task_board_format(self) -> BucketTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the bucketTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .bucket_task_board_format.bucket_task_board_format_request_builder import BucketTaskBoardFormatRequestBuilder

        return BucketTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> DetailsRequestBuilder:
        """
        Provides operations to manage the details property of the microsoft.graph.plannerTask entity.
        """
        from .details.details_request_builder import DetailsRequestBuilder

        return DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress_task_board_format(self) -> ProgressTaskBoardFormatRequestBuilder:
        """
        Provides operations to manage the progressTaskBoardFormat property of the microsoft.graph.plannerTask entity.
        """
        from .progress_task_board_format.progress_task_board_format_request_builder import ProgressTaskBoardFormatRequestBuilder

        return ProgressTaskBoardFormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlannerTaskItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlannerTaskItemRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. The collection of tasks in the bucket.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class PlannerTaskItemRequestBuilderGetRequestConfiguration(RequestConfiguration[PlannerTaskItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PlannerTaskItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

