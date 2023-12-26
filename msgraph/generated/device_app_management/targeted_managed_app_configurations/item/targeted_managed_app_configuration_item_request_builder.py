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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .apps.apps_request_builder import AppsRequestBuilder
    from .assign.assign_request_builder import AssignRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .deployment_summary.deployment_summary_request_builder import DeploymentSummaryRequestBuilder
    from .target_apps.target_apps_request_builder import TargetAppsRequestBuilder

class TargetedManagedAppConfigurationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TargetedManagedAppConfigurationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/targetedManagedAppConfigurations/{targetedManagedAppConfiguration%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a targetedManagedAppConfiguration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[TargetedManagedAppConfiguration]:
        """
        Read properties and relationships of the targetedManagedAppConfiguration object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TargetedManagedAppConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.targeted_managed_app_configuration import TargetedManagedAppConfiguration

        return await self.request_adapter.send_async(request_info, TargetedManagedAppConfiguration, error_mapping)
    
    async def patch(self,body: Optional[TargetedManagedAppConfiguration] = None, request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[TargetedManagedAppConfiguration]:
        """
        Update the properties of a targetedManagedAppConfiguration object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TargetedManagedAppConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/intune-mam-targetedmanagedappconfiguration-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.targeted_managed_app_configuration import TargetedManagedAppConfiguration

        return await self.request_adapter.send_async(request_info, TargetedManagedAppConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a targetedManagedAppConfiguration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the targetedManagedAppConfiguration object.
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
    
    def to_patch_request_information(self,body: Optional[TargetedManagedAppConfiguration] = None, request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a targetedManagedAppConfiguration object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TargetedManagedAppConfigurationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TargetedManagedAppConfigurationItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TargetedManagedAppConfigurationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def apps(self) -> AppsRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        from .apps.apps_request_builder import AppsRequestBuilder

        return AppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign(self) -> AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign.assign_request_builder import AssignRequestBuilder

        return AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_summary(self) -> DeploymentSummaryRequestBuilder:
        """
        Provides operations to manage the deploymentSummary property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        from .deployment_summary.deployment_summary_request_builder import DeploymentSummaryRequestBuilder

        return DeploymentSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target_apps(self) -> TargetAppsRequestBuilder:
        """
        Provides operations to call the targetApps method.
        """
        from .target_apps.target_apps_request_builder import TargetAppsRequestBuilder

        return TargetAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the targetedManagedAppConfiguration object.
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
    class TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TargetedManagedAppConfigurationItemRequestBuilder.TargetedManagedAppConfigurationItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

