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

security_reports_root = lazy_import('msgraph.generated.models.security_reports_root')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
get_attack_simulation_repeat_offenders_request_builder = lazy_import('msgraph.generated.reports.security.get_attack_simulation_repeat_offenders.get_attack_simulation_repeat_offenders_request_builder')
get_attack_simulation_simulation_user_coverage_request_builder = lazy_import('msgraph.generated.reports.security.get_attack_simulation_simulation_user_coverage.get_attack_simulation_simulation_user_coverage_request_builder')
get_attack_simulation_training_user_coverage_request_builder = lazy_import('msgraph.generated.reports.security.get_attack_simulation_training_user_coverage.get_attack_simulation_training_user_coverage_request_builder')

class SecurityRequestBuilder():
    """
    Provides operations to manage the security property of the microsoft.graph.reportRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SecurityRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/reports/security{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[SecurityRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property security for reports
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
    
    def create_get_request_information(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get security from reports
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
    
    def create_patch_request_information(self,body: Optional[security_reports_root.SecurityReportsRoot] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property security in reports
        Args:
            body: 
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
    
    async def delete(self,request_configuration: Optional[SecurityRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property security for reports
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
    
    async def get(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[security_reports_root.SecurityReportsRoot]:
        """
        Get security from reports
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[security_reports_root.SecurityReportsRoot]
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
        return await self.request_adapter.send_async(request_info, security_reports_root.SecurityReportsRoot, response_handler, error_mapping)
    
    def get_attack_simulation_repeat_offenders(self,) -> get_attack_simulation_repeat_offenders_request_builder.GetAttackSimulationRepeatOffendersRequestBuilder:
        """
        Provides operations to call the getAttackSimulationRepeatOffenders method.
        Returns: get_attack_simulation_repeat_offenders_request_builder.GetAttackSimulationRepeatOffendersRequestBuilder
        """
        return get_attack_simulation_repeat_offenders_request_builder.GetAttackSimulationRepeatOffendersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_attack_simulation_simulation_user_coverage(self,) -> get_attack_simulation_simulation_user_coverage_request_builder.GetAttackSimulationSimulationUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationSimulationUserCoverage method.
        Returns: get_attack_simulation_simulation_user_coverage_request_builder.GetAttackSimulationSimulationUserCoverageRequestBuilder
        """
        return get_attack_simulation_simulation_user_coverage_request_builder.GetAttackSimulationSimulationUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_attack_simulation_training_user_coverage(self,) -> get_attack_simulation_training_user_coverage_request_builder.GetAttackSimulationTrainingUserCoverageRequestBuilder:
        """
        Provides operations to call the getAttackSimulationTrainingUserCoverage method.
        Returns: get_attack_simulation_training_user_coverage_request_builder.GetAttackSimulationTrainingUserCoverageRequestBuilder
        """
        return get_attack_simulation_training_user_coverage_request_builder.GetAttackSimulationTrainingUserCoverageRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def patch(self,body: Optional[security_reports_root.SecurityReportsRoot] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[security_reports_root.SecurityReportsRoot]:
        """
        Update the navigation property security in reports
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[security_reports_root.SecurityReportsRoot]
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
        return await self.request_adapter.send_async(request_info, security_reports_root.SecurityReportsRoot, response_handler, error_mapping)
    
    @dataclass
    class SecurityRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Get security from reports
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
    class SecurityRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SecurityRequestBuilder.SecurityRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SecurityRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

