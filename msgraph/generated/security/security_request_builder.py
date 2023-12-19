from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.security.security import Security
    from .alerts.alerts_request_builder import AlertsRequestBuilder
    from .alerts_v2.alerts_v2_request_builder import Alerts_v2RequestBuilder
    from .attack_simulation.attack_simulation_request_builder import AttackSimulationRequestBuilder
    from .cases.cases_request_builder import CasesRequestBuilder
    from .incidents.incidents_request_builder import IncidentsRequestBuilder
    from .microsoft_graph_security_run_hunting_query.microsoft_graph_security_run_hunting_query_request_builder import MicrosoftGraphSecurityRunHuntingQueryRequestBuilder
    from .secure_scores.secure_scores_request_builder import SecureScoresRequestBuilder
    from .secure_score_control_profiles.secure_score_control_profiles_request_builder import SecureScoreControlProfilesRequestBuilder
    from .subject_rights_requests.subject_rights_requests_request_builder import SubjectRightsRequestsRequestBuilder
    from .threat_intelligence.threat_intelligence_request_builder import ThreatIntelligenceRequestBuilder
    from .triggers.triggers_request_builder import TriggersRequestBuilder
    from .trigger_types.trigger_types_request_builder import TriggerTypesRequestBuilder

class SecurityRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the security singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SecurityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> Optional[Security]:
        """
        Get security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Security]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security.security import Security

        return await self.request_adapter.send_async(request_info, Security, error_mapping)
    
    async def patch(self,body: Optional[Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> Optional[Security]:
        """
        Update security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Security]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security.security import Security

        return await self.request_adapter.send_async(request_info, Security, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SecurityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Security] = None, request_configuration: Optional[SecurityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SecurityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SecurityRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SecurityRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def alerts(self) -> AlertsRequestBuilder:
        """
        Provides operations to manage the alerts property of the microsoft.graph.security entity.
        """
        from .alerts.alerts_request_builder import AlertsRequestBuilder

        return AlertsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def alerts_v2(self) -> Alerts_v2RequestBuilder:
        """
        Provides operations to manage the alerts_v2 property of the microsoft.graph.security entity.
        """
        from .alerts_v2.alerts_v2_request_builder import Alerts_v2RequestBuilder

        return Alerts_v2RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attack_simulation(self) -> AttackSimulationRequestBuilder:
        """
        Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
        """
        from .attack_simulation.attack_simulation_request_builder import AttackSimulationRequestBuilder

        return AttackSimulationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cases(self) -> CasesRequestBuilder:
        """
        Provides operations to manage the cases property of the microsoft.graph.security entity.
        """
        from .cases.cases_request_builder import CasesRequestBuilder

        return CasesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incidents(self) -> IncidentsRequestBuilder:
        """
        Provides operations to manage the incidents property of the microsoft.graph.security entity.
        """
        from .incidents.incidents_request_builder import IncidentsRequestBuilder

        return IncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_run_hunting_query(self) -> MicrosoftGraphSecurityRunHuntingQueryRequestBuilder:
        """
        Provides operations to call the runHuntingQuery method.
        """
        from .microsoft_graph_security_run_hunting_query.microsoft_graph_security_run_hunting_query_request_builder import MicrosoftGraphSecurityRunHuntingQueryRequestBuilder

        return MicrosoftGraphSecurityRunHuntingQueryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_score_control_profiles(self) -> SecureScoreControlProfilesRequestBuilder:
        """
        Provides operations to manage the secureScoreControlProfiles property of the microsoft.graph.security entity.
        """
        from .secure_score_control_profiles.secure_score_control_profiles_request_builder import SecureScoreControlProfilesRequestBuilder

        return SecureScoreControlProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secure_scores(self) -> SecureScoresRequestBuilder:
        """
        Provides operations to manage the secureScores property of the microsoft.graph.security entity.
        """
        from .secure_scores.secure_scores_request_builder import SecureScoresRequestBuilder

        return SecureScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subject_rights_requests(self) -> SubjectRightsRequestsRequestBuilder:
        """
        Provides operations to manage the subjectRightsRequests property of the microsoft.graph.security entity.
        """
        from .subject_rights_requests.subject_rights_requests_request_builder import SubjectRightsRequestsRequestBuilder

        return SubjectRightsRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_intelligence(self) -> ThreatIntelligenceRequestBuilder:
        """
        Provides operations to manage the threatIntelligence property of the microsoft.graph.security entity.
        """
        from .threat_intelligence.threat_intelligence_request_builder import ThreatIntelligenceRequestBuilder

        return ThreatIntelligenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger_types(self) -> TriggerTypesRequestBuilder:
        """
        Provides operations to manage the triggerTypes property of the microsoft.graph.security entity.
        """
        from .trigger_types.trigger_types_request_builder import TriggerTypesRequestBuilder

        return TriggerTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def triggers(self) -> TriggersRequestBuilder:
        """
        Provides operations to manage the triggers property of the microsoft.graph.security entity.
        """
        from .triggers.triggers_request_builder import TriggersRequestBuilder

        return TriggersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Get security
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SecurityRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SecurityRequestBuilder.SecurityRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SecurityRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

