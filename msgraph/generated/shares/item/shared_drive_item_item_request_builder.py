from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

shared_drive_item = lazy_import('msgraph.generated.models.shared_drive_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
drive_item_request_builder = lazy_import('msgraph.generated.shares.item.drive_item.drive_item_request_builder')
items_request_builder = lazy_import('msgraph.generated.shares.item.items.items_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.shares.item.items.item.drive_item_item_request_builder')
list_request_builder = lazy_import('msgraph.generated.shares.item.list.list_request_builder')
list_item_request_builder = lazy_import('msgraph.generated.shares.item.list_item.list_item_request_builder')
permission_request_builder = lazy_import('msgraph.generated.shares.item.permission.permission_request_builder')
root_request_builder = lazy_import('msgraph.generated.shares.item.root.root_request_builder')
site_request_builder = lazy_import('msgraph.generated.shares.item.site.site_request_builder')

class SharedDriveItemItemRequestBuilder():
    """
    Provides operations to manage the collection of sharedDriveItem entities.
    """
    @property
    def drive_item(self) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.sharedDriveItem entity.
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.sharedDriveItem entity.
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list(self) -> list_request_builder.ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.sharedDriveItem entity.
        """
        return list_request_builder.ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.sharedDriveItem entity.
        """
        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission(self) -> permission_request_builder.PermissionRequestBuilder:
        """
        Provides operations to manage the permission property of the microsoft.graph.sharedDriveItem entity.
        """
        return permission_request_builder.PermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> root_request_builder.RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.sharedDriveItem entity.
        """
        return root_request_builder.RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site(self) -> site_request_builder.SiteRequestBuilder:
        """
        Provides operations to manage the site property of the microsoft.graph.sharedDriveItem entity.
        """
        return site_request_builder.SiteRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    def create_delete_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def create_get_request_information(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[shared_drive_item.SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete entity from shares
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[SharedDriveItemItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[shared_drive_item.SharedDriveItem]:
        """
        Access a shared DriveItem or a collection of shared items by using a **shareId** or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[shared_drive_item.SharedDriveItem]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, shared_drive_item.SharedDriveItem, response_handler, error_mapping)
    
    def items_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.sharedDriveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[shared_drive_item.SharedDriveItem] = None, request_configuration: Optional[SharedDriveItemItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[shared_drive_item.SharedDriveItem]:
        """
        Update entity in shares
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[shared_drive_item.SharedDriveItem]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, shared_drive_item.SharedDriveItem, response_handler, error_mapping)
    
    @dataclass
    class SharedDriveItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SharedDriveItemItemRequestBuilderGetQueryParameters():
        """
        Access a shared DriveItem or a collection of shared items by using a **shareId** or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class SharedDriveItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

