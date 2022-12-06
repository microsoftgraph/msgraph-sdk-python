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

drive = lazy_import('msgraph.generated.models.drive')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
bundles_request_builder = lazy_import('msgraph.generated.users.item.drives.item.bundles.bundles_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.users.item.drives.item.bundles.item.drive_item_item_request_builder')
following_request_builder = lazy_import('msgraph.generated.users.item.drives.item.following.following_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.users.item.drives.item.following.item.drive_item_item_request_builder')
items_request_builder = lazy_import('msgraph.generated.users.item.drives.item.items.items_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.users.item.drives.item.items.item.drive_item_item_request_builder')
list_request_builder = lazy_import('msgraph.generated.users.item.drives.item.list.list_request_builder')
recent_request_builder = lazy_import('msgraph.generated.users.item.drives.item.recent.recent_request_builder')
root_request_builder = lazy_import('msgraph.generated.users.item.drives.item.root.root_request_builder')
search_with_q_request_builder = lazy_import('msgraph.generated.users.item.drives.item.search_with_q.search_with_q_request_builder')
shared_with_me_request_builder = lazy_import('msgraph.generated.users.item.drives.item.shared_with_me.shared_with_me_request_builder')
special_request_builder = lazy_import('msgraph.generated.users.item.drives.item.special.special_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.users.item.drives.item.special.item.drive_item_item_request_builder')

class DriveItemRequestBuilder():
    """
    Provides operations to manage the drives property of the microsoft.graph.user entity.
    """
    def bundles(self) -> bundles_request_builder.BundlesRequestBuilder:
        """
        Provides operations to manage the bundles property of the microsoft.graph.drive entity.
        """
        return bundles_request_builder.BundlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def following(self) -> following_request_builder.FollowingRequestBuilder:
        """
        Provides operations to manage the following property of the microsoft.graph.drive entity.
        """
        return following_request_builder.FollowingRequestBuilder(self.request_adapter, self.path_parameters)
    
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.drive entity.
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def list(self) -> list_request_builder.ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.drive entity.
        """
        return list_request_builder.ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    def root(self) -> root_request_builder.RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.drive entity.
        """
        return root_request_builder.RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    def special(self) -> special_request_builder.SpecialRequestBuilder:
        """
        Provides operations to manage the special property of the microsoft.graph.drive entity.
        """
        return special_request_builder.SpecialRequestBuilder(self.request_adapter, self.path_parameters)
    
    def bundles_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the bundles property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DriveItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/drives/{drive%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property drives for users
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
    
    def create_get_request_information(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of drives available for this user. Read-only.
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
    
    def create_patch_request_information(self,body: Optional[drive.Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property drives in users
        Args:
            body: 
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
    
    async def delete(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property drives for users
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
    
    def following_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the following property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[drive.Drive]:
        """
        A collection of drives available for this user. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[drive.Drive]
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
        return await self.request_adapter.send_async(request_info, drive.Drive, response_handler, error_mapping)
    
    def items_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[drive.Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[drive.Drive]:
        """
        Update the navigation property drives in users
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[drive.Drive]
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
        return await self.request_adapter.send_async(request_info, drive.Drive, response_handler, error_mapping)
    
    def recent(self,) -> recent_request_builder.RecentRequestBuilder:
        """
        Provides operations to call the recent method.
        Returns: recent_request_builder.RecentRequestBuilder
        """
        return recent_request_builder.RecentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def search_with_q(self,q: Optional[str] = None) -> search_with_q_request_builder.SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        Args:
            q: Usage: q='{q}'
        Returns: search_with_q_request_builder.SearchWithQRequestBuilder
        """
        if q is None:
            raise Exception("q cannot be undefined")
        return search_with_q_request_builder.SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    def shared_with_me(self,) -> shared_with_me_request_builder.SharedWithMeRequestBuilder:
        """
        Provides operations to call the sharedWithMe method.
        Returns: shared_with_me_request_builder.SharedWithMeRequestBuilder
        """
        return shared_with_me_request_builder.SharedWithMeRequestBuilder(self.request_adapter, self.path_parameters)
    
    def special_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the special property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DriveItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DriveItemRequestBuilderGetQueryParameters():
        """
        A collection of drives available for this user. Read-only.
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
    class DriveItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DriveItemRequestBuilder.DriveItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DriveItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

