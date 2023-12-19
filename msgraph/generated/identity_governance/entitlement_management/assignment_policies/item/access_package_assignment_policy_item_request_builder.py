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
    from .....models.access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_package.access_package_request_builder import AccessPackageRequestBuilder
    from .catalog.catalog_request_builder import CatalogRequestBuilder
    from .custom_extension_stage_settings.custom_extension_stage_settings_request_builder import CustomExtensionStageSettingsRequestBuilder
    from .questions.questions_request_builder import QuestionsRequestBuilder

class AccessPackageAssignmentPolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageAssignmentPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        In Microsoft Entra entitlement management, delete an accessPackageAssignmentPolicy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageAssignmentPolicy]:
        """
        In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignmentPolicy object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_policy import AccessPackageAssignmentPolicy

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)
    
    async def put(self,body: Optional[AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration] = None) -> Optional[AccessPackageAssignmentPolicy]:
        """
        Update the navigation property assignmentPolicies in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentPolicy]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_policy import AccessPackageAssignmentPolicy

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        In Microsoft Entra entitlement management, delete an accessPackageAssignmentPolicy.
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignmentPolicy object.
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
    
    def to_put_request_information(self,body: Optional[AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property assignmentPolicies in identityGovernance
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
        request_info.http_method = Method.PUT
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessPackageAssignmentPolicyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access_package(self) -> AccessPackageRequestBuilder:
        """
        Provides operations to manage the accessPackage property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .access_package.access_package_request_builder import AccessPackageRequestBuilder

        return AccessPackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def catalog(self) -> CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .catalog.catalog_request_builder import CatalogRequestBuilder

        return CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_extension_stage_settings(self) -> CustomExtensionStageSettingsRequestBuilder:
        """
        Provides operations to manage the customExtensionStageSettings property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .custom_extension_stage_settings.custom_extension_stage_settings_request_builder import CustomExtensionStageSettingsRequestBuilder

        return CustomExtensionStageSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def questions(self) -> QuestionsRequestBuilder:
        """
        Provides operations to manage the questions property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .questions.questions_request_builder import QuestionsRequestBuilder

        return QuestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters():
        """
        In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignmentPolicy object.
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
    class AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessPackageAssignmentPolicyItemRequestBuilder.AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

