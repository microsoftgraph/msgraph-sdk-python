from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.security.security import Security
    from .alerts.alerts_request_builder import AlertsRequestBuilder
    from .alerts_v2.alerts_v2_request_builder import Alerts_v2RequestBuilder
    from .attack_simulation.attack_simulation_request_builder import AttackSimulationRequestBuilder
    from .cases.cases_request_builder import CasesRequestBuilder
    from .data_security_and_governance.data_security_and_governance_request_builder import DataSecurityAndGovernanceRequestBuilder
    from .identities.identities_request_builder import IdentitiesRequestBuilder
    from .incidents.incidents_request_builder import IncidentsRequestBuilder
    from .labels.labels_request_builder import LabelsRequestBuilder
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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SecurityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SecurityRequestBuilderGetQueryParameters]] = None) -> Optional[Security]:
        """
        Get security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Security]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security.security import Security

        return await self.request_adapter.send_async(request_info, Security, error_mapping)
    
    async def patch(self,body: Security, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Security]:
        """
        Update security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Security]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.security.security import Security

        return await self.request_adapter.send_async(request_info, Security, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SecurityRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Security, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update security
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
    
    def with_url(self,raw_url: str) -> SecurityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SecurityRequestBuilder
        """
        if raw_url is None:
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
    def data_security_and_governance(self) -> DataSecurityAndGovernanceRequestBuilder:
        """
        Provides operations to manage the dataSecurityAndGovernance property of the microsoft.graph.security entity.
        """
        from .data_security_and_governance.data_security_and_governance_request_builder import DataSecurityAndGovernanceRequestBuilder

        return DataSecurityAndGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identities(self) -> IdentitiesRequestBuilder:
        """
        Provides operations to manage the identities property of the microsoft.graph.security entity.
        """
        from .identities.identities_request_builder import IdentitiesRequestBuilder

        return IdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incidents(self) -> IncidentsRequestBuilder:
        """
        Provides operations to manage the incidents property of the microsoft.graph.security entity.
        """
        from .incidents.incidents_request_builder import IncidentsRequestBuilder

        return IncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def labels(self) -> LabelsRequestBuilder:
        """
        Provides operations to manage the labels property of the microsoft.graph.security entity.
        """
        from .labels.labels_request_builder import LabelsRequestBuilder

        return LabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class SecurityRequestBuilderGetRequestConfiguration(RequestConfiguration[SecurityRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SecurityRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

