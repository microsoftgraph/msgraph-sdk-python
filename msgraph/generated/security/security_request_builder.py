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

security = lazy_import('msgraph.generated.models.security')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
alerts_request_builder = lazy_import('msgraph.generated.security.alerts.alerts_request_builder')
alert_item_request_builder = lazy_import('msgraph.generated.security.alerts.item.alert_item_request_builder')
attack_simulation_request_builder = lazy_import('msgraph.generated.security.attack_simulation.attack_simulation_request_builder')
cases_request_builder = lazy_import('msgraph.generated.security.cases.cases_request_builder')
secure_score_control_profiles_request_builder = lazy_import('msgraph.generated.security.secure_score_control_profiles.secure_score_control_profiles_request_builder')
secure_score_control_profile_item_request_builder = lazy_import('msgraph.generated.security.secure_score_control_profiles.item.secure_score_control_profile_item_request_builder')
secure_scores_request_builder = lazy_import('msgraph.generated.security.secure_scores.secure_scores_request_builder')
secure_score_item_request_builder = lazy_import('msgraph.generated.security.secure_scores.item.secure_score_item_request_builder')

class SecurityRequestBuilder():
    """
    Provides operations to manage the security singleton.
    """
    def alerts(self) -> alerts_request_builder.AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        """
        return alerts_request_builder.AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attack_simulation(self) -> attack_simulation_request_builder.AttackSimulationRequestBuilder:
        """
        Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
        """
        return attack_simulation_request_builder.AttackSimulationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def cases(self) -> cases_request_builder.CasesRequestBuilder:
        """
        Provides operations to manage the cases property of the microsoft.graph.security entity.
        """
        return cases_request_builder.CasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def secure_score_control_profiles(self) -> secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        """
        return secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def secure_scores(self) -> secure_scores_request_builder.SecureScoresRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        """
        return secure_scores_request_builder.SecureScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    def alerts_by_id(self,id: str) -> alert_item_request_builder.AlertItemRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: alert_item_request_builder.AlertItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["alert%2Did"] = id
        return alert_item_request_builder.AlertItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        self.url_template: str = "{+baseurl}/security{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get security
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
    
    def create_patch_request_information(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update security
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
    
    async def get(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[security.Security]:
        """
        Get security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[security.Security]
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
        return await self.request_adapter.send_async(request_info, security.Security, response_handler, error_mapping)
    
    async def patch(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[security.Security]:
        """
        Update security
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[security.Security]
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
        return await self.request_adapter.send_async(request_info, security.Security, response_handler, error_mapping)
    
    def secure_score_control_profiles_by_id(self,id: str) -> secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["secureScoreControlProfile%2Did"] = id
        return secure_score_control_profile_item_request_builder.SecureScoreControlProfileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def secure_scores_by_id(self,id: str) -> secure_score_item_request_builder.SecureScoreItemRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        Args:
            id: Unique identifier of the item
        Returns: secure_score_item_request_builder.SecureScoreItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["secureScore%2Did"] = id
        return secure_score_item_request_builder.SecureScoreItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Get security
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

    

