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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageCatalogItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/catalogs/{accessPackageCatalog%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessPackageCatalogItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
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

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageCatalogItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessPackageCatalog]:
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

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    async def patch(self,body: Optional[AccessPackageCatalog] = None, request_configuration: Optional[AccessPackageCatalogItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessPackageCatalog]:
        """
        Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCatalog]
        Find more info here: https://learn.microsoft.com/graph/api/accesspackagecatalog-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_package_catalog import AccessPackageCatalog

        return await self.request_adapter.send_async(request_info, AccessPackageCatalog, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageCatalogItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessPackageCatalog.
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageCatalogItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an accessPackageCatalog object.
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
    
    def to_patch_request_information(self,body: Optional[AccessPackageCatalog] = None, request_configuration: Optional[AccessPackageCatalogItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessPackageCatalogItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackageCatalogItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageCatalogItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessPackageCatalogItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an accessPackageCatalog object.
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
    class AccessPackageCatalogItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessPackageCatalogItemRequestBuilder.AccessPackageCatalogItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessPackageCatalogItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

