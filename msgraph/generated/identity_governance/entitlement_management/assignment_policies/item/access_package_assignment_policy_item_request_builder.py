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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccessPackageAssignmentPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters]] = None) -> Optional[AccessPackageAssignmentPolicy]:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_policy import AccessPackageAssignmentPolicy

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)
    
    async def put(self,body: AccessPackageAssignmentPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccessPackageAssignmentPolicy]:
        """
        Update an existing accessPackageAssignmentPolicy object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageAssignmentPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_assignment_policy import AccessPackageAssignmentPolicy

        return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        In Microsoft Entra entitlement management, delete an accessPackageAssignmentPolicy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignmentPolicy object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: AccessPackageAssignmentPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update an existing accessPackageAssignmentPolicy object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if raw_url is None:
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
    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters():
        """
        In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignmentPolicy object.
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
    class AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

