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
    from ....models.cross_tenant_migration_job import CrossTenantMigrationJob
    from ....models.o_data_errors.o_data_error import ODataError
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .migrate.migrate_request_builder import MigrateRequestBuilder
    from .validate.validate_request_builder import ValidateRequestBuilder

class CrossTenantMigrationJobsWithDisplayNameRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the crossTenantMigrationJobs property of the microsoft.graph.migrationsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], display_name: Optional[str] = None) -> None:
        """
        Instantiates a new CrossTenantMigrationJobsWithDisplayNameRequestBuilder and sets the default values.
        param display_name: Alternate key of crossTenantMigrationJob
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['displayName'] = display_name
        super().__init__(request_adapter, "{+baseurl}/solutions/migrations/crossTenantMigrationJobs(displayName='{displayName}'){?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a crossTenantMigrationJob object. Delete requests are long-running and finish within 48 hours. A crossTenantMigrationJob that is currently in progress can't be deleted. You can perform the deletion only after the crossTenantMigrationJob reaches a final state. If a crossTenantMigrationJob isn't in a final state, a 409 Conflict response is returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/migrationsroot-delete-crosstenantmigrationjobs?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CrossTenantMigrationJobsWithDisplayNameRequestBuilderGetQueryParameters]] = None) -> Optional[CrossTenantMigrationJob]:
        """
        Read the properties and relationships of a crossTenantMigrationJob object. This API provides details about the migration job, but not about the individual crossTenantMigrationTasks objects associated with the migration job.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CrossTenantMigrationJob]
        Find more info here: https://learn.microsoft.com/graph/api/crosstenantmigrationjob-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cross_tenant_migration_job import CrossTenantMigrationJob

        return await self.request_adapter.send_async(request_info, CrossTenantMigrationJob, error_mapping)
    
    async def patch(self,body: CrossTenantMigrationJob, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CrossTenantMigrationJob]:
        """
        Update the completeAfterDateTime property of a crossTenantMigrationJob object. Only updates to completeAfterDateTime are supported. This property specifies when the migration job can proceed toward completion. If the value is in the past, the service treats it as already due and proceeds toward completion during its next processing cycle. This behavior doesn't bypass earlier validation or synchronization stages.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CrossTenantMigrationJob]
        Find more info here: https://learn.microsoft.com/graph/api/crosstenantmigrationjob-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cross_tenant_migration_job import CrossTenantMigrationJob

        return await self.request_adapter.send_async(request_info, CrossTenantMigrationJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a crossTenantMigrationJob object. Delete requests are long-running and finish within 48 hours. A crossTenantMigrationJob that is currently in progress can't be deleted. You can perform the deletion only after the crossTenantMigrationJob reaches a final state. If a crossTenantMigrationJob isn't in a final state, a 409 Conflict response is returned.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CrossTenantMigrationJobsWithDisplayNameRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a crossTenantMigrationJob object. This API provides details about the migration job, but not about the individual crossTenantMigrationTasks objects associated with the migration job.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CrossTenantMigrationJob, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the completeAfterDateTime property of a crossTenantMigrationJob object. Only updates to completeAfterDateTime are supported. This property specifies when the migration job can proceed toward completion. If the value is in the past, the service treats it as already due and proceeds toward completion during its next processing cycle. This behavior doesn't bypass earlier validation or synchronization stages.
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
    
    def with_url(self,raw_url: str) -> CrossTenantMigrationJobsWithDisplayNameRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CrossTenantMigrationJobsWithDisplayNameRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CrossTenantMigrationJobsWithDisplayNameRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migrate(self) -> MigrateRequestBuilder:
        """
        Provides operations to call the migrate method.
        """
        from .migrate.migrate_request_builder import MigrateRequestBuilder

        return MigrateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate(self) -> ValidateRequestBuilder:
        """
        Provides operations to call the validate method.
        """
        from .validate.validate_request_builder import ValidateRequestBuilder

        return ValidateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CrossTenantMigrationJobsWithDisplayNameRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CrossTenantMigrationJobsWithDisplayNameRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a crossTenantMigrationJob object. This API provides details about the migration job, but not about the individual crossTenantMigrationTasks objects associated with the migration job.
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
    class CrossTenantMigrationJobsWithDisplayNameRequestBuilderGetRequestConfiguration(RequestConfiguration[CrossTenantMigrationJobsWithDisplayNameRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CrossTenantMigrationJobsWithDisplayNameRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

