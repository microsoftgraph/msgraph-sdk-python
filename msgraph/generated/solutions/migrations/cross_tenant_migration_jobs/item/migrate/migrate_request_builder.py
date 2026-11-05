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
    from ......models.cross_tenant_migration_job import CrossTenantMigrationJob
    from ......models.o_data_errors.o_data_error import ODataError

class MigrateRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the migrate method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MigrateRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/migrations/crossTenantMigrationJobs/{crossTenantMigrationJob%2Did}/migrate", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CrossTenantMigrationJob]:
        """
        Migrate a cross-tenant migration job asynchronously. The job must pass validation before migration can start. After a job is created by using the Create crossTenantMigrationJob method and validated by using the validate action, call this action to start the migration of user data from the source tenant to the target tenant for the specified workloads. Validation results expire after seven days; if expired, revalidate the job before you call the migrate API. This action is asynchronous. After you call the migrate API, poll the Get crossTenantMigrationJob endpoint to check for a terminal status of completed, completedWithErrors, or failed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CrossTenantMigrationJob]
        Find more info here: https://learn.microsoft.com/graph/api/crosstenantmigrationjob-migrate?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.cross_tenant_migration_job import CrossTenantMigrationJob

        return await self.request_adapter.send_async(request_info, CrossTenantMigrationJob, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Migrate a cross-tenant migration job asynchronously. The job must pass validation before migration can start. After a job is created by using the Create crossTenantMigrationJob method and validated by using the validate action, call this action to start the migration of user data from the source tenant to the target tenant for the specified workloads. Validation results expire after seven days; if expired, revalidate the job before you call the migrate API. This action is asynchronous. After you call the migrate API, poll the Get crossTenantMigrationJob endpoint to check for a terminal status of completed, completedWithErrors, or failed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MigrateRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MigrateRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MigrateRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MigrateRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

