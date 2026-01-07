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
    from .....models.file_storage_container import FileStorageContainer
    from .....models.o_data_errors.o_data_error import ODataError
    from .activate.activate_request_builder import ActivateRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .drive.drive_request_builder import DriveRequestBuilder
    from .lock.lock_request_builder import LockRequestBuilder
    from .migration_jobs.migration_jobs_request_builder import MigrationJobsRequestBuilder
    from .permanent_delete.permanent_delete_request_builder import PermanentDeleteRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .provision_migration_containers.provision_migration_containers_request_builder import ProvisionMigrationContainersRequestBuilder
    from .recycle_bin.recycle_bin_request_builder import RecycleBinRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .unlock.unlock_request_builder import UnlockRequestBuilder

class FileStorageContainerItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deletedContainers property of the microsoft.graph.fileStorage entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FileStorageContainerItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/deletedContainers/{fileStorageContainer%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property deletedContainers for storage
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FileStorageContainerItemRequestBuilderGetQueryParameters]] = None) -> Optional[FileStorageContainer]:
        """
        The collection of deleted fileStorageContainer resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileStorageContainer]
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
        from .....models.file_storage_container import FileStorageContainer

        return await self.request_adapter.send_async(request_info, FileStorageContainer, error_mapping)
    
    async def patch(self,body: FileStorageContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileStorageContainer]:
        """
        Update the navigation property deletedContainers in storage
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileStorageContainer]
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
        from .....models.file_storage_container import FileStorageContainer

        return await self.request_adapter.send_async(request_info, FileStorageContainer, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property deletedContainers for storage
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FileStorageContainerItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The collection of deleted fileStorageContainer resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: FileStorageContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property deletedContainers in storage
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
    
    def with_url(self,raw_url: str) -> FileStorageContainerItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FileStorageContainerItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FileStorageContainerItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def activate(self) -> ActivateRequestBuilder:
        """
        Provides operations to call the activate method.
        """
        from .activate.activate_request_builder import ActivateRequestBuilder

        return ActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.fileStorageContainer entity.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.fileStorageContainer entity.
        """
        from .drive.drive_request_builder import DriveRequestBuilder

        return DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lock(self) -> LockRequestBuilder:
        """
        Provides operations to call the lock method.
        """
        from .lock.lock_request_builder import LockRequestBuilder

        return LockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migration_jobs(self) -> MigrationJobsRequestBuilder:
        """
        Provides operations to manage the migrationJobs property of the microsoft.graph.fileStorageContainer entity.
        """
        from .migration_jobs.migration_jobs_request_builder import MigrationJobsRequestBuilder

        return MigrationJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permanent_delete(self) -> PermanentDeleteRequestBuilder:
        """
        Provides operations to call the permanentDelete method.
        """
        from .permanent_delete.permanent_delete_request_builder import PermanentDeleteRequestBuilder

        return PermanentDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.fileStorageContainer entity.
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_migration_containers(self) -> ProvisionMigrationContainersRequestBuilder:
        """
        Provides operations to call the provisionMigrationContainers method.
        """
        from .provision_migration_containers.provision_migration_containers_request_builder import ProvisionMigrationContainersRequestBuilder

        return ProvisionMigrationContainersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recycle_bin(self) -> RecycleBinRequestBuilder:
        """
        Provides operations to manage the recycleBin property of the microsoft.graph.fileStorageContainer entity.
        """
        from .recycle_bin.recycle_bin_request_builder import RecycleBinRequestBuilder

        return RecycleBinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unlock(self) -> UnlockRequestBuilder:
        """
        Provides operations to call the unlock method.
        """
        from .unlock.unlock_request_builder import UnlockRequestBuilder

        return UnlockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FileStorageContainerItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FileStorageContainerItemRequestBuilderGetQueryParameters():
        """
        The collection of deleted fileStorageContainer resources.
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
    class FileStorageContainerItemRequestBuilderGetRequestConfiguration(RequestConfiguration[FileStorageContainerItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FileStorageContainerItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

