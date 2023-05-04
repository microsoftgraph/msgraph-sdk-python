from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors import o_data_error
    from ..models.security import security
    from .alerts import alerts_request_builder
    from .alerts_v2 import alerts_v2_request_builder
    from .attack_simulation import attack_simulation_request_builder
    from .cases import cases_request_builder
    from .incidents import incidents_request_builder
    from .microsoft_graph_security_run_hunting_query import microsoft_graph_security_run_hunting_query_request_builder
    from .secure_score_control_profiles import secure_score_control_profiles_request_builder
    from .secure_scores import secure_scores_request_builder
    from .triggers import triggers_request_builder
    from .trigger_types import trigger_types_request_builder

class SecurityRequestBuilder():
    """
    Provides operations to manage the security singleton.
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
        self.url_template: str = "{+baseurl}/security{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> Optional[security.Security]:
        """
        Get security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[security.Security]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security import security

        return await self.request_adapter.send_async(request_info, security.Security, error_mapping)
    
    async def patch(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> Optional[security.Security]:
        """
        Update security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[security.Security]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security import security

        return await self.request_adapter.send_async(request_info, security.Security, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[security.Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update security
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def alerts(self) -> alerts_request_builder.AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        """
        from .alerts import alerts_request_builder

        return alerts_request_builder.AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alerts_v2(self) -> alerts_v2_request_builder.Alerts_v2RequestBuilder:
        """
        Provides operations to manage the alerts_v2 property of the microsoft.graph.security entity.
        """
        from .alerts_v2 import alerts_v2_request_builder

        return alerts_v2_request_builder.Alerts_v2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attack_simulation(self) -> attack_simulation_request_builder.AttackSimulationRequestBuilder:
        """
        Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
        """
        from .attack_simulation import attack_simulation_request_builder

        return attack_simulation_request_builder.AttackSimulationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cases(self) -> cases_request_builder.CasesRequestBuilder:
        """
        Provides operations to manage the cases property of the microsoft.graph.security entity.
        """
        from .cases import cases_request_builder

        return cases_request_builder.CasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incidents(self) -> incidents_request_builder.IncidentsRequestBuilder:
        """
        Provides operations to manage the incidents property of the microsoft.graph.security entity.
        """
        from .incidents import incidents_request_builder

        return incidents_request_builder.IncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_run_hunting_query(self) -> microsoft_graph_security_run_hunting_query_request_builder.MicrosoftGraphSecurityRunHuntingQueryRequestBuilder:
        """
        Provides operations to call the runHuntingQuery method.
        """
        from .microsoft_graph_security_run_hunting_query import microsoft_graph_security_run_hunting_query_request_builder

        return microsoft_graph_security_run_hunting_query_request_builder.MicrosoftGraphSecurityRunHuntingQueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_score_control_profiles(self) -> secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        """
        from .secure_score_control_profiles import secure_score_control_profiles_request_builder

        return secure_score_control_profiles_request_builder.SecureScoreControlProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_scores(self) -> secure_scores_request_builder.SecureScoresRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        """
        from .secure_scores import secure_scores_request_builder

        return secure_scores_request_builder.SecureScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def triggers(self) -> triggers_request_builder.TriggersRequestBuilder:
        """
        Provides operations to manage the triggers property of the microsoft.graph.security entity.
        """
        from .triggers import triggers_request_builder

        return triggers_request_builder.TriggersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_types(self) -> trigger_types_request_builder.TriggerTypesRequestBuilder:
        """
        Provides operations to manage the triggerTypes property of the microsoft.graph.security entity.
        """
        from .trigger_types import trigger_types_request_builder

        return trigger_types_request_builder.TriggerTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Get security
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SecurityRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

