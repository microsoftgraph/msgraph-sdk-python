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
    from ......models.access_package_catalog import AccessPackageCatalog
    from ......models.o_data_errors.o_data_error import ODataError
    from .access_packages.access_packages_request_builder import AccessPackagesRequestBuilder
    from .custom_workflow_extensions.custom_workflow_extensions_request_builder import CustomWorkflowExtensionsRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .resource_roles.resource_roles_request_builder import ResourceRolesRequestBuilder
    from .resource_scopes.resource_scopes_request_builder import ResourceScopesRequestBuilder

class CatalogRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the catalog property of the microsoft.graph.accessPackageResourceRequest entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CatalogRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/resourceRequests/{accessPackageResourceRequest%2Did}/catalog{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CatalogRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property catalog for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CatalogRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageCatalog]:
        """
        Get catalog from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCatalog]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    async def patch(self,body: Optional[AccessPackageCatalog] = None, request_configuration: Optional[CatalogRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessPackageCatalog]:
        """
        Update the navigation property catalog in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCatalog]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CatalogRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property catalog for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/identityGovernance/entitlementManagement/resourceRequests/{accessPackageResourceRequest%2Did}/catalog', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CatalogRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get catalog from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[AccessPackageCatalog] = None, request_configuration: Optional[CatalogRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property catalog in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/identityGovernance/entitlementManagement/resourceRequests/{accessPackageResourceRequest%2Did}/catalog', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CatalogRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CatalogRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CatalogRequestBuilder(self.request_adapter, raw_url)
    
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CatalogRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CatalogRequestBuilderGetQueryParameters():
        """
        Get catalog from identityGovernance
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
    class CatalogRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CatalogRequestBuilder.CatalogRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CatalogRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

