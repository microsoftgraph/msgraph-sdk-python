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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.shared_drive_item import SharedDriveItem
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .drive_item.drive_item_request_builder import DriveItemRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .list_item.list_item_request_builder import ListItemRequestBuilder
    from .permission.permission_request_builder import PermissionRequestBuilder
    from .root.root_request_builder import RootRequestBuilder
    from .site.site_request_builder import SiteRequestBuilder

class SharedDriveItemItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of sharedDriveItem entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SharedDriveItemItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/shares/{sharedDriveItem%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from shares
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[SharedDriveItem]:
        """
        Access a shared DriveItem or a collection of shared items by using a shareId or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharedDriveItem]
        Find more info here: https://learn.microsoft.com/graph/api/shares-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.shared_drive_item import SharedDriveItem

        return await self.request_adapter.send_async(request_info, SharedDriveItem, error_mapping)
    
    async def patch(self,body: Optional[SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[SharedDriveItem]:
        """
        Update entity in shares
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharedDriveItem]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.shared_drive_item import SharedDriveItem

        return await self.request_adapter.send_async(request_info, SharedDriveItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from shares
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
    
    def to_get_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Access a shared DriveItem or a collection of shared items by using a shareId or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
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
    
    def to_patch_request_information(self,body: Optional[SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in shares
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
    
    def with_url(self,raw_url: Optional[str] = None) -> SharedDriveItemItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SharedDriveItemItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SharedDriveItemItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_item(self) -> DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.sharedDriveItem entity.
        """
        from .drive_item.drive_item_request_builder import DriveItemRequestBuilder

        return DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.sharedDriveItem entity.
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.sharedDriveItem entity.
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.sharedDriveItem entity.
        """
        from .list_item.list_item_request_builder import ListItemRequestBuilder

        return ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission(self) -> PermissionRequestBuilder:
        """
        Provides operations to manage the permission property of the microsoft.graph.sharedDriveItem entity.
        """
        from .permission.permission_request_builder import PermissionRequestBuilder

        return PermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.sharedDriveItem entity.
        """
        from .root.root_request_builder import RootRequestBuilder

        return RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site(self) -> SiteRequestBuilder:
        """
        Provides operations to manage the site property of the microsoft.graph.sharedDriveItem entity.
        """
        from .site.site_request_builder import SiteRequestBuilder

        return SiteRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SharedDriveItemItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class SharedDriveItemItemRequestBuilderGetQueryParameters():
        """
        Access a shared DriveItem or a collection of shared items by using a shareId or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
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
    class SharedDriveItemItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SharedDriveItemItemRequestBuilder.SharedDriveItemItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SharedDriveItemItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

