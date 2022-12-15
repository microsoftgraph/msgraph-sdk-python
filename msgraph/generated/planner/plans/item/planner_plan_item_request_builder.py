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

planner_plan = lazy_import('msgraph.generated.models.planner_plan')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
buckets_request_builder = lazy_import('msgraph.generated.planner.plans.item.buckets.buckets_request_builder')
planner_bucket_item_request_builder = lazy_import('msgraph.generated.planner.plans.item.buckets.item.planner_bucket_item_request_builder')
details_request_builder = lazy_import('msgraph.generated.planner.plans.item.details.details_request_builder')
tasks_request_builder = lazy_import('msgraph.generated.planner.plans.item.tasks.tasks_request_builder')
planner_task_item_request_builder = lazy_import('msgraph.generated.planner.plans.item.tasks.item.planner_task_item_request_builder')

class PlannerPlanItemRequestBuilder():
    """
    Provides operations to manage the plans property of the microsoft.graph.planner entity.
    """
    @property
    def buckets(self) -> buckets_request_builder.BucketsRequestBuilder:
        """
        Provides operations to manage the buckets property of the microsoft.graph.plannerPlan entity.
        """
        return buckets_request_builder.BucketsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def details(self) -> details_request_builder.DetailsRequestBuilder:
        """
        Provides operations to manage the details property of the microsoft.graph.plannerPlan entity.
        """
        return details_request_builder.DetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> tasks_request_builder.TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plannerPlan entity.
        """
        return tasks_request_builder.TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    def buckets_by_id(self,id: str) -> planner_bucket_item_request_builder.PlannerBucketItemRequestBuilder:
        """
        Provides operations to manage the buckets property of the microsoft.graph.plannerPlan entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_bucket_item_request_builder.PlannerBucketItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerBucket%2Did"] = id
        return planner_bucket_item_request_builder.PlannerBucketItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlannerPlanItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/planner/plans/{plannerPlan%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[PlannerPlanItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property plans for planner
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
    
    def create_get_request_information(self,request_configuration: Optional[PlannerPlanItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read-only. Nullable. Returns a collection of the specified plans
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
    
    def create_patch_request_information(self,body: Optional[planner_plan.PlannerPlan] = None, request_configuration: Optional[PlannerPlanItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property plans in planner
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
    
    async def delete(self,request_configuration: Optional[PlannerPlanItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property plans for planner
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
    
    async def get(self,request_configuration: Optional[PlannerPlanItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[planner_plan.PlannerPlan]:
        """
        Read-only. Nullable. Returns a collection of the specified plans
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[planner_plan.PlannerPlan]
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
        return await self.request_adapter.send_async(request_info, planner_plan.PlannerPlan, response_handler, error_mapping)
    
    async def patch(self,body: Optional[planner_plan.PlannerPlan] = None, request_configuration: Optional[PlannerPlanItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[planner_plan.PlannerPlan]:
        """
        Update the navigation property plans in planner
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[planner_plan.PlannerPlan]
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
        return await self.request_adapter.send_async(request_info, planner_plan.PlannerPlan, response_handler, error_mapping)
    
    def tasks_by_id(self,id: str) -> planner_task_item_request_builder.PlannerTaskItemRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.plannerPlan entity.
        Args:
            id: Unique identifier of the item
        Returns: planner_task_item_request_builder.PlannerTaskItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["plannerTask%2Did"] = id
        return planner_task_item_request_builder.PlannerTaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class PlannerPlanItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PlannerPlanItemRequestBuilderGetQueryParameters():
        """
        Read-only. Nullable. Returns a collection of the specified plans
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
    class PlannerPlanItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PlannerPlanItemRequestBuilder.PlannerPlanItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PlannerPlanItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

