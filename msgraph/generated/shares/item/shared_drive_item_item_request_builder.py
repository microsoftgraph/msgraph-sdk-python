from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import shared_drive_item
    from ...models.o_data_errors import o_data_error
    from .drive_item import drive_item_request_builder
    from .items import items_request_builder
    from .list import list_request_builder
    from .list_item import list_item_request_builder
    from .permission import permission_request_builder
    from .root import root_request_builder
    from .site import site_request_builder

class SharedDriveItemItemRequestBuilder():
    """
    Provides operations to manage the collection of sharedDriveItem entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SharedDriveItemItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/shares/{sharedDriveItem%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from shares
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[shared_drive_item.SharedDriveItem]:
        """
        Access a shared DriveItem or a collection of shared items by using a **shareId** or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[shared_drive_item.SharedDriveItem]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import shared_drive_item

        return await self.request_adapter.send_async(request_info, shared_drive_item.SharedDriveItem, error_mapping)
    
    async def patch(self,body: Optional[shared_drive_item.SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[shared_drive_item.SharedDriveItem]:
        """
        Update entity in shares
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[shared_drive_item.SharedDriveItem]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import shared_drive_item

        return await self.request_adapter.send_async(request_info, shared_drive_item.SharedDriveItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from shares
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Access a shared DriveItem or a collection of shared items by using a **shareId** or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[shared_drive_item.SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in shares
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def drive_item(self) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.sharedDriveItem entity.
        """
        from .drive_item import drive_item_request_builder

        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.sharedDriveItem entity.
        """
        from .items import items_request_builder

        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list(self) -> list_request_builder.ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.sharedDriveItem entity.
        """
        from .list import list_request_builder

        return list_request_builder.ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.sharedDriveItem entity.
        """
        from .list_item import list_item_request_builder

        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission(self) -> permission_request_builder.PermissionRequestBuilder:
        """
        Provides operations to manage the permission property of the microsoft.graph.sharedDriveItem entity.
        """
        from .permission import permission_request_builder

        return permission_request_builder.PermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> root_request_builder.RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.sharedDriveItem entity.
        """
        from .root import root_request_builder

        return root_request_builder.RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site(self) -> site_request_builder.SiteRequestBuilder:
        """
        Provides operations to manage the site property of the microsoft.graph.sharedDriveItem entity.
        """
        from .site import site_request_builder

        return site_request_builder.SiteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SharedDriveItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SharedDriveItemItemRequestBuilderGetQueryParameters():
        """
        Access a shared DriveItem or a collection of shared items by using a **shareId** or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SharedDriveItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SharedDriveItemItemRequestBuilder.SharedDriveItemItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SharedDriveItemItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

