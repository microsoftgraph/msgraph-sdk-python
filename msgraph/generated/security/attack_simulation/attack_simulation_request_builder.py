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
    from ...models.attack_simulation_root import AttackSimulationRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .end_user_notifications.end_user_notifications_request_builder import EndUserNotificationsRequestBuilder
    from .landing_pages.landing_pages_request_builder import LandingPagesRequestBuilder
    from .login_pages.login_pages_request_builder import LoginPagesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .payloads.payloads_request_builder import PayloadsRequestBuilder
    from .simulations.simulations_request_builder import SimulationsRequestBuilder
    from .simulation_automations.simulation_automations_request_builder import SimulationAutomationsRequestBuilder
    from .trainings.trainings_request_builder import TrainingsRequestBuilder

class AttackSimulationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the attackSimulation property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AttackSimulationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/attackSimulation{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property attackSimulation for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AttackSimulationRequestBuilderGetQueryParameters]] = None) -> Optional[AttackSimulationRoot]:
        """
        Get attackSimulation from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AttackSimulationRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.attack_simulation_root import AttackSimulationRoot

        return await self.request_adapter.send_async(request_info, AttackSimulationRoot, error_mapping)
    
    async def patch(self,body: AttackSimulationRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AttackSimulationRoot]:
        """
        Update the navigation property attackSimulation in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AttackSimulationRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.attack_simulation_root import AttackSimulationRoot

        return await self.request_adapter.send_async(request_info, AttackSimulationRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property attackSimulation for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AttackSimulationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get attackSimulation from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AttackSimulationRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property attackSimulation in security
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
    
    def with_url(self,raw_url: str) -> AttackSimulationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AttackSimulationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AttackSimulationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def end_user_notifications(self) -> EndUserNotificationsRequestBuilder:
        """
        Provides operations to manage the endUserNotifications property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .end_user_notifications.end_user_notifications_request_builder import EndUserNotificationsRequestBuilder

        return EndUserNotificationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def landing_pages(self) -> LandingPagesRequestBuilder:
        """
        Provides operations to manage the landingPages property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .landing_pages.landing_pages_request_builder import LandingPagesRequestBuilder

        return LandingPagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def login_pages(self) -> LoginPagesRequestBuilder:
        """
        Provides operations to manage the loginPages property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .login_pages.login_pages_request_builder import LoginPagesRequestBuilder

        return LoginPagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payloads(self) -> PayloadsRequestBuilder:
        """
        Provides operations to manage the payloads property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .payloads.payloads_request_builder import PayloadsRequestBuilder

        return PayloadsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def simulation_automations(self) -> SimulationAutomationsRequestBuilder:
        """
        Provides operations to manage the simulationAutomations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .simulation_automations.simulation_automations_request_builder import SimulationAutomationsRequestBuilder

        return SimulationAutomationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def simulations(self) -> SimulationsRequestBuilder:
        """
        Provides operations to manage the simulations property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .simulations.simulations_request_builder import SimulationsRequestBuilder

        return SimulationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trainings(self) -> TrainingsRequestBuilder:
        """
        Provides operations to manage the trainings property of the microsoft.graph.attackSimulationRoot entity.
        """
        from .trainings.trainings_request_builder import TrainingsRequestBuilder

        return TrainingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AttackSimulationRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AttackSimulationRequestBuilderGetQueryParameters():
        """
        Get attackSimulation from security
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
    class AttackSimulationRequestBuilderGetRequestConfiguration(RequestConfiguration[AttackSimulationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AttackSimulationRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

