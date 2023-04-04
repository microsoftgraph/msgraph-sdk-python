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
    from ...models import drive
    from ...models.o_data_errors import o_data_error
    from .bundles import bundles_request_builder
    from .bundles.item import drive_item_item_request_builder
    from .following import following_request_builder
    from .following.item import drive_item_item_request_builder
    from .items import items_request_builder
    from .items.item import drive_item_item_request_builder
    from .list import list_request_builder
    from .recent import recent_request_builder
    from .root import root_request_builder
    from .search_with_q import search_with_q_request_builder
    from .shared_with_me import shared_with_me_request_builder
    from .special import special_request_builder
    from .special.item import drive_item_item_request_builder

class DriveItemRequestBuilder():
    """
    Provides operations to manage the collection of drive entities.
    """
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
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def bundles_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the bundles property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .bundles.item import drive_item_item_request_builder
        from .following.item import drive_item_item_request_builder
        from .items.item import drive_item_item_request_builder
        from .special.item import drive_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete entity from drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def following_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the following property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .bundles.item import drive_item_item_request_builder
        from .following.item import drive_item_item_request_builder
        from .items.item import drive_item_item_request_builder
        from .special.item import drive_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None) -> Optional[drive.Drive]:
        """
        Retrieve the properties and relationships of a Drive resource. A Drive is the top-level container for a file system, such as OneDrive or SharePoint document libraries.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[drive.Drive]
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
        from ...models import drive

        return await self.request_adapter.send_async(request_info, drive.Drive, error_mapping)
    
    def items_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .bundles.item import drive_item_item_request_builder
        from .following.item import drive_item_item_request_builder
        from .items.item import drive_item_item_request_builder
        from .special.item import drive_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[drive.Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[drive.Drive]:
        """
        Update entity in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[drive.Drive]
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
        from ...models import drive

        return await self.request_adapter.send_async(request_info, drive.Drive, error_mapping)
    
    def search_with_q(self,q: Optional[str] = None) -> search_with_q_request_builder.SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        Args:
            q: Usage: q='{q}'
        Returns: search_with_q_request_builder.SearchWithQRequestBuilder
        """
        if q is None:
            raise Exception("q cannot be undefined")
        from .search_with_q import search_with_q_request_builder

        return search_with_q_request_builder.SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    def special_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the special property of the microsoft.graph.drive entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .bundles.item import drive_item_item_request_builder
        from .following.item import drive_item_item_request_builder
        from .items.item import drive_item_item_request_builder
        from .special.item import drive_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from drives
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
    
    def to_get_request_information(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a Drive resource. A Drive is the top-level container for a file system, such as OneDrive or SharePoint document libraries.
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
    
    def to_patch_request_information(self,body: Optional[drive.Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in drives
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
    def bundles(self) -> bundles_request_builder.BundlesRequestBuilder:
        """
        Provides operations to manage the bundles property of the microsoft.graph.drive entity.
        """
        from .bundles import bundles_request_builder

        return bundles_request_builder.BundlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def following(self) -> following_request_builder.FollowingRequestBuilder:
        """
        Provides operations to manage the following property of the microsoft.graph.drive entity.
        """
        from .following import following_request_builder

        return following_request_builder.FollowingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.drive entity.
        """
        from .items import items_request_builder

        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list(self) -> list_request_builder.ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.drive entity.
        """
        from .list import list_request_builder

        return list_request_builder.ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recent(self) -> recent_request_builder.RecentRequestBuilder:
        """
        Provides operations to call the recent method.
        """
        from .recent import recent_request_builder

        return recent_request_builder.RecentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> root_request_builder.RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.drive entity.
        """
        from .root import root_request_builder

        return root_request_builder.RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_with_me(self) -> shared_with_me_request_builder.SharedWithMeRequestBuilder:
        """
        Provides operations to call the sharedWithMe method.
        """
        from .shared_with_me import shared_with_me_request_builder

        return shared_with_me_request_builder.SharedWithMeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def special(self) -> special_request_builder.SpecialRequestBuilder:
        """
        Provides operations to manage the special property of the microsoft.graph.drive entity.
        """
        from .special import special_request_builder

        return special_request_builder.SpecialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DriveItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DriveItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a Drive resource. A Drive is the top-level container for a file system, such as OneDrive or SharePoint document libraries.
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
    class DriveItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

