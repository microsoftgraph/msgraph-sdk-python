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
    from ...models.migrations_root import MigrationsRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .cross_tenant_migration_jobs.cross_tenant_migration_jobs_request_builder import CrossTenantMigrationJobsRequestBuilder
    from .cross_tenant_migration_jobs_with_display_name.cross_tenant_migration_jobs_with_display_name_request_builder import CrossTenantMigrationJobsWithDisplayNameRequestBuilder

class MigrationsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the migrations property of the microsoft.graph.solutionsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MigrationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/migrations{?%24expand,%24select}", path_parameters)
    
    def cross_tenant_migration_jobs_with_display_name(self,display_name: str) -> CrossTenantMigrationJobsWithDisplayNameRequestBuilder:
        """
        Provides operations to manage the crossTenantMigrationJobs property of the microsoft.graph.migrationsRoot entity.
        param display_name: Alternate key of crossTenantMigrationJob
        Returns: CrossTenantMigrationJobsWithDisplayNameRequestBuilder
        """
        if display_name is None:
            raise TypeError("display_name cannot be null.")
        from .cross_tenant_migration_jobs_with_display_name.cross_tenant_migration_jobs_with_display_name_request_builder import CrossTenantMigrationJobsWithDisplayNameRequestBuilder

        return CrossTenantMigrationJobsWithDisplayNameRequestBuilder(self.request_adapter, self.path_parameters, display_name)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property migrations for solutions
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MigrationsRequestBuilderGetQueryParameters]] = None) -> Optional[MigrationsRoot]:
        """
        The entry point for cross-tenant migration operations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MigrationsRoot]
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
        from ...models.migrations_root import MigrationsRoot

        return await self.request_adapter.send_async(request_info, MigrationsRoot, error_mapping)
    
    async def patch(self,body: MigrationsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MigrationsRoot]:
        """
        Update the navigation property migrations in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MigrationsRoot]
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
        from ...models.migrations_root import MigrationsRoot

        return await self.request_adapter.send_async(request_info, MigrationsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property migrations for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MigrationsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The entry point for cross-tenant migration operations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: MigrationsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property migrations in solutions
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
    
    def with_url(self,raw_url: str) -> MigrationsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MigrationsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MigrationsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cross_tenant_migration_jobs(self) -> CrossTenantMigrationJobsRequestBuilder:
        """
        Provides operations to manage the crossTenantMigrationJobs property of the microsoft.graph.migrationsRoot entity.
        """
        from .cross_tenant_migration_jobs.cross_tenant_migration_jobs_request_builder import CrossTenantMigrationJobsRequestBuilder

        return CrossTenantMigrationJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MigrationsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MigrationsRequestBuilderGetQueryParameters():
        """
        The entry point for cross-tenant migration operations.
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
    class MigrationsRequestBuilderGetRequestConfiguration(RequestConfiguration[MigrationsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MigrationsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

