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
    from .....models.access_package_catalog import AccessPackageCatalog
    from .....models.o_data_errors.o_data_error import ODataError
    from .access_packages.access_packages_request_builder import AccessPackagesRequestBuilder
    from .custom_workflow_extensions.custom_workflow_extensions_request_builder import CustomWorkflowExtensionsRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .resource_roles.resource_roles_request_builder import ResourceRolesRequestBuilder
    from .resource_scopes.resource_scopes_request_builder import ResourceScopesRequestBuilder

class AccessPackageCatalogItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the catalogs property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccessPackageCatalogItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete an accessPackageCatalog.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AccessPackageCatalogItemRequestBuilderGetQueryParameters]] = None) -> Optional[AccessPackageCatalog]:
        """
        Retrieve the properties and relationships of an accessPackageCatalog object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCatalog]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-get?view=graph-rest-1.0
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
        from .....models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    async def patch(self,body: AccessPackageCatalog, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AccessPackageCatalog]:
        """
        Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCatalog]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an accessPackageCatalog.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AccessPackageCatalogItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an accessPackageCatalog object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AccessPackageCatalog, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.
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
    
    def with_url(self,raw_url: str) -> AccessPackageCatalogItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageCatalogItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AccessPackageCatalogItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access_packages(self) -> AccessPackagesRequestBuilder:
        """
        Provides operations to manage the accessPackages property of the microsoft.graph.accessPackageCatalog entity.
        """
        from .access_packages.access_packages_request_builder import AccessPackagesRequestBuilder

        return AccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_workflow_extensions(self) -> CustomWorkflowExtensionsRequestBuilder:
        """
        Provides operations to manage the customWorkflowExtensions property of the microsoft.graph.accessPackageCatalog entity.
        """
        from .custom_workflow_extensions.custom_workflow_extensions_request_builder import CustomWorkflowExtensionsRequestBuilder

        return CustomWorkflowExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_roles(self) -> ResourceRolesRequestBuilder:
        """
        Provides operations to manage the resourceRoles property of the microsoft.graph.accessPackageCatalog entity.
        """
        from .resource_roles.resource_roles_request_builder import ResourceRolesRequestBuilder

        return ResourceRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_scopes(self) -> ResourceScopesRequestBuilder:
        """
        Provides operations to manage the resourceScopes property of the microsoft.graph.accessPackageCatalog entity.
        """
        from .resource_scopes.resource_scopes_request_builder import ResourceScopesRequestBuilder

        return ResourceScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.accessPackageCatalog entity.
        """
        from .resources.resources_request_builder import ResourcesRequestBuilder

        return ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackageCatalogItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageCatalogItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an accessPackageCatalog object.
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
    class AccessPackageCatalogItemRequestBuilderGetRequestConfiguration(RequestConfiguration[AccessPackageCatalogItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AccessPackageCatalogItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

